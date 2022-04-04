"""
To Do List :

Desenvolva uma To Do List (Lista de Tarefas) em Python utilizando, obrigatoriamente, listas encadeadas (livre escolha de qual delas será a mais adequada).

Como será essa aplicação?

- Deve contemplar todas principais atividades de um CRUD simples, isto é: Inserir, Deleter, Remover e Alterar - uma tarefa ou várias.

- Implementar um pequeno menu dando a opção de escolha ao usuário e, consequentemente, viabilizando maior interação com a aplicação.

- Além das operações básicas também podem implementar outras funcionalidades, como por exemplo, marcar uma tarefa como feita e manter ela destacada na listagem (ou não).

Dicas:

- Procure modularizar a sua aplicação o máximo que conseguir, mantendo coesão e coerência do início ao fim. Não esquecendo dos quatro pilares da Programação Orientada a Objetos

- Use a criatividade, destaquei pontos essenciais apenas.

"""



def menu():
    print('''O que você deseja fazer:
           0 -  Sair
           1 -	Inserir Tarefa
           2 -	Buscar Tarefa
           3 -  Mostrar Todas as Tarefas
           4 -	Alterar Tarefa
           5 -	Remover Tarefa
           Escolha: '''
          )
    print()
    print()
    return input()


class ElementoLista:
    def __init__(self, dado=0, proximo_elemento=None):
        self.dado = dado
        self.proximo = proximo_elemento

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class Lista:
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"


def insere_no_inicio(lista, nova_tarefa):
    novo_elemento = ElementoLista(nova_tarefa)
    novo_elemento.proximo = lista.cabeca
    lista.cabeca = novo_elemento


def insere_depois(lista, elemento_anterior, nova_tarefa):
    assert elemento_anterior, "Elemento anterior precisa existir na lista!"
    novo_elemento = ElementoLista(nova_tarefa)
    novo_elemento.proximo = elemento_anterior.proximo
    elemento_anterior.proximo = novo_elemento


def busca(lista, tarefa):
    inicial = lista.cabeca
    while inicial and inicial.dado != tarefa:
        inicial = inicial.proximo
    return inicial


def alterar(lista, valor):
    tarefa = busca(lista, valor)
    if tarefa is None:
        print("Tarefa nao localizada!")
    else:
        nova_tarefa = input("Qual a atualizacao você gostaria de fazer? Digite a tarefa: ").upper()
        tarefa.dado = nova_tarefa
        print(lista)
        print("Tarefa atualizada com sucesso!")


def remove(self, valor):
    assert self.cabeca, "Lista vazia! Nao e possivel remover valor!!!"

    if self.cabeca.dado == valor:
        self.cabeca = self.cabeca.proximo
    else:
        anterior = None
        atual = self.cabeca
        while atual and atual.dado != valor:
            anterior = atual
            atual = atual.proximo
        if atual:
            anterior.proximo = atual.proximo
        else:
            anterior.proximo = None




lista = Lista()


while True:

    resposta = menu()

    if resposta == "0":
        break


    elif resposta == "1":

        nova_tarefa = input("Digite o nome da tarefa que deseja inserir: ").upper()
        if lista.cabeca is None:
            insere_no_inicio(lista, nova_tarefa)
            nodo_anterior = lista.cabeca
        else:
            insere_depois(lista, nodo_anterior, nova_tarefa)
        print("Tarefa cadastrada com sucesso!")


    elif resposta == "2":
        tarefa = input("Qual tarefa gostaria de localizar? ").upper()
        resposta = busca(lista, tarefa)
        if resposta is None:
            print("Tarefa nao localizada!")
        else:
            print("Tarefa localizada!")


    elif resposta == "3":
        print("As tarefas cadastradas são: ", lista)


    elif resposta == "4":
        print(lista)
        tarefa = input("Qual tarefa gostaria de alterar? ").upper()
        alterar(lista, tarefa)


    elif resposta == "5":
        print(lista)
        tarefa_remover = input("Qual tarefa gostaria de remover? ").upper()
        remove(lista, tarefa_remover)
        print(lista)
        print("Tarefa removida com sucesso!")


    else:
        print("Erro. Favor digitar apenas alguma das opcoes do menu!")


