from tkinter import ttk, Tk, Frame, Button, Label, Entry, TOP, RIGHT, CENTER, LEFT, X, Y, YES
import ttkbootstrap as tkbts
from gui.events.main import EventoWidget
from controller.cliente import ClienteController
from models.cliente import Cliente
from models.pedido import Pedido
from controller.pedido import PedidoController
from config.db import Database
import asyncio


window = Tk()
window.geometry('600x400')
window.title('CRUD do trab 2')
fieldsCliente = ('nome', 'isEmpresa', 'registro', 'cep', 'uf')
fieldsPedido = ('nomeCliente', 'produto', 'precoProduto', 'precoFrete')
db = Database()

def postCliente(entries):
    c = ClienteController
    values = []
    for entry in entries: 
        values.append(entry[1].get())

    c1 = Cliente(values[0], values[1], values[2],values[3], values[4])
    c.criarCliente(c1, db)

def addForm(fields):
    entries = []
    for field in fields:
        row = Frame()
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))

        
    return entries

async def clearScreen():
    for widget in await window.winfo_children():
        widget.destroy()

def goToHome():
    clearScreen()
    addAllHomeWidgets()
    
def test():
    ents = addForm(fields=fieldsCliente)
    b1 = Button(window, text='Criar cliente',
                  command=(lambda e=ents: postCliente(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(window, text='Voltar', command=goToHome())
    b2.pack(side=LEFT, padx=5, pady=5)

def addClienteScreen():
    asyncio.run(clearScreen())
    print('add buttons')
    test()
    


def addPedidoScreen():
    yield clearScreen()
    ents = addForm(fields=fieldsPedido)

    b1 = Button(window, text='Criar pedido',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(window, text='Voltar', command=goToHome())
    b2.pack(side=LEFT, padx=5, pady=5)


def addAllHomeWidgets():
    # Tabela de Cliente 
    tabelaCliente = ttk.Treeview(window, columns = fieldsCliente, show = 'headings')
    
    tabelaCliente.column('nome', anchor=CENTER)
    tabelaCliente.column('registro', anchor=CENTER)
    tabelaCliente.column('cep', anchor=CENTER)
    tabelaCliente.column('uf', anchor=CENTER)


    tabelaCliente.heading('nome', text = 'Nome')
    tabelaCliente.heading('registro', text = 'Registro')
    tabelaCliente.heading('cep', text = 'CEP')
    tabelaCliente.heading('uf', text = 'UF')
    tabelaCliente.pack(fill = 'both', expand = True)

    # Tabela de Pedido
    tabelaPedido = ttk.Treeview(window, columns = fieldsPedido, show = 'headings')
    
    tabelaPedido.column('nomeCliente', anchor=CENTER)
    tabelaPedido.column('produto', anchor=CENTER)
    tabelaPedido.column('precoProduto', anchor=CENTER)
    tabelaPedido.column('precoFrete', anchor=CENTER)

    tabelaPedido.heading('nomeCliente', text = 'Nome do cliente')
    tabelaPedido.heading('produto', text = 'Produto')
    tabelaPedido.heading('precoProduto', text = 'Preço do produto')
    tabelaPedido.heading('precoFrete', text = 'Preço do frete')
    tabelaPedido.pack(fill = 'both', expand = True)

    btnCliente = tkbts.Button(text = 'Adicionar cliente', command=addClienteScreen, bootstyle='danger')
    btnPedido = tkbts.Button(text = 'Adicionar pedido', command=addPedidoScreen, bootstyle='primary')
    
    EventoWidget.criarDado(EventoWidget, tabelaCliente)

    print()
    btnCliente.pack(side=LEFT, padx=5, pady=5)
    btnPedido.pack(side=LEFT, padx=5, pady=5)

def run():
    addAllHomeWidgets()
    window.mainloop()