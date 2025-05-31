from tkinter import PhotoImage
from tkinter.ttk import Treeview

from controller.cliente import ClienteController
from controller.pedido import PedidoController
from gui.widgets.main import *


class EventoWidget:

    # mock data
    nome = ['Rodrigo', 'Maria', 'Alex', 'Rafaela', 'Marcos', 'Henrique', 'Lisa', 'Ana', 'Carla']
    registro = ['428.651.170-73', '675.580.250-60', '675.580.250-60', '675.580.250-60', '675.580.250-60', '45.969.227/0001-88', '45.969.227/0001-88', '45.969.227/0001-88', '45.969.227/0001-88']
    cep = ['01001-000', '01001-000', '01001-000', '01001-000', '01001-000', '01001-000', '01001-000', '01001-000', '01001-000']
    uf = ['DF', 'MA', 'AP', 'AC', 'PA', 'MG', 'SP', 'RJ', 'PI']

    def clienteSelecao(self, tabela: Treeview):
        print(tabela.selection())
        for i in tabela.selection():
            print(tabela.item(i)['values'])

    def criarDado(self, tabela: Treeview, data: list):
        editImg = PhotoImage(file="search.png")
        if len(data) > 0:
            for d in data:
                tabela.insert('', "end", image=editImg, values = d)

    def alterarDado(self, tabela: Treeview):
        print('altera dado na tabela e banco')

    def removerDado(self, tabela: Treeview):
        for i in tabela.selection():
            print(tabela.item(i)['values'][0])
            tabela.delete(i)



"""
tabelaCliente.bind('<<TreeviewSelect>>', item_select)
tabelaPedido.bind('<Delete>', delete_items)
tabelaPedido.bind('<Delete>', delete_items)

"""
