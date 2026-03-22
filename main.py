# Interface principal

import cadastro
import login
import alimentos
import metabolismo
import relatorio


def menu():
    while True:
        print("\n═══════ Sistema ═══════")
        print("[1] Cadastrar")
        print("[2] Login")
        print("[3] Sair")

        op = input("> ")

        if op == "1":
            cadastro.cadastrar_user()

        elif op == "2":
            user = login.fazer_login()

            if user:
                menu_usuario(user)

        elif op == "3":
            break

        else:
            print("Opção inválida")


def menu_usuario(user):
    while True:
        print(f"\n═══════ Bem-vindo {user['nome']} ═══════")
        print("[1] Adicionar alimento")
        print("[2] Listar alimentos")
        print("[3] Ver metabolismo")
        print("[4] Ver relatório")
        print("[5] Logout")

        op = input("> ")

        if op == "1":
            alimentos.adicionar_alimento(user)

        elif op == "2":
            alimentos.listar_alimentos(user)

        elif op == "3":
            metabolismo.mostrar_metabolismo(user)

        elif op == "4":
            relatorio.mostrar_relatorio(user)

        elif op == "5":
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu()