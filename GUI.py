from tkinter import *
import gestion


class GUI(gestion.Database):
    def __init__(self):
        self.root = Tk()
        self.root.title = "Gestion des stocks"
        self.root.geometry("650x550")
        self.root.config(bg="snow3")

    def run(self):
        self.root.mainloop()


if __name__ == "__GUI__":
    app = GUI()
    app.run()