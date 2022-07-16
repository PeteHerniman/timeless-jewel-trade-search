import tkinter as tk

from controller import Controller
from model import Model
from view import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Timeless Jewel Trade Search')
        self.resizable(True, False)
        self.geometry('700x91')

        # Create a model
        model = Model()

        # Create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        view.columnconfigure(tuple(range(5)), weight=1)
        view.pack(fill='x')

        # Create a controller
        controller = Controller(model, view)

        # Set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
