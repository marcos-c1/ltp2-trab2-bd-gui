import asyncio
from tkinter import (CENTER, LEFT, RIGHT, TOP, YES, Button, Entry, Frame,
                     Label, PhotoImage, Tk, X, Y, messagebox, ttk)

import ttkbootstrap as tkbts

from config.db import Database
from controller.cliente import ClienteController
from controller.pedido import PedidoController
from gui.events.main import EventoWidget
from models.cliente import Cliente
from models.pedido import Pedido

window = Tk()
window.geometry('600x400')
window.title('CRUD do trab 2')
fieldsCliente = ('id', 'nome', 'isEmpresa', 'registro', 'cep', 'uf')
fieldsPedido = ('id', 'idCliente', 'produto', 'precoProduto', 'precoFrete')
db = Database()
cc = ClienteController()
pc = PedidoController()

def successMessage(message):
    messagebox.showinfo("Success", message)

def postPedido(entries):
    values = []

    for entry in entries:
        values.append(entry[1].get())

    p = Pedido(values[0], values[1], int(values[2]), int(values[3]))
    pc.criarPedido(p, db)
    successMessage("Cliente adicionado com sucesso")

def postCliente(entries):
    values = []
    for entry in entries:
        print(entry)
        values.append(entry[1].get())

    c1 = Cliente(values[0], True if values[1] == 1 else False, values[2], values[3], values[4])
    c.criarCliente(p=c1, db=db)
    #EventoWidget.criarDado(EventoWidget, entries[1].get(), values)
    successMessage("Cliente adicionado com sucesso")

def addForm(fields):
    entries = []
    for index, field in enumerate(fields):
        if index == 0:
            continue
        row = Frame()
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))

    return entries

def clearScreen():
    for widget in window.winfo_children():
        widget.destroy()

def goToHome():
    clearScreen()
    addAllHomeWidgets()

def pedidoForm(atualizar: bool):
    ents = addForm(fields=fieldsPedido)
    b1 = Button(window, text='Atualizar pedido' if atualizar else 'Criar pedido',
                command=(lambda e=ents: postPedido(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(window, text='Voltar', command=goToHome)
    b2.pack(side=LEFT, padx=5, pady=5)


def clientForm(atualizar: bool, valores):
    ents = addForm(fields=fieldsCliente)
    b1 = Button(window, text='Atualizar cliente' if atualizar else 'Criar cliente',
                  command=(lambda e=ents: postCliente(e) if atualizar else putCliente(e, valores)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(window, text='Voltar', command=goToHome)
    b2.pack(side=LEFT, padx=5, pady=5)

def addClienteScreen(atualizar: bool, valores):
    clearScreen()
    clientForm(atualizar, valores)

def addPedidoScreen(atualizar: bool):
    clearScreen()
    pedidoForm(atualizar, valores)

def editarSelection(tabelaCliente: ttk.Treeview, tabelaPedido: ttk.Treeview):
    selCliente = tabelaCliente.selection()[0] if len(tabelaCliente.selection()) > 0 else ""
    selPedido = tabelaPedido.selection()[0] if len(tabelaPedido.selection()) > 0 else ""


    if len(selCliente) > 0:
        idCliente = tabelaCliente.item(selCliente)['values'][0]
        cliente = cc.getCliente(int(idCliente), db)
        clearScreen()
        addClienteScreen(True, tabelaCliente.item(selCliente)['values'])
    elif len(selPedido):
        idPedido = tabelaPedido.item(selPedido)['values'][0]
        pedido = pc.getPedido(int(idPedido), db)
        clearScreen()
        addPedidoScreen(True, tabelaPedido.item(selCliente)['values'])

def removeSelection(tabelaCliente: ttk.Treeview, tabelaPedido: ttk.Treeview):
    for i in tabelaCliente.selection():
        cc.deletarCliente(tabelaCliente.item(i)['values'][0], db)
        tabelaCliente.delete(i)

    for i in tabelaPedido.selection():
        pc.deletarPedido(tabelaPedido.item(i)['values'][0], db)
        tabelaPedido.delete(i)

def addAllHomeWidgets():
    # Tabela de Cliente
    tabelaCliente = ttk.Treeview(window, columns = fieldsCliente, show = 'headings')

    tabelaCliente.heading("#0", text = 'Editar')

    for i, f in enumerate(fieldsCliente):
        tabelaCliente.column(f, anchor=CENTER)
        tabelaCliente.heading(f, text = f.capitalize())


    tabelaCliente.pack(fill = 'both', expand = True)

    # Tabela de Pedido
    tabelaPedido = ttk.Treeview(window, columns = fieldsPedido, show = 'headings')

    tabelaPedido.heading("#0", text = 'Editar')

    for i, f in enumerate(fieldsPedido):
        tabelaPedido.column(f, anchor=CENTER)
        tabelaPedido.heading(f, text = f.capitalize())



    tabelaPedido.pack(fill = 'both', expand = True)

    btnCliente = tkbts.Button(text = 'Adicionar cliente', command=lambda: addClienteScreen(False, None), bootstyle='primary')
    btnPedido = tkbts.Button(text = 'Adicionar pedido', command=lambda: addPedidoScreen(False, None), bootstyle='primary')
    btnRemover = tkbts.Button(text = 'Remover selecionado', command=lambda: removeSelection(tabelaCliente, tabelaPedido), bootstyle='danger')
    btnEditar = tkbts.Button(text = 'Editar um selecionado', command=lambda: editarSelection(tabelaCliente, tabelaPedido), bootstyle='secondary')

    EventoWidget.criarDado(EventoWidget, tabelaCliente, cc.listarClientes(db))
    EventoWidget.criarDado(EventoWidget, tabelaPedido, pc.listarPedidos(db))

    btnCliente.pack(side=LEFT, padx=5, pady=5)
    btnPedido.pack(side=LEFT, padx=5, pady=5)
    btnRemover.pack(side=LEFT, padx=5, pady=5)
    btnEditar.pack(side=LEFT, padx=5, pady=5)

def run():
    addAllHomeWidgets()
    window.mainloop()
