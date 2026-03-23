# Sistema de alimentos

from cadastro import carregar_dados, salvar_dados


def adicionar_alimento(user):
    print("═══════ Adicionar alimento ═══════")

    nome = input("Nome do alimento:\n> ")
    gramas = float(input("Quantidade (g):\n> "))
    caloria = float(input("Calorias:\n> "))

    proteina = float(input("Proteína:\n> "))
    carbo = float(input("Carboidrato:\n> "))
    gordura = float(input("Gordura:\n> "))

    alimento = {
        "nome": nome,
        "gramas": gramas,
        "caloria": caloria,
        "macronutrientes": {
            "proteina": proteina,
            "carbo": carbo,
            "gordura": gordura
        }
    }

    dados = carregar_dados()

    for u in dados["usuarios"]:
        if u["nome"] == user["nome"]:

            if "alimentos" not in u:
                u["alimentos"] = []

            u["alimentos"].append(alimento)

    salvar_dados(dados)

    print("Alimento adicionado!")


def listar_alimentos(user):
    print("═══════ Seus alimentos ═══════")

    # Pega os dados att do jsonzito, antes eu tava pegando por parâmetro, se n me engano, e tava
    # dando pau
    dados = carregar_dados()

    for u in dados["usuarios"]:
        if u["nome"] == user["nome"]:

            if "alimentos" not in u or not u["alimentos"]:
                print("Nenhum alimento cadastrado")
                return

            for alimento in u["alimentos"]:
                print(f"{alimento['nome']} - {alimento['caloria']} kcal")

            return