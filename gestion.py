import mysql.connector


class Database:
    def __init__(self, host, user, password, database):
        self.connector = mysql.connector.connect(
            host=str(host),
            user=str(user),
            password=str(password),
            database=str(database),
            )
        self.cursor = self.connector.cursor()

    def connection(self):
        if self.connector.is_connected():
            cursor = self.connector.cursor()

    def load(self, table_name):
        self.cursor.execute("SELECT produit.id, produit.nom, produit.description, produit.prix, produit.quantite,"
                            " categorie.nom FROM " + str(table_name) + " JOIN categorie ON id_categorie = categorie.id")
        data = self.cursor.fetchall()
        return data

    def close_connector(self):
        self.connector.close()

    def add_product(self, nom, description, prix, quantite, id_categorie, categorie):
        obj = self.load("produit")
        add_item = "INSERT into produit (nom, description, prix, quantite, id_categorie) VALUES(%s,%s,%s,%s,%s)"
        add_cat = "INSERT into categorie (nom) VALUES (%s)"
        data = (nom, description, prix, quantite, id_categorie)
        cat = [categorie]
        if nom not in obj:
            self.cursor.execute(add_item, data)
            self.connector.commit()
        if categorie not in obj:
            self.cursor.execute(add_cat, cat)
            self.connector.commit()

    def insert_last_item(self):
        self.cursor.execute("SELECT produit.id, produit.nom, produit.description, produit.prix, produit.quantite,"
                            " categorie.nom FROM produit JOIN categorie ON id_categorie = categorie.id ORDER BY ID DESC LIMIT 1")
        item = self.cursor.fetchall()
        return item

    def del_product(self, num):
        del_item = "DELETE FROM produit WHERE id = %s"
        self.cursor.execute(del_item, num)
        self.connector.commit()

    def select_deleted_product(self, num):
        selected = "SELECT FROM produit WHERE id = %s"
        self.cursor.execute(selected, num)
        self.connector.commit()

    def mod_product(self, nom, description, prix, quantite, id_categorie, categorie):
        mod_item = "UPDATE produit SET nom = ?, description = ?, prix = ?, quantite = ?, id_categorie = ? WHERE id = ?;"
        mod_cat = "UPDATE categorie SET nom = ? WHERE id = ?;"
        data = (nom, description, prix, quantite, id_categorie)
        cat = [categorie]
        self.cursor.execute(mod_item, data)
        self.connector.commit()
        self.cursor.execute(mod_cat, cat)
        self.connector.commit()
