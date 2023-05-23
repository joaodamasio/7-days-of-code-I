# Definindo a classe Pedido que tera as informações do cliente e pedido
class Pedido:
    def __init__(self, numero, nome, prato):
        self.numero = numero
        self.nome = nome
        self.prato = prato


# Criando outra classe para receber a FilaDePedidos alterar quando necesario
class FilaDePedidos:
    def __init__(self):
        self.filaPedidos = []

    # Método que adiciona o pedido ao final da fila
    def adicionar_pedido(self, numero, nome, prato):
        novo_pedido = Pedido(numero, nome, prato)
        self.filaPedidos.append(novo_pedido)

    # Método que remove e retorna o primero elemento da fila
    def remover_pedido(self):
        if len(self.filaPedidos) < 1:
            return None
        return self.filaPedidos.pop(0)

    # Método que mostra cada pedido dentro da lista de pedidos
    def mostrar_pedidos(self):
        if len(self.filaPedidos) < 1:
            print("Não há pedidos no momento")
            return
        for pedido in self.filaPedidos:
            print(f"Número: {pedido.numero}, Nome: {pedido.nome}, Prato: {pedido.prato}")

fila = FilaDePedidos()

fila.adicionar_pedido(1, "João", "Hambúrguer")
fila.adicionar_pedido(2, "Maria", "Pizza")
fila.adicionar_pedido(3, "José", "Sushi")

fila.mostrar_pedidos()