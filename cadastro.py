# Cadastro de usuários

import json
import classes


def cadastrar_user():
    """
    Cadastra um usuário e garante que a conta possua um nome único.
    """
    print("═══════ Cadastro de usuário ═══════")

    nome = input("Digite seu nome:\n> ")

    # Verifica se já existe uma conta com o msm nome
    if verifica_cadastro(nome):
        print("Já possui cadastro")
        return

    senha = input("Digite sua senha:\n> ")

    # Idade
    while True:
        try:
            idade = int(input("Digite sua idade:\n> "))
            if idade <= 0:
                print("Idade inválida")
                continue # Skipa o restante do código, e vai pra próxima iteração do loop
            break # Só vai cair no break se o input for um número válido maior que 0
        except ValueError:
            print("Digite um número válido")

    # Peso
    while True:
        try:
            peso = float(input("Digite seu peso:\n> "))
            if peso <= 0:
                print("Peso inválido")
                continue
            break
        except ValueError:
            print("Digite um número válido")

    # Altura
    while True:
        try:
            altura = float(input("Digite sua altura (em metros):\n> "))
            if altura <= 0:
                print("Altura inválida")
                continue
            break
        except ValueError:
            print("Digite um número válido")

    # Sexo
    sexo = input("Sexo (M/F): ").upper()
    while sexo not in ["M", "F"]: # Garantia pro user burrinho fzr oq eu quero
        sexo = input("Digite M ou F: ").upper()

    # Atividade
    print("\nNível de atividade:")
    print("[1] Sedentário")
    print("[2] Leve")
    print("[3] Moderado")
    print("[4] Intenso")
    print("[5] Muito intenso")

    atividade_op = input("> ")
    # Números tirados do gemini, não entendo de nutrição
    fatores = {
        "1": 1.2,
        "2": 1.375,
        "3": 1.55,
        "4": 1.725,
        "5": 1.9
    }

    while atividade_op not in fatores:
        atividade_op = input("Digite de 1 a 5: ")

    atividade = fatores[atividade_op]

    # Objetivo
    print("\nObjetivo:")
    print("[1] Perda de peso\n[2] Manutenção\n[3] Ganho de massa")

    objetivo = input("> ")
    while objetivo not in ["1", "2", "3"]:
        objetivo = input("Digite 1, 2 ou 3: ")

    objetivo = int(objetivo)


    # Criar usuário
    user = classes.User(
        nome, senha, idade, peso, altura, objetivo, sexo, atividade
    )

    dados = carregar_dados()

    dados["usuarios"].append(user.to_dict())

    salvar_dados(dados)

    print("Usuário cadastrado com sucesso!")


def verifica_cadastro(nome):
    """
    Verifica se já possui uma conta com esse nome.
    """
    dados = carregar_dados()

    for user in dados["usuarios"]:
        if nome == user["nome"]:
            return True

    return False


def carregar_dados():
    """
    Carrega os dados do JSON garantindo estrutura consistente.
    """
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            # Corrige usuários antigos
            for u in dados["usuarios"]:
                if "alimentos" not in u:
                    u["alimentos"] = []

            return dados

    except FileNotFoundError:
        return {"usuarios": []}


def salvar_dados(dados):
    """
    Salva os dados no JSON com suporte a UTF-8.
    """
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)