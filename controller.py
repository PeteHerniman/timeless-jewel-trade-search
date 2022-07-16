class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def select_jewel(self, jewel_selected):
        """
        Updates the name checkboxes with the names for the given jewel
        :return:
        """
        if jewel_selected:
            self.model.set_jewel_selected(jewel_selected)
            timeless_stats = self.model.get_timeless_stats_json()
            if timeless_stats:
                stat_names = [timeless_stat['name'] for timeless_stat in timeless_stats]
                self.view.set_name_checkbutton_values(stat_names, '!disabled')

    def search(self, search_for_first_name, search_for_second_name, search_for_third_name, seed):
        """
        Searches for timeless jewels with the selected names and seed values
        :return:
        """
        try:
            self.model.search(search_for_first_name, search_for_second_name, search_for_third_name, seed.split(','))
        except ValueError as error:
            error_message = 'Error searching for timeless jewels: ' + str(error)
            print(error_message)
            self.view.show_error(error_message)
