# Sistema de cálculo metabólico

from cadastro import carregar_dados
from classes import User


def mostrar_metabolismo(user):
    print("═══════ Metabolismo ═══════")

    dados = carregar_dados()

    for u in dados["usuarios"]:
        if u["nome"] == user["nome"]:

            usuario = User(
                u["nome"], u["senha"], u["idade"], u["peso"],
                u["altura"], u["objetivo"], u["sexo"], u["atividade"],
                u.get("meta_calorica")
            )

            tmb = usuario.calcular_tmb()
            get = usuario.calcular_get()
            meta = usuario.calcular_meta_calorica()

            print(f"TMB: {tmb:.2f} kcal")
            print(f"GET: {get:.2f} kcal")
            print(f"Meta calórica: {meta:.2f} kcal")

            return