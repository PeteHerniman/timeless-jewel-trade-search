from tkinter import ttk

import tkinter as tk


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create Widgets
        # PoE Session ID Field
        self.session_id_frame = ttk.Frame(self)
        self.session_id_frame.pack(fill=tk.X)
        self.session_id_label = ttk.Label(self.session_id_frame, text='PoE Session ID:', justify=tk.RIGHT)
        self.session_id_label.pack(side=tk.LEFT, padx=5, pady=5)
        self.session_id_entry = ttk.Entry(self.session_id_frame, width=100)
        self.session_id_entry.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        # Jewel buttons
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(fill=tk.X)
        self.brutal_restraint_button = ttk.Button(self.buttons_frame, text='Brutal Restraint', command=self.brutal_restraint_button_clicked)
        self.brutal_restraint_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.elegant_hubris_button = ttk.Button(self.buttons_frame, text='Elegant Hubris', command=self.elegant_hubris_button_clicked)
        self.elegant_hubris_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.glorious_vanity_button = ttk.Button(self.buttons_frame, text='Glorious Vanity', command=self.glorious_vanity_button_clicked)
        self.glorious_vanity_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.lethal_pride_button = ttk.Button(self.buttons_frame, text='Lethal Pride', command=self.lethal_pride_button_clicked)
        self.lethal_pride_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.militant_faith_button = ttk.Button(self.buttons_frame, text='Militant Faith', command=self.militant_faith_button_clicked)
        self.militant_faith_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        # Name buttons
        self.name_frame = ttk.Frame(self)
        self.name_frame.pack(fill=tk.X)
        self.name_var1 = tk.BooleanVar()
        self.name_var1.set(False)
        self.name_checkbutton1 = ttk.Checkbutton(self.name_frame, text='', variable=self.name_var1, state='disabled')
        self.name_checkbutton1.pack(side=tk.LEFT, padx=5)
        self.name_var2 = tk.BooleanVar()
        self.name_var2.set(False)
        self.name_checkbutton2 = ttk.Checkbutton(self.name_frame, text='', variable=self.name_var2, state='disabled')
        self.name_checkbutton2.pack(side=tk.LEFT, padx=5)
        self.name_var3 = tk.BooleanVar()
        self.name_var3.set(False)
        self.name_checkbutton3 = ttk.Checkbutton(self.name_frame, text='', variable=self.name_var3, state='disabled')
        self.name_checkbutton3.pack(side=tk.LEFT, padx=5)

        # Seed entry and search button.
        self.seeds_frame = ttk.Frame(self)
        self.seeds_frame.pack(fill=tk.X)
        self.seed_var = tk.StringVar()
        self.seed_entry = ttk.Entry(self.seeds_frame, textvariable=self.seed_var, width=100)
        self.seed_entry.pack(side=tk.LEFT, expand=True)
        self.search_button = ttk.Button(self.seeds_frame, text='Search', command=self.search_button_clicked)
        self.search_button.pack(side=tk.LEFT)

        # Message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.pack(fill=tk.X, padx=5)

        # Set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller: The controller
        """
        self.controller = controller

    def brutal_restraint_button_clicked(self):
        """
        Handle brutal restraint button click event
        """
        self.controller.select_jewel('brutal_restraint')

    def elegant_hubris_button_clicked(self):
        """
        Handle elegant hubris button click event
        """
        self.controller.select_jewel('elegant_hubris')

    def glorious_vanity_button_clicked(self):
        """
        Handle glorious vanity button click event
        """
        self.controller.select_jewel('glorious_vanity')

    def lethal_pride_button_clicked(self):
        """
        Handle lethal pride button click event
        """
        self.controller.select_jewel('lethal_pride')

    def militant_faith_button_clicked(self):
        """
        Handle militant faith button click event
        """
        self.controller.select_jewel('militant_faith')

    def set_name_checkbutton_values(self, values, enabled):
        """
        Updates the name checkbuttons with the given names
        :param values: The jewel names
        :param enabled: Whether the checkbuttons are enabled
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
        """
        poe_session_id = self.session_id_entry.get()
        self.controller.search(poe_session_id, self.name_var1.get(), self.name_var2.get(), self.name_var3.get(), self.seed_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message: The message
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
