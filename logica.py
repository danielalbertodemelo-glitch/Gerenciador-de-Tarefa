import json
import os
import tempfile

ficheiro_tarefas = "tarefas.json"
estados = ["Pendente", "Feito", "Não Feito"]
estado_inicial = "Pendente"
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

def criar_tarefa(nome, dia, permanente):
    tarefa = {
        "nome": nome,
        "estado": estado_inicial,
        "dia": dia,
        "permanente": permanente
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

def filtrar_tarefas_por_dia(tarefas, dia):
    return [tarefa for tarefa in tarefas if tarefa.get("dia") == dia]

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
            tarefas = json.load(ficheiro)
            for tarefa in tarefas:
                tarefa.setdefault("dia", None)
                tarefa.setdefault("permanente", False)
            return tarefas
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, UnicodeDecodeError) as erro:
        raise ValueError(
            f"O ficheiro '{ficheiro_tarefas}' está vazio, contém JSON inválido "
            "ou não está codificado corretamente. "
            "O ficheiro foi preservado; corrija-o ou recupere uma cópia de segurança."
        ) from erro