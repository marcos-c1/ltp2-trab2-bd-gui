import sqlite3

from config.db import Database
from models.cliente import Cliente


class ClienteController:

    def criarCliente(self, p: Cliente, db: Database):
        try:
            with db.connect() as connection:
                c = connection.cursor()
                c.execute("INSERT INTO clientes(nome, isEmpresa, registro, cep, uf) VALUES(?, ?, ?, ?, ?)", (p.nome, 1 if p.isEmpresa else 0, p.registro, p.cep, p.uf))
        except sqlite3.IntegrityError as e:
                print("Não é possível inserir outro cliente do mesmo id!")
        except sqlite3.InternalError as e:
                print(f"Algum erro interno no banco ocorreu: {e}")

    def listarClientes(self, db: Database) -> tuple:
        clientes = []

        try:
            with db.connect() as connection:
                c = connection.cursor()
                clientes = c.execute("SELECT * FROM clientes").fetchall()
                print(clientes)
        except sqlite3.Error as e:
                print(f"Erro a nivel de banco: {e}")

        return clientes

    def getCliente(self, id: int, db: Database) -> tuple:
        cliente = []

        try:
            with db.connect() as connection:
                c = connection.cursor()
                cliente = c.execute("SELECT ID FROM clientes WHERE id = ?", str(id)).fetchone()
                print(pedido)
        except sqlite3.Error as e:
                print(f"Erro a nivel de banco: {e}")

        return cliente


    def atualizarCliente(self, p: Cliente,  db: Database):
        try:
            with db.connect() as connection:
                c = connection.cursor()
                cliente = c.execute("SELECT ID FROM clientes WHERE id = ?", str(p.getId())).fetchone()
                if cliente == None:
                     print("ID inexistente")
                else:
                    c.execute("UPDATE clientes SET nome = ?, isEmpresa = ?, registro = ?, cep = ?, uf = ? WHERE id = ?", (p.nome, 1 if p.isEmpresa else 0, p.registro, p.cep, p.uf))
        except sqlite3.Error as e:
            print(f"Erro a nivel de banco: {e}")

    def deletarCliente(self, id: int, db: Database):
        try:
            with db.connect() as connection:
                c = connection.cursor()
                cliente = c.execute("SELECT ID FROM clientes WHERE id = ?", str(id)).fetchone()
                if cliente == None:
                     print("ID inexistente")
                else:
                    c.execute("DELETE FROM clientes WHERE id = ?", str(id))
        except sqlite3.Error as e:
            print(f"Erro a nivel de banco: {e}")
