# Sistema de relatórios

from cadastro import carregar_dados
from classes import User


def mostrar_relatorio(user):
    print("═══════ Relatório Diário ═══════")

    dados = carregar_dados()

    for u in dados["usuarios"]:
        if u["nome"] == user["nome"]:

            if "alimentos" not in u or not u["alimentos"]:
                print("Nenhum alimento registrado hoje")
                return

            # Soma calorias
            total_calorias = sum(a["caloria"] for a in u["alimentos"])

            usuario = User(
                u["nome"], u["senha"], u["idade"], u["peso"],
                u["altura"], u["objetivo"], u["sexo"], u["atividade"]
            )

            tmb = usuario.calcular_tmb()
            get = usuario.calcular_get()
            meta = usuario.calcular_meta_calorica()

            print(f"TMB: {tmb:.2f} kcal")
            print(f"GET: {get:.2f} kcal")
            print(f"Meta calórica: {meta:.2f} kcal")
            print(f"Consumido hoje: {total_calorias:.2f} kcal")

            diferenca = total_calorias - meta

            print("\n═══════ Análise ═══════")

            if diferenca > 0:
                print(f"Superávit de {diferenca:.2f} kcal")
            elif diferenca < 0:
                print(f"Déficit de {abs(diferenca):.2f} kcal")
            else:
                print("Você atingiu exatamente sua meta!")

            return