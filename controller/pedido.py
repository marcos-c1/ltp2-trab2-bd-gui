import sqlite3
from config.db import Database
from models.pedido import Pedido

class PedidoController():
    
    def criarPedido(self, p: Pedido, db: Database):
        try:
            with db.connect() as connection:
                c = connection.cursor()
                c.execute("INSERT INTO pedidos(idCliente, produto, precoProduto, precoFrete) VALUES(?, ?, ?, ?)", (p.idCliente, p.produto, p.precoProduto, p.precoFrete))
        except sqlite3.IntegrityError as e:
                print("Não é possível inserir outro pedido do mesmo id!")
        except sqlite3.InternalError as e:
                print(f"Algum erro interno no banco ocorreu: {e}")
    
    def listarPedidos(self, db: Database) -> list[any]:
        pedidos = []
        
        try:
            with db.connect() as connection:
                c = connection.cursor()
                pedidos = c.execute("SELECT * FROM pedidos").fetchall()
                print(pedidos)
        except sqlite3.Error as e:
                print(f"Erro a nivel de banco: {e}")

        return pedidos
    
    def atualizarPedido(self, p: Pedido,  db: Database):
        try:
            with db.connect() as connection:
                c = connection.cursor()
                pedido = c.execute("SELECT ID FROM pedidos WHERE id = ?", str(p.getId())).fetchone()
                if pedido == None:
                     print("ID inexistente")
                else: 
                    c.execute("UPDATE pedidos SET produto = ?, precoProduto = ?, precoFrete = ? WHERE id = ?", (p.produto, p.precoProduto, p.precoFrete))
        except sqlite3.Error as e:
            print(f"Erro a nivel de banco: {e}")
    
    def deletarPedido(self, id: str, db: Database):
        try:
            with db.connect() as connection:
                c = connection.cursor()
                pedido = c.execute("SELECT ID FROM pedidos WHERE id = ?", id).fetchone()
                if pedido == None:
                     print("ID inexistente")
                else:
                    c.execute("DELETE FROM pedidos WHERE id = ?", id)
        except sqlite3.Error as e:
            print(f"Erro a nivel de banco: {e}")