import sqlite3

class Database:
    def __init__(self):
       self.createTable()
       

    def connect(self):
        try:
            return sqlite3.connect("schema.db")
        except sqlite3.Error as e:
            print(f"{e}")

    def createTable(self):
        with self.connect() as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS clientes(ID INTEGER PRIMARY KEY, NOME TEXT NOT NULL, ISEMPRESA INTEGER DEFAULT 0, REGISTRO TEXT NOT NULL, UF TEXT NOT NULL)")
            conn.execute("CREATE TABLE IF NOT EXISTS pedidos(ID INTEGER PRIMARY KEY, PRODUTO TEXT NOT NULL, PRECOPRODUTO REAL NOT NULL, PRECOFRETE REAL NOT NULL)")
            conn.commit()