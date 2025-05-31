import sqlite3


class Database:
    def __init__(self):
       self.createTable()


    def connect(self):
        try:
            return sqlite3.connect("schema.db")
        except sqlite3.Error as e:
            print(f"{e}")

    def dropTables(self):
        with self.connect() as conn:
            conn.execute("DROP TABLE clientes")
            conn.execute("DROP TABLE pedidos")

    def createTable(self):
        with self.connect() as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS clientes(ID INTEGER PRIMARY KEY, NOME TEXT NOT NULL, ISEMPRESA INTEGER DEFAULT 0, REGISTRO TEXT NOT NULL, CEP TEXT NOT NULL, UF TEXT NOT NULL)")
            print('Table clientes criada')
            conn.execute("CREATE TABLE IF NOT EXISTS pedidos(ID INTEGER PRIMARY KEY, IDCLIENTE INTEGER NOT NULL, PRODUTO TEXT NOT NULL, PRECOPRODUTO REAL NOT NULL, PRECOFRETE REAL NOT NULL, FOREIGN KEY(IDCLIENTE) REFERENCES clientes(ID))")
            print('Table pedidos criada')
            conn.commit()
