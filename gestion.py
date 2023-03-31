import mysql.connector


class Database:
    def __init__(self, host, user, password, database):  # Create tools to access database
        self.connector = mysql.connector.connect(
            host=str(host),
            user=str(user),
            password=str(password),
            database=str(database),
            )
        self.cursor = self.connector.cursor()

    def load(self, table_name):  # Get data from tables
        self.cursor.execute("SELECT produit.id, produit.nom, produit.description, produit.prix, produit.quantite,"
                            " categorie.nom FROM " + str(table_name) + " JOIN categorie ON id_categorie = categorie.id")
        data = self.cursor.fetchall()
        return data

    def close_connector(self):
        self.connector.close()

    # Function to add an element
    def add_product(self, nom, description, prix, quantite, id_categorie, categorie):
        obj = self.load("produit")
        add_item = "INSERT into produit (nom, description, prix, quantite, id_categorie) VALUES(%s,%s,%s,%s,%s)"
        add_cat = "INSERT into categorie (nom) VALUES (%s)"
        data = (nom, description, prix, quantite, id_categorie)  # Create a tuple to insert into table
        cat = [categorie]

        if nom not in obj:  # Check if element name is in table
            self.cursor.execute(add_item, data)
            self.connector.commit()
        if categorie not in obj:   # Check if element categories is in table
            self.cursor.execute(add_cat, cat)
            self.connector.commit()

    # Function to get the newly added element to insert into tree
    def insert_last_item(self):
        self.cursor.execute("SELECT produit.id, produit.nom, produit.description, produit.prix, produit.quantite,"
                            " categorie.nom FROM produit JOIN categorie ON id_categorie = categorie.id ORDER BY ID DESC LIMIT 1")
        item = self.cursor.fetchall()
        return item

    # Function to delete an element
    def del_product(self, num):
        del_item = "DELETE FROM produit WHERE id = %s"
        self.cursor.execute(del_item, num)
        self.connector.commit()

    # Function to modify an element
    def mod_product(self, nom, description, prix, quantite, id_categorie, categorie, id_select):
        mod_item = "UPDATE produit SET nom = %s, description = %s, prix = %s, quantite = %s, id_categorie = %s WHERE id = %s;"
        data = (nom, description, prix, quantite, id_categorie, id_select)
        self.cursor.execute(mod_item, data)
        self.connector.commit()
