import os
import time
from logica import criar_tarefa, contar_por_estado

tarefas = []
opcoes_menu = ["Adicionar tarefa", "Listar tarefas", "Sair"]

def mostrar_linha():
    print("=" * 40)

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pedir_opcao(mensagem, quantidade):
    while True:
        try:
            opcao = int(input(f"\n{mensagem} [1-{quantidade}]: "))
            if 1 <= opcao <= quantidade:
                return opcao
            print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Digite apenas números.")

def adicionar_tarefa():
    mostrar_linha()
    print("\tADICIONAR TAREFA")
    mostrar_linha()

    nome = input("\nNome da tarefa: ").strip()
    while nome == "":
        print("O nome da tarefa não pode ficar vazio.")
        nome = input("Nome da tarefa: ").strip()

    tarefa = criar_tarefa(nome)
    tarefas.append(tarefa)
    
    print("\nTarefa Adicionada com Sucesso!")

def listar_tarefas():
    mostrar_linha()
    print("\tLISTA DE TAREFAS")
    mostrar_linha()

    if not tarefas:
        print("Não há tarefas cadastradas.")
        mostrar_linha()
        return

    for tarefa in tarefas:
        print(f"{tarefa['nome']:<20}{tarefa['estado']}")
    mostrar_linha()

    contagem = contar_por_estado(tarefas)
    for estado, quantidade in contagem.items():
        print(f"{estado}: {quantidade}")
    mostrar_linha()

def menu():
    while True:
        limpar_tela()
        mostrar_linha()
        print("\tGERENCIADOR DE TAREFAS")
        mostrar_linha()

        for i, opcao_menu in enumerate(opcoes_menu, start=1):
            print(f"[{i}] - {opcao_menu}")

        opcao = pedir_opcao("Escolha uma opção", len(opcoes_menu))

        if opcao == 1:
            limpar_tela()
            adicionar_tarefa()
            input("Pressione ENTER para voltar...")
        elif opcao == 2:
            limpar_tela()
            listar_tarefas()
            input("\nPressione ENTER para voltar...")
        else:
            limpar_tela()
            break

menu()
print("Finalizando...")
time.sleep(1)
print("Volte sempre!")