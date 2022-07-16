import copy
import json
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
            'User-Agent': 'Timeless Jewel Trade Search 1.0.0'
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
        :param jewel_selected:
        :return:
        """
        self._jewel_selected = jewel_selected

    def get_timeless_stats_json(self):
        """
        Gets the timeless stats json for the currently selected jewel
        :return:
        """
        return self.TIMELESS_STATS[self._jewel_selected]

    def search(self, search_for_first_name, search_for_second_name, search_for_third_name, seeds):
        """
        Opens a search on in the browser for timeless jewels with the desired names and seeds
        :param search_for_first_name:
        :param search_for_second_name:
        :param search_for_third_name:
        :param seeds:
        :return:
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
        if len(search_filters) > 38:
            raise ValueError('Too many names/seeds selected. Max value of names*seeds is 38. Current names*seeds=' + str(len(search_filters)) + '.')

        # Add search filters to query
        query = self.BASE_QUERY.copy()
        query['query']['stats'][0]['filters'] = search_filters

        # Run query
        json_response = requests.post('https://www.pathofexile.com/api/trade/search/Sentinel', json=query, headers=self.HEADERS).json()
        url = 'https://www.pathofexile.com/trade/search/Sentinel/' + json_response['id']
        webbrowser.open(url, new=2)

    def create_search_filters(self, name_id, seeds):
        """
        Creates a search filter for the given name ID and seed
        :param name_id:
        :param seeds:
        :return:
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
        :param seeds:
        :return:
        """
        if len(seeds) > 0:
            for seed in seeds:
                if not seed.isdigit():
                    return False
        return True
