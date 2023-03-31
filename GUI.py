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
        self.state = 0  # Variable used when selecting an option from menu

        self.__col_name = ['id', 'nom', 'description', 'prix en €', 'quantité', 'catégorie']

    def create_tree(self):
        data = self.base.load("produit")
        if self.base.connector.is_connected():
            self.tree_box = ttk.Treeview(self.root, columns=self.__col_name, show='headings', height=20)
            # Create a treeview to display data loaded from table "produit"
            for index, item in enumerate(self.__col_name):
                self.tree_box.column(f"{index}", anchor=CENTER, width=200)
                self.tree_box.heading(item, text=item.upper())
            for obj in data:
                self.tree_box.insert('', END, values=obj)
            self.tree_box.pack()
            print(self.tree_box, type(self.tree_box))

    def clear_text(self):  # Clear all data entries
        if self.state == 1 or 3:
            self.nom.delete(0, 'end')
            self.description.delete(0, 'end')
            self.prix.delete(0, 'end')
            self.quantite.delete(0, 'end')
            self.id_categorie.delete(0, 'end')
            self.categorie.delete(0, 'end')
        if self.state == 2:
            self.id_to_del.delete(0, 'end')
        if self.state == 3:
            self.nom.delete(0, 'end')
            self.description.delete(0, 'end')
            self.prix.delete(0, 'end')
            self.quantite.delete(0, 'end')
            self.id_categorie.delete(0, 'end')
            self.categorie.delete(0, 'end')
            self.id_to_mod.delete(0, 'end')

    def addto_db(self):  # Store data from entries
        titre = self.nom.get()
        des = self.description.get()
        price = int(self.prix.get())
        quant = int(self.quantite.get())
        id_cat = int(self.id_categorie.get())
        cat = self.categorie.get()
        self.clear_text()

        self.base.add_product(titre, des, price, quant, id_cat, cat)
        item = self.base.insert_last_item()
        for val in item:  # inserting new item into tree
            self.tree_box.insert('', END, values=val)

    def del_row_db(self):
        row = self.id_to_del.get()  # Get id from entry then converts it into int
        row_int = int(row)
        lst = [row_int]
        self.clear_text()
        self.base.del_product(lst)

        list_tree = self.tree_box.get_children() # Store tree elements (id)
        for obj in list_tree:
            if self.tree_box.item(obj)['values'][0] == row_int:  # access tree id then compares it to selected id
                self.tree_box.delete(obj)

    def modify_product(self):  # Get tree id and data from entries
        list_tree = self.tree_box.get_children()
        titre = self.nom.get()
        des = self.description.get()
        price = int(self.prix.get())
        quant = int(self.quantite.get())
        id_cat = int(self.id_categorie.get())
        cat = self.categorie.get()
        id_modify = int(self.id_to_mod.get())
        self.clear_text()
        for obj in list_tree:
            if self.tree_box.item(obj)['values'][0] == id_modify:
                val = self.tree_box.item(obj)['values'][0]  # Stores id to modify
        self.base.mod_product(titre, des, price, quant, id_cat, cat, val)
        self.tree_box.destroy()
        self.create_tree()

    def change_state(self, state):  # Set state then invokes fields to create a new window
        self.state = state
        self.fields()

    def fields(self):
        self.win_root = Tk()
        self.win_root.geometry("600x300")
        self.box_frame = Frame(self.win_root, pady=25)
        self.box_frame.pack()

        match self.state:
            case 1:
                self.win_root.title("Ajouter un produit")
                Labl1 = Label(self.box_frame, text="Nom")
                Labl1.grid(row=0, column=0)
                self.nom = Entry(self.box_frame, width=30)
                self.nom.grid(row=0, column=1)
                Labl2 = Label(self.box_frame, text="Description")
                Labl2.grid(row=1, column=0)
                self.description = Entry(self.box_frame, width=30)
                self.description.grid(row=1, column=1)
                Labl3 = Label(self.box_frame, text="Prix")
                Labl3.grid(row=2, column=0)
                self.prix = Entry(self.box_frame, width=10)
                self.prix.grid(row=2, column=1)
                Labl4 = Label(self.box_frame, text="Quantité")
                Labl4.grid(row=3, column=0)
                self.quantite = Entry(self.box_frame, width=10)
                self.quantite.grid(row=3, column=1)
                Labl5 = Label(self.box_frame, text="ID_Catégorie")
                Labl5.grid(row=4, column=0)
                self.id_categorie = Entry(self.box_frame, width=10)
                self.id_categorie.grid(row=4, column=1)
                Labl6 = Label(self.box_frame, text="Catégorie")
                Labl6.grid(row=5, column=0)
                self.categorie = Entry(self.box_frame, width=30)
                self.categorie.grid(row=5, column=1)
                enter = Button(self.box_frame, text="Entrée", width=10, height=1, command=self.addto_db)
                enter.grid(row=6, column=0)
            case 2:
                self.win_root.title("Supprimer un produit")
                Labl1 = Label(self.box_frame, text="ID")
                Labl1.grid(row=0, column=0)
                self.id_to_del = Entry(self.box_frame, width=10)
                self.id_to_del.grid(row=0, column=1)
                enter = Button(self.box_frame, text="Entrée", width=10, height=1, command=self.del_row_db)
                enter.grid(row=0, column=2)
            case 3:
                self.win_root.title("Modifier un produit")
                Labl1 = Label(self.box_frame, text="Nom")
                Labl1.grid(row=0, column=0)
                self.nom = Entry(self.box_frame, width=30)
                self.nom.grid(row=0, column=1)
                Labl2 = Label(self.box_frame, text="Description")
                Labl2.grid(row=1, column=0)
                self.description = Entry(self.box_frame, width=30)
                self.description.grid(row=1, column=1)
                Labl3 = Label(self.box_frame, text="Prix")
                Labl3.grid(row=2, column=0)
                self.prix = Entry(self.box_frame, width=10)
                self.prix.grid(row=2, column=1)
                Labl4 = Label(self.box_frame, text="Quantité")
                Labl4.grid(row=3, column=0)
                self.quantite = Entry(self.box_frame, width=10)
                self.quantite.grid(row=3, column=1)
                Labl5 = Label(self.box_frame, text="ID_Catégorie")
                Labl5.grid(row=4, column=0)
                self.id_categorie = Entry(self.box_frame, width=10)
                self.id_categorie.grid(row=4, column=1)
                Labl6 = Label(self.box_frame, text="Catégorie")
                Labl6.grid(row=5, column=0)
                self.categorie = Entry(self.box_frame, width=30)
                self.categorie.grid(row=5, column=1)
                Labl7 = Label(self.box_frame, text="ID à modifier")
                Labl7.grid(row=6, column=0)
                self.id_to_mod = Entry(self.box_frame, width=30)
                self.id_to_mod.grid(row=6, column=1)
                enter = Button(self.box_frame, text="Entrée", width=10, height=1, command=self.modify_product)
                enter.grid(row=0, column=2)

    def menu(self):  # Menu parameters
        menu_choice = Menu(self.root)
        self.root.config(menu=menu_choice)
        organize_menu = Menu(menu_choice, tearoff=False)
        menu_choice.add_cascade(label="Product Managing", menu=organize_menu)
        organize_menu.add_command(label="Ajouter un produit", command=lambda: self.change_state(1))
        organize_menu.add_command(label="Supprimer un produit", command=lambda: self.change_state(2))
        organize_menu.add_command(label="Modifier un produit", command=lambda: self.change_state(3))

    def run(self):
        self.create_tree()
        self.menu()
        self.root.mainloop()
        self.base.close_connector()


app = GUI()
app.run()
