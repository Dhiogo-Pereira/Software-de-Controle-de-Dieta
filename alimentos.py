from cadastro import carregar_dados, salvar_dados
from classes import Alimento


def adicionar_alimento(user):
    print("═══════ Adicionar alimento ═══════")

    nome = input("Nome do alimento:\n> ")
    quantidade = float(input("Quantidade:\n> "))
    caloria = float(input("Calorias:\n> "))

    proteina = float(input("Proteína:\n> "))
    carbo = float(input("Carboidrato:\n> "))
    gordura = float(input("Gordura:\n> "))

    macros = {
        "proteina": proteina,
        "carbo": carbo,
        "gordura": gordura
    }

    alimento = Alimento(nome, quantidade, caloria, macros)

    dados = carregar_dados()

    for u in dados["usuarios"]:
        if u["nome"] == user["nome"]:

            if "alimentos" not in u:
                u["alimentos"] = []

            u["alimentos"].append(alimento.to_dict())

    salvar_dados(dados)

    print("Alimento adicionado!")

def listar_alimentos(user):
    print("═══════ Seus alimentos ═══════")

    dados = carregar_dados()

    for u in dados["usuarios"]:
        if u["nome"] == user["nome"]:

            if "alimentos" not in u or not u["alimentos"]:
                print("Nenhum alimento cadastrado")
                return

            for alimento in u["alimentos"]:
                print(f"{alimento['nome']} - {alimento['caloria']} kcal")

            return