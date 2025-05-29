from gui.widgets.main import *
from tkinter.ttk import Treeview

class EventoWidget:

    # mock data 
    nome = ['Rodrigo', 'Maria', 'Alex', 'Rafaela', 'Marcos', 'Henrique', 'Lisa', 'Ana', 'Carla']
    registro = ['428.651.170-73', '675.580.250-60', '675.580.250-60', '675.580.250-60', '675.580.250-60', '45.969.227/0001-88', '45.969.227/0001-88', '45.969.227/0001-88', '45.969.227/0001-88']
    cep = ['01001-000', '01001-000', '01001-000', '01001-000', '01001-000', '01001-000', '01001-000', '01001-000', '01001-000']
    uf = ['DF', 'MA', 'AP', 'AC', 'PA', 'MG', 'SP', 'RJ', 'PI']

    def clienteSelecao(this, tabela: Treeview):
        print(tabela.selection())
        for i in tabela.selection():
            print(tabela.item(i)['values'])
          
    def criarDado(this, tabela: Treeview):
        for i in range(9):
            nome = this.nome[i]
            isEmpresa = 0
            registro = this.registro[i]
            cep = this.cep[i]
            uf = this.uf[i]
            data = (nome, isEmpresa, registro, cep, uf)
            tabela.insert(parent = '', index = 0, values = data)

    def alterarDado(this, tabela: Treeview):
        print('altera dado na tabela e banco')

    def removerDado(this, tabela: Treeview):
        for i in tabela.selection():
            tabela.delete(i)

	

"""
tabelaCliente.bind('<<TreeviewSelect>>', item_select)
tabelaPedido.bind('<Delete>', delete_items)
tabelaPedido.bind('<Delete>', delete_items)

"""