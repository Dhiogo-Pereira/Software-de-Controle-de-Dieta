# Sistema de login

from cadastro import carregar_dados


def fazer_login():
    print("═══════ Login ═══════")

    nome = input("Nome:\n> ")
    senha = input("Senha:\n> ")

    dados = carregar_dados()

    for user in dados["usuarios"]:
        if user["nome"] == nome and user["senha"] == senha:
            print("Login realizado com sucesso!")
            return user

    print("Nome ou senha incorretos")
    return None