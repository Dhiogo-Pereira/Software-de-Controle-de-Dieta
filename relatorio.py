from cadastro import carregar_dados
from classes import Alimento, Cardapio, User


def mostrar_relatorio(user):
    print("═══════ Relatório Diário ═══════")

    dados = carregar_dados()

    for u in dados["usuarios"]:
        if u["nome"] == user["nome"]:

            if "alimentos" not in u or not u["alimentos"]:
                print("Nenhum alimento registrado")
                return

            cardapio = Cardapio()

            for a in u["alimentos"]:
                alimento = Alimento(
                    a["nome"], a["quantidade"], a["caloria"], a["macronutrientes"]
                )
                cardapio.adicionar_alimento(alimento)

            total = cardapio.calcular_total_calorias()

            usuario = User(
                u["nome"], u["senha"], u["idade"], u["peso"],
                u["altura"], u["objetivo"], u["sexo"], u["atividade"],
                u.get("meta_calorica")
            )

            meta = usuario.calcular_meta_calorica()

            print(f"Consumido: {total:.2f} kcal")
            
            if u["objetivo"] == 2:
                print("Objetivo: Manutenção (meta automática)")
            else:
                print(f"Meta: {meta:.2f} kcal")

            if total > meta:
                print("Superávit calórico")
            elif total < meta:
                print("Déficit calórico")
            else:
                print("Parabéns você atingiu exatamente a sua meta!")

            return