import datetime 

class Pedido():
    def __init__(self, idCliente: int, produto: str, precoProduto: float, precoFrete: float):
        self.dataPedido = datetime.datetime.now()
        if(idCliente is None):
            raise Exception("Pedido não relacionado com cliente")
        if(len(produto) == 0):
            raise Exception("Deve existir um produto")
        if(precoProduto <= 0):
            raise Exception("Preço do produto não pode ser menor ou igual a 0")
        if(precoFrete <= 0):
            raise Exception("Preço do frete não pode ser menor ou igual a 0")
        self.idCliente = idCliente
        self.produto = produto
        self.precoProduto = precoProduto
        self.precoFrete = precoFrete