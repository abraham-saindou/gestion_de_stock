from tkinter import *
from tkinter import ttk
from gestion import Database


class GUI:
    def __init__(self):
        self.base = Database("localhost", "abraham", "abraham", "boutique")
        self.root = Tk()
        self.root.title = "Gestion des stocks"
        self.root.geometry("1200x550")
        self.root.config(bg="snow3")

        self.__col_name = ['id', 'nom', 'description', 'prix en €', 'quantité', 'catégorie']

        self.add_product = Button(self.root, text="Ajouter un produit")
        self.del_product = Button(self.root, text="Supprimer un produit")
        self.mod_product = Button(self.root, text="Modifier un produit")

    def liste(self):

        data = self.base.load("produit")
        print(data)

        if self.base.connector.is_connected():
            self.box_list = ttk.Treeview(self.root, columns=self.__col_name, show='headings')
            for index, item in enumerate(self.__col_name):
                self.box_list.column(f"{index}", anchor=CENTER, width=200)
                self.box_list.heading(item, text=item.upper())
            for obj in data:
                self.box_list.insert('', END, values=obj)
            self.box_list.pack()

    def buttons(self):
        self.add_product.pack()
        self.del_product.pack()
        self.mod_product.pack()

    def menu(self):
        menu_choice = Menu(self.root)
        self.root.config(menu=menu_choice)
        organize_menu = Menu(menu_choice, tearoff=False)
        menu_choice.add_cascade(label="Product Managing", menu=organize_menu)
        organize_menu.add_command(label="Ajouter un produit")
        organize_menu.add_command(label="Supprimer un produit")
        organize_menu.add_command(label="Modifier un produit")

    def run(self):
        self.liste()
        self.menu()
        self.buttons()
        self.root.mainloop()


app = GUI()
app.run()
