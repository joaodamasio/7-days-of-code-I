#criar uma classe chamada ListaDeCompras
class ListaDeCompras:
#criar duas listas vazias: itens e quantidades
    def __init__(self,itens,quantidades):
        self.itens=itens
        self.quantidades=quantidades
#criar um metodo adicionar item que recebe como argumento o nome do produto e a quantidade desejada
#dentro do metodo adicionar o nome do produto á lista itens e a quantidade a lista quantidades
    def adicionar_item(self,produto,quantidade_desejada):
        self.itens.append(produto)
        self.quantidades.append(quantidade_desejada)
        return print(f'{quantidade_desejada} {produto}(s) foram adicionados a sua lista')

#criar um metodo remover item que recebe como agumento o nome do produto a ser removido
#dentro do metodo encontrar o indice do produto na lista de items e remova o produto tanto da lista itens quanto da lista quantidades
    def remover_item(self,produto):
        for i in self.itens:
            if i == produto:
                self.itens.remove(i)
        print(f'|{produto} foi removido da sua lista de compras.|')

#criar o metodo listar itens que percorre a lista itens e a lista quantidades simultaneamente e exibe o nome do produto e a quantidade em um formato legivel
    def listar_itens(self):
        print('Lista de compras:')
        print('_'*20)
        for i,j in zip(self.quantidades,self.itens):
            print(i,j)
        print('_'*20)
#testar a implementação criando uma instancia da classe Lista de compras adicionando e removendo itens

compra = ListaDeCompras(['Arroz','Feijão'],[1,2])
compra.adicionar_item('Pão',4)
compra.listar_itens()