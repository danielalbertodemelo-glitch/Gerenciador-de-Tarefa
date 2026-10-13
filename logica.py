estados = ["Pendente", "Feito", "Não Feito"]
estado_inicial = "Pendente"

def criar_tarefa(nome):
    tarefa = {
        "nome": nome,
        "estado": estado_inicial
    }
    return tarefa

def contar_por_estado(tarefas):
    contagem = {}
    for estado in estados:
        contagem[estado] = 0

    for tarefa in tarefas:
        contagem[tarefa["estado"]] += 1

    return contagem