import json
import os
import tempfile

ficheiro_tarefas = "tarefas.json"
estados = ["Pendente", "Feito", "Não Feito"]
estado_inicial = "Pendente"

def criar_tarefa(nome):
    tarefa = {
        "nome": nome,
        "estado": estado_inicial
    }
    return tarefa

def atualizar_estado(tarefas, indice_tarefa, novo_estado):
    tarefas[indice_tarefa]["estado"] = novo_estado

def contar_por_estado(tarefas):
    contagem = {}
    for estado in estados:
        contagem[estado] = 0

    for tarefa in tarefas:
        contagem[tarefa["estado"]] += 1

    return contagem

def guardar_tarefas(tarefas):
    pasta = os.path.dirname(os.path.abspath(ficheiro_tarefas))
    caminho_temporario = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=pasta,
            delete=False
        ) as ficheiro:
            caminho_temporario = ficheiro.name
            json.dump(tarefas, ficheiro, ensure_ascii=False, indent=4)

        os.replace(caminho_temporario, ficheiro_tarefas)
    finally:
        if caminho_temporario and os.path.exists(caminho_temporario):
            os.remove(caminho_temporario)

def carregar_tarefas():
    try:
        with open(ficheiro_tarefas, "r", encoding="utf-8") as ficheiro:
            return json.load(ficheiro)
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, UnicodeDecodeError) as erro:
        raise ValueError(
            f"O ficheiro '{ficheiro_tarefas}' está vazio, contém JSON inválido "
            "ou não está codificado corretamente. "
            "O ficheiro foi preservado; corrija-o ou recupere uma cópia de segurança."
        ) from erro