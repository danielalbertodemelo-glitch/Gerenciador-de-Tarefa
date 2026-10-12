import os
import time

tarefas = []
estados = ["Feito", "Pendente", "Não Feito"]

def mostrar_linha():
    print("=" * 40)

def adicionar_tarefa():
    mostrar_linha()
    print("\tADICIONAR TAREFA")
    mostrar_linha()

    nome = input("\nNome da tarefa: ").strip()
    while nome == "":
        print("O nome da tarefa não pode ficar vazio.")
        nome = input("Nome da tarefa: ").strip()

    print("\nEscolha o estado:")
    for i, estado in enumerate(estados, start=1):
        print(f"{i} - {estado}")

    while True:
        try:
            opcao_estado = int(input("Digite a opção do estado [1-3]: "))
            if 1 <= opcao_estado <= 3:
                break
            print("Opção inválida. Tente de novo.")
        except ValueError:
            print("Digite apenas números.")

    tarefa = {
        "nome": nome,
        "estado": estados[opcao_estado - 1]
    }
    print ("\nTarefa Adicionada com Sucesso!")
    tarefas.append(tarefa)

def listar_tarefas():
    mostrar_linha()
    print("\tLISTA DE TAREFAS")
    mostrar_linha()

    if not tarefas:
        print("Não há tarefas cadastradas.")
        mostrar_linha()
        return

    print(f"{'NOME':<20}{'ESTADO'}")
    mostrar_linha()

    for tarefa in tarefas:
        print(f"{tarefa['nome']:<20}{tarefa['estado']}")

    mostrar_linha()

while True:
    os.system("cls")
    mostrar_linha()
    print("\tGERENCIADOR DE TAREFAS")
    mostrar_linha()

    print("\n[1] - Adicionar tarefa")
    print("[2] - Listar tarefas")
    print("[3] - Sair")

    while True:
        try:
            opcao = int(input("\nEscolha uma opção [1-3]: "))
            if 1 <= opcao <= 3:
                break
            print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Digite apenas números.")

    if opcao == 1:
        os.system ("cls")
        adicionar_tarefa()
        input("Pressione ENTER para voltar...")
    elif opcao == 2:
        os.system ("cls")
        listar_tarefas()
        input("\nPressione ENTER para voltar...")
    else:
        break

print("Finalizando...")
time.sleep(1)
print("Volte sempre!")