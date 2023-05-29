# Definindo a  classe que vai receber os atributos

class Livro:
    def __init__(self, nome, numeroDePaginas):
        self.nome =  nome
        self.numeroDePaginas = numeroDePaginas

# Definindo a classe que vai ter os métodos

class PilhaDeLivros:
    def __init__(self):
        self.pilhaLivros = []

    # Adiciona no final da pilha
    def  adicionar_livro(self, nome, numeroDePaginas):
        novo_livro = Livro(nome,numeroDePaginas)
        self.pilhaLivros.append(novo_livro)

    # Remove o último elemento adicionado na pilha
    def remover_livro(self):
        if len(self.pilhaLivros) < 1:
            return None
        return self.pilhaLivros.pop()

    def mostrar_livro_topo(self):
        ultimo_index = len(self.pilhaLivros) - 1
        print(f"O livro que está no topo é {self.pilhaLivros[ultimo_index]}")
        return  self.pilhaLivros[ultimo_index]

    def mostrar_livros(self):
        if len(self.pilhaLivros) < 1:
            print("Não há livros na pilha no momento")
            return
        for livro in self.pilhaLivros:
            print(f"Nome: {livro.nome}, número de páginas: {livro.numeroDePaginas}")
