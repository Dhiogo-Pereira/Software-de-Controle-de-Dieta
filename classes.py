# Classes legais

class User:
    # Construtor
    def __init__(self, nome, senha, idade, peso, altura, objetivo, sexo, atividade):
        self.__nome = nome
        self.__senha = senha
        self.__idade = int(idade)
        self.__peso = float(peso)
        self.__altura = float(altura)
        self.__objetivo = int(objetivo)
        # Os dois abaixo são "extras" importantes para o cálculo correto do GET e TMB
        self.__sexo = sexo
        self.__atividade = float(atividade)
        self.__alimentos = []

    # Getters
    def get_nome(self):
        return self.__nome

    # Cálculo de Metabolismo Basal (TMB)
    # Fórmula de Mifflin-St Jeor
    # https://reference.medscape.com/calculator/846/mifflin-st-jeor-equation
    def calcular_tmb(self):
        altura_cm = self.__altura * 100

        if self.__sexo == "M":
            return 10*self.__peso + 6.25*altura_cm - 5*self.__idade + 5
        else:
            return 10*self.__peso + 6.25*altura_cm - 5*self.__idade - 161

    # Gasto Energético Total (GET)
    def calcular_get(self):
        return self.calcular_tmb() * self.__atividade

    # Meta Calórica
    def calcular_meta_calorica(self):
        get = self.calcular_get()

        if self.__objetivo == 1:  # perda
            return get - 400
        # Número escolhido ao acaso, pra representar o quanto algm gostaria de ganhar ou perder
        elif self.__objetivo == 2:  # manutenção
            return get
        else:  # ganho
            return get + 400

    # Converter para JSON
    def to_dict(self):
        return {
            "nome": self.__nome,
            "senha": self.__senha,
            "idade": self.__idade,
            "peso": self.__peso,
            "altura": self.__altura,
            "objetivo": self.__objetivo,
            "sexo": self.__sexo,
            "atividade": self.__atividade,
            "alimentos": self.__alimentos
        }