import sqlite3
from config.db import Database
from models.cliente import Cliente

class ClienteController():
    
    def criarCliente(self, p: Cliente, db: Database):
        try:
            with db.connect() as connection:
                c = connection.cursor()
                c.execute("INSERT INTO clientes(nome, isEmpresa, registro, cep, uf) VALUES(?, ?, ?, ?, ?)", (p.nome, p.isEmpresa, p.registro, p.cep, p.uf))
        except sqlite3.IntegrityError as e:
                print("Não é possível inserir outro cliente do mesmo id!")
        except sqlite3.InternalError as e:
                print(f"Algum erro interno no banco ocorreu: {e}")
    
    def listarClientes(self, db: Database) -> list[any]:
        clientes = []
        
        try:
            with db.connect() as connection:
                c = connection.cursor()
                clientes = c.execute("SELECT * FROM clientes").fetchall()
                print(clientes)
        except sqlite3.Error as e:
                print(f"Erro a nivel de banco: {e}")

        return clientes
    
    def atualizarCliente(self, p: Cliente,  db: Database):
        try:
            with db.connect() as connection:
                c = connection.cursor()
                cliente = c.execute("SELECT ID FROM clientes WHERE id = ?", str(p.getId())).fetchone()
                if cliente == None:
                     print("ID inexistente")
                else: 
                    c.execute("UPDATE clientes SET nome = ?, isEmpresa = ?, registro = ?, cep = ?, uf = ? WHERE id = ?", (p.nome, p.isEmpresa, p.registro, p.cep, p.uf))
        except sqlite3.Error as e:
            print(f"Erro a nivel de banco: {e}")
    
    def deletarCliente(self, id: str, db: Database):
        try:
            with db.connect() as connection:
                c = connection.cursor()
                cliente = c.execute("SELECT ID FROM clientes WHERE id = ?", id).fetchone()
                if cliente == None:
                     print("ID inexistente")
                else:
                    c.execute("DELETE FROM clientes WHERE id = ?", id)
        except sqlite3.Error as e:
            print(f"Erro a nivel de banco: {e}")