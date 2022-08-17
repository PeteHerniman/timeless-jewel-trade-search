import copy
import webbrowser

import requests


class Model:
    BASE_QUERY = \
        {
            "query": {
                "status": {
                    "option": "online"
                },
                "stats": [{
                    "type": "count",
                    "min": 1,
                    "filters": []
                }]
            }
        }
    BASE_SEARCH_FILTER = \
        {
            "id": "",
            "value": {
                "min": 0,
                "max": 0
            }
        }
    HEADERS = \
        {
            'User-Agent': 'Timeless Jewel Trade Search 1.2.0'
        }
    TIMELESS_STATS = \
        {
            "brutal_restraint": [
                {
                    "id": "explicit.pseudo_timeless_jewel_asenath",
                    "name": "Asenath"
                },
                {
                    "id": "explicit.pseudo_timeless_jewel_balbala",
                    "name": "Balbala"
                },
                {
                    "id": "explicit.pseudo_timeless_jewel_nasima",
                    "name": "Nasima"
                }
            ],
            "elegant_hubris": [
                {
                    "id": "explicit.pseudo_timeless_jewel_cadiro",
                    "name": "Cadiro"
                },
                {
                    "id": "explicit.pseudo_timeless_jewel_caspiro",
                    "name": "Caspiro"
                },
                {
                    "id": "explicit.pseudo_timeless_jewel_victario",
                    "name": "Victario",
                    "text": "Commissioned # coins to commemorate Victario",
                    "type": "explicit"
                }
            ],
            "glorious_vanity": [
                {
                    "id": "explicit.pseudo_timeless_jewel_ahuana",
                    "name": "Ahuana"
                },
                {
                    "id": "explicit.pseudo_timeless_jewel_doryani",
                    "name": "Doryani"
                },
                {
                    "id": "explicit.pseudo_timeless_jewel_xibaqua",
                    "name": "Xibaqua"
                }
            ],
            "lethal_pride": [
                {
                    "id": "explicit.pseudo_timeless_jewel_akoya",
                    "name": "Akoya"
                },
                {
                    "id": "explicit.pseudo_timeless_jewel_kaom",
                    "name": "Kaom"
                },
                {
                    "id": "explicit.pseudo_timeless_jewel_rakiata",
                    "name": "Rakiata"
                }
            ],
            "militant_faith": [
                {
                    "id": "explicit.pseudo_timeless_jewel_avarius",
                    "name": "Avarius"
                },
                {
                    "id": "explicit.pseudo_timeless_jewel_dominus",
                    "name": "Dominus"
                },
                {
                    "id": "explicit.pseudo_timeless_jewel_maxarius",
                    "name": "Maxarius"
                }
            ]
        }

    def __init__(self):
        self._jewel_selected = None

    def set_jewel_selected(self, jewel_selected):
        """
        Sets the currently selected jewel
        :param jewel_selected: The selected jewel
        """
        self._jewel_selected = jewel_selected

    def get_timeless_stats_json(self):
        """
        Gets the timeless stats json for the currently selected jewel
        :return: The timeless stats json
        """
        return self.TIMELESS_STATS[self._jewel_selected]

    def get_leagues(self):
        """
        Gets the current PC leagues
        :return: List of PC leagues
        """
        leagues_json = requests.get('https://www.pathofexile.com/api/trade/data/leagues', headers=self.HEADERS).json()
        pc_leagues = filter(lambda league: league['realm'] == 'pc', leagues_json['result'])
        pc_league_ids = map(lambda league: league['id'], pc_leagues)
        return list(pc_league_ids)

    def search(self, poe_session_id, league_id, search_for_first_name, search_for_second_name, search_for_third_name, seeds):
        """
        Opens a search on in the browser for timeless jewels with the desired names and seeds
        :param poe_session_id: The PoE session ID
        :param league_id: The league ID
        :param search_for_first_name: Whether to search for jewels with the first name
        :param search_for_second_name: Whether to search for jewels with the second name
        :param search_for_third_name: Whether to search for jewels with the third name
        :param seeds: The seeds to search for
        """
        # Validate inputs
        if not self._jewel_selected:
            raise ValueError('No jewel type selected.')
        if not search_for_first_name and not search_for_second_name and not search_for_third_name:
            raise ValueError('At least one name must be selected.')
        if not self.seeds_validated(seeds):
            raise ValueError('At least one seed must be given, and seeds must be digits separated by commas.')

        # Create list of search filters
        search_filters = []
        if search_for_first_name:
            search_filters.extend(self.create_search_filters(0, seeds))
        if search_for_second_name:
            search_filters.extend(self.create_search_filters(1, seeds))
        if search_for_third_name:
            search_filters.extend(self.create_search_filters(2, seeds))

        # Check if the search will be too complex
        max_search_filters = 188 if poe_session_id else 38
        if len(search_filters) > max_search_filters:
            raise ValueError(f'Too many names/seeds selected. Max value of names*seeds is {max_search_filters}. Current names*seeds={str(len(search_filters))}.')

        # Add search filters to query
        query = self.BASE_QUERY.copy()
        query['query']['stats'][0]['filters'] = search_filters

        # Run query
        session = requests.Session()
        if poe_session_id:
            session.cookies.update({'POESESSID': poe_session_id})
        json_response = session.post(f'https://www.pathofexile.com/api/trade/search/{league_id}', json=query, headers=self.HEADERS).json()
        if 'id' in json_response:
            url = f'https://www.pathofexile.com/trade/search/{league_id}/' + json_response['id']
            webbrowser.open(url, new=2)
        elif 'error' in json_response:
            error = json_response['error']
            error_code = error['code']
            error_message = error['message']
            raise Exception(f'Error {error_code}: {error_message}')
        else:
            raise Exception(f'Unknown error: {json_response}')

    def create_search_filters(self, name_id, seeds):
        """
        Creates a search filter for the given name ID and seeds
        :param name_id: The name ID to create the search filter for
        :param seeds: The seeds to create the search filter for
        :return: The search filter
        """
        search_filters = []
        for seed in seeds:
            search_filter = copy.deepcopy(self.BASE_SEARCH_FILTER)
            search_filter['id'] = self.TIMELESS_STATS[self._jewel_selected][name_id]['id']
            search_filter['value']['min'] = int(seed)
            search_filter['value']['max'] = int(seed)
            search_filters.append(search_filter)
        return search_filters

    def seeds_validated(self, seeds):
        """
        Validates the seeds
        :param seeds: The seeds to validate
        :return: True if valid, False otherwise
        """
        if len(seeds) > 0:
            for seed in seeds:
                if not seed.isdigit():
                    return False
        return True
