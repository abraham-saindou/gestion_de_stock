import mysql.connector

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Database:
    def __init__(self):
        self.connector = mysql.connector.connect(host='localhost', database='LaPlateforme', user='abraham', password='abraham')

    def connection(self):
        if self.connector.is_connected():
            cursor = self.connector.cursor()

    def gui(self):
        pass
