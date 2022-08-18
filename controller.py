class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_leagues(self):
        """
        Updates the league selection menu with the leagues from the model
        """
        try:
            leagues = self.model.get_leagues()
            if leagues:
                self.view.set_league_menu_values(leagues)
            else:
                raise Exception('No leagues found')
        except Exception as error:
            error_message = 'Error updating leagues: ' + str(error)
            self.view.show_error(error_message)

    def select_jewel(self, jewel_selected):
        """
        Updates the name checkboxes with the names for the given jewel
        :param jewel_selected: The name of the jewel selected
        """
        if jewel_selected:
            self.model.set_jewel_selected(jewel_selected)
            timeless_stats = self.model.get_timeless_stats_json()
            if timeless_stats:
                stat_names = [timeless_stat['name'] for timeless_stat in timeless_stats]
                self.view.set_name_checkbutton_values(stat_names, '!disabled')

    def search(self, poe_session_id, league_id, search_for_first_name, search_for_second_name, search_for_third_name, seed):
        """
        Searches for timeless jewels with the selected names and seed values and opens the results in the browser
        :param poe_session_id: The PoE session id
        :param league_id: The league id
        :param search_for_first_name: Whether to search for jewels with the first name
        :param search_for_second_name: Whether to search for jewels with the second name
        :param search_for_third_name: Whether to search for jewels with the third name
        :param seed: The seed entry value
        :return: None
        """
        self.view.show_error('')
        try:
            self.model.search(poe_session_id, league_id, search_for_first_name, search_for_second_name, search_for_third_name, seed.split(','))
        except Exception as error:
            error_message = 'Error searching for timeless jewels: ' + str(error)
            print(error_message)
            self.view.show_error(error_message)
