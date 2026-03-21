# Sistema de cálculo metabólico

from cadastro import carregar_dados


def mostrar_metabolismo(user):
    print("═══════ Metabolismo ═══════")

    dados = carregar_dados()

    for u in dados["usuarios"]:
        if u["nome"] == user["nome"]:

            # Recria objeto
            from classes import User

            usuario = User(
                u["nome"], u["senha"], u["idade"], u["peso"],
                u["altura"], u["objetivo"], u["sexo"], u["atividade"]
            )

            tmb = usuario.calcular_tmb()
            get = usuario.calcular_get()

            print(f"TMB: {tmb:.2f} kcal")
            print(f"GET: {get:.2f} kcal")

            return