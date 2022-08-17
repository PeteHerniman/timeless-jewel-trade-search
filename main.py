import tkinter as tk

from controller import Controller
from model import Model
from view import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Timeless Jewel Trade Search 1.2.0')
        self.resizable(False, False)

        # Create a model
        model = Model()

        # Create a view and place it on the root window
        view = View(self)
        view.pack(fill=tk.BOTH, expand=True)

        # Create a controller
        controller = Controller(model, view)

        # Set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
