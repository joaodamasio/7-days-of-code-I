# Criando estrutura de nó para armazenar informações: 
class Paciente:
    def __init__(self, id, nome, estado_saude):
        self.id = id
        self.nome = nome
        self.estado_saude = estado_saude
        self.proximo_paciente = None

# Criando a classe ListaDePacientes para representar a lista simplesmente encadeada
class ListaDePacientes:
    def __init__(self):
        self.head = None
        self.tail = None

    def adicionar_paciente(self, id, nome, estado_saude):
        novo_paciente = Paciente(id,nome,estado_saude)
        if self.head is None:
            # Se a lista estiver vazia, o novo paciente é adicionado como cabeça
            self.head = novo_paciente
            self.tail = novo_paciente

        else:
            # Caso contrario, o paciente é adiconado ao final da lista
            self.tail.proximo_paciente = novo_paciente
            self.tail = novo_paciente

    #Definindo métodos para remover um paciente
    def remover_paciente(self,id):
        if self.head is None:
            # Se a lista estiver vazia, não ha o que remover
            return
        elif self.head.id == id:
            # Se o paciente a ser removido for a cabeça da lista, basta atualizar o ponteiro para o próximo paciente
            self.head = self.head.proximo_paciente

            # Se a lista tiver ficado vazia, atualiza tambem a cauda
            if self.head is None:
                self.tail = None
            return
        # Caso contrário ira percorrer a lista até encontrar o paciente a ser removido
        else:
            paciente_atual = self.head
            while paciente_atual.proximo_paciente is not None:
                if paciente_atual.proximo_paciente.id == id:
                    paciente_atual.proximo_paciente = paciente_atual.proximo_paciente.proximo_paciente
                    if paciente_atual.proximo_paciente is None:
                        self.tail = paciente_atual
                        return
                paciente_atual = paciente_atual.proximo_paciente

    #Método para imprimir todos os pacientes da lista
    def listar_pacientes(self):
        if self.head is None:
            print('Não há pacientes na lista.')
        else:
            paciente_atual = self.head
            while paciente_atual is not None:
                print(f"Nome: {paciente_atual.nome}, ID: {paciente_atual.id}, Estado de saúde: {paciente_atual.estado_saude}")
                paciente_atual = paciente_atual.proximo_paciente

listaDePacientes = ListaDePacientes()

listaDePacientes.adicionar_paciente(1, "Giovanna", "Estável")
listaDePacientes.adicionar_paciente(2, "Lucas", "Tratamento intensivo")
listaDePacientes.adicionar_paciente(3, "Alex", "Crítico")
listaDePacientes.adicionar_paciente(4, "Beatriz", "Estável")

listaDePacientes.listar_pacientes()

listaDePacientes.remover_paciente(3)

listaDePacientes.listar_pacientes()