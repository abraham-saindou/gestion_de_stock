from tkinter import *
from tkinter import ttk, messagebox
from gestion import Database


class GUI(Toplevel):
    def __init__(self):
        self.base = Database("localhost", "abraham", "abraham", "boutique")
        self.root = Tk()
        self.root.title = "Gestion des stocks"
        self.root.geometry("1200x550")
        self.root.config(bg="snow3")
        self.state = 0

        self.__col_name = ['id', 'nom', 'description', 'prix en €', 'quantité', 'catégorie']
        self.add_values = []

    def create_tree(self):
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
            print(self.box_list, type(self.box_list))

    def clear_text(self):
        if self.state == 1 or 3:
            self.nom.delete(0, 'end')
            self.description.delete(0, 'end')
            self.prix.delete(0, 'end')
            self.quantite.delete(0, 'end')
            self.id_categorie.delete(0, 'end')
            self.categorie.delete(0, 'end')
        if self.state == 2:
            self.id_to_del.delete(0, 'end')

    def close_win(self):
        self.win_root.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.win_root.destroy()

    def ask(self):
        q = Label(self.box_frame, text="Do you want to quit ?")
        q.grid(row=7, column=0)
        yes = Button(self.box_frame, text="Yes", width=10, height=1, command=self.close_win)
        yes.grid(row=7, column=1)
        no = Button(self.box_frame, text="No", width=10, height=1)
        no.grid(row=7, column=2)

    def addto_db(self):
        self.win_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        titre = self.nom.get()
        des = self.description.get()
        price = int(self.prix.get())
        quant = int(self.quantite.get())
        id_cat = int(self.id_categorie.get())
        cat = self.categorie.get()
        self.clear_text()

        self.add_values = [titre, des, price, quant, id_cat, cat]
        self.base.add_product(titre, des, price, quant, id_cat, cat)
        item = self.base.insert_last_item()
        for val in item:
            self.box_list.insert('', END, values=val)

    def modify_product(self):
        titre = self.nom.get()
        des = self.description.get()
        price = int(self.prix.get())
        quant = int(self.quantite.get())
        id_cat = int(self.id_categorie.get())
        cat = self.categorie.get()
        self.clear_text()

        self.add_values = [titre, des, price, quant, id_cat, cat]
        self.base.mod_product(titre, des, price, quant, id_cat, cat)

    def del_row_db(self):
        row = self.id_to_del.get()
        self.clear_text()
        row_int = int(row)
        lst = [row_int]
        self.base.del_product(lst)
        list_tree = self.box_list.get_children()
        for i, obj in enumerate(list_tree):
            if self.box_list.item(obj)['values'][0] == row_int:
                self.box_list.delete(obj)

    def change_state(self, state):
        self.state = state
        self.fields()

    def get_data_add(self):

        values = [self.add_item_box()]

        print(values)

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
                self.win_root.protocol("WM_DELETE_WINDOW", self.on_closing)
            case 2:
                self.win_root.title("Supprimer un produit")
                Labl1 = Label(self.box_frame, text="ID")
                Labl1.grid(row=0, column=0)
                self.id_to_del = Entry(self.box_frame, width=10)
                self.id_to_del.grid(row=0, column=1)
                enter = Button(self.box_frame, text="Entrée", width=10, height=1, command=self.del_row_db)
                enter.grid(row=0, column=2)
                self.win_root.protocol("WM_DELETE_WINDOW", self.on_closing)
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
                enter = Button(self.box_frame, text="Entrée", width=10, height=1, command=self.del_row_db)
                enter.grid(row=0, column=2)
                self.win_root.protocol("WM_DELETE_WINDOW", self.on_closing)


    def menu(self):
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


app = GUI()
app.run()
