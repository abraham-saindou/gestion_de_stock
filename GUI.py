from tkinter import *
from tkinter import ttk
from gestion import Database


class GUI(Toplevel):
    def __init__(self):
        self.base = Database("localhost", "abraham", "abraham", "boutique")
        self.root = Tk()
        self.root.title = "Gestion des stocks"
        self.root.geometry("1200x550")
        self.root.config(bg="snow3")

        self.__col_name = ['id', 'nom', 'description', 'prix en €', 'quantité', 'catégorie']
        self.add_values = []

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

    def get_data_add(self):

        values = [self.add_item_box()]

        print(values)

    def fields(self):
        win_root = Tk()
        win_root.title("Ajout d'un produit")
        win_root.geometry("600x300")
        self.box_frame = Frame(win_root, pady=25)
        self.box_frame.pack()

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

        enter = Button(self.box_frame, text="Entrée", width=10, height=1, command=self.getdata)
        enter.grid(row=6, column=0)

    def getdata(self):
        titre = self.nom.get()
        des = self.description.get()
        price = int(self.prix.get())
        quant = int(self.quantite.get())
        id_cat = int(self.id_categorie.get())
        cat = self.categorie.get()

        self.add_values = [titre, des, price, quant, id_cat, cat]
        self.base.add_product(titre, des, price, quant, id_cat, cat)
        self.liste()
        print(self.add_values)

    def menu(self):
        menu_choice = Menu(self.root)
        self.root.config(menu=menu_choice)
        organize_menu = Menu(menu_choice, tearoff=False)
        menu_choice.add_cascade(label="Product Managing", menu=organize_menu)
        organize_menu.add_command(label="Ajouter un produit", command=self.fields)
        organize_menu.add_command(label="Supprimer un produit")
        organize_menu.add_command(label="Modifier un produit")

    def run(self):
        self.liste()
        self.menu()
        self.root.mainloop()


app = GUI()
app.run()
