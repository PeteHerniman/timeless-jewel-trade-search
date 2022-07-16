from tkinter import ttk

import tkinter as tk


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create Widgets
        # Jewel buttons
        self.brutal_restraint_button = ttk.Button(self, text='Brutal Restraint', command=self.brutal_restraint_button_clicked)
        self.brutal_restraint_button.grid(row=1, column=0, padx=10, sticky=tk.NSEW)
        self.elegant_hubris_button = ttk.Button(self, text='Elegant Hubris', command=self.elegant_hubris_button_clicked)
        self.elegant_hubris_button.grid(row=1, column=1, padx=10, sticky=tk.NSEW)
        self.glorious_vanity_button = ttk.Button(self, text='Glorious Vanity', command=self.glorious_vanity_button_clicked)
        self.glorious_vanity_button.grid(row=1, column=2, padx=10, sticky=tk.NSEW)
        self.lethal_pride_button = ttk.Button(self, text='Lethal Pride', command=self.lethal_pride_button_clicked)
        self.lethal_pride_button.grid(row=1, column=3, padx=10, sticky=tk.NSEW)
        self.militant_faith_button = ttk.Button(self, text='Militant Faith', command=self.militant_faith_button_clicked)
        self.militant_faith_button.grid(row=1, column=4, padx=10, sticky=tk.NSEW)

        # Name buttons
        self.name_var1 = tk.BooleanVar()
        self.name_var1.set(False)
        self.name_checkbutton1 = ttk.Checkbutton(self, text='', variable=self.name_var1, state='disabled')
        self.name_checkbutton1.grid(row=2, column=0, padx=10)
        self.name_var2 = tk.BooleanVar()
        self.name_var2.set(False)
        self.name_checkbutton2 = ttk.Checkbutton(self, text='', variable=self.name_var2, state='disabled')
        self.name_checkbutton2.grid(row=2, column=1, padx=10)
        self.name_var3 = tk.BooleanVar()
        self.name_var3.set(False)
        self.name_checkbutton3 = ttk.Checkbutton(self, text='', variable=self.name_var3, state='disabled')
        self.name_checkbutton3.grid(row=2, column=2, padx=10)

        # Value entry
        self.seed_var = tk.StringVar()
        self.seed_entry = ttk.Entry(self, textvariable=self.seed_var, width=30)
        self.seed_entry.grid(row=3, column=0, columnspan=4, sticky=tk.NSEW)

        # Search button
        self.search_button = ttk.Button(self, text='Search', command=self.search_button_clicked)
        self.search_button.grid(row=3, column=4, columnspan=1, padx=10)

        # Message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=4, column=0, columnspan=5, sticky=tk.W)

        # Set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def brutal_restraint_button_clicked(self):
        """
        Handle brutal restraint button click event
        :return:
        """
        self.controller.select_jewel('brutal_restraint')

    def elegant_hubris_button_clicked(self):
        """
        Handle elegant hubris button click event
        :return:
        """
        self.controller.select_jewel('elegant_hubris')

    def glorious_vanity_button_clicked(self):
        """
        Handle glorious vanity button click event
        :return:
        """
        self.controller.select_jewel('glorious_vanity')

    def lethal_pride_button_clicked(self):
        """
        Handle lethal pride button click event
        :return:
        """
        self.controller.select_jewel('lethal_pride')

    def militant_faith_button_clicked(self):
        """
        Handle militant faith button click event
        :return:
        """
        self.controller.select_jewel('militant_faith')

    def set_name_checkbutton_values(self, values, enabled):
        """
        Updates the name buttons with the given names
        :return:
        """
        if values and len(values) == 3:
            # Set text values
            self.name_checkbutton1['text'] = values[0]
            self.name_checkbutton2['text'] = values[1]
            self.name_checkbutton3['text'] = values[2]
            # Set whether checkbuttons are enabled
            self.name_checkbutton1['state'] = enabled
            self.name_checkbutton2['state'] = enabled
            self.name_checkbutton3['state'] = enabled
            # Unselect checkbuttons
            self.name_var1.set(False)
            self.name_var2.set(False)
            self.name_var3.set(False)

    def search_button_clicked(self):
        """
        Handle search button click event
        :return:
        """
        self.controller.search(self.name_var1.get(), self.name_var2.get(), self.name_var3.get(), self.seed_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
