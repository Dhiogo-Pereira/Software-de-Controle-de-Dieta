# Classes legais

class User:
    # Construtor
    def __init__(self, nome, senha, idade, peso, altura, objetivo, sexo, atividade):
        if int(idade) <= 0:
            raise ValueError("Idade inválida")

        if float(peso) <= 0:
            raise ValueError("Peso inválido")

        if float(altura) <= 0:
            raise ValueError("Altura inválida")

        if int(objetivo) not in [1, 2, 3]:
            raise ValueError("Objetivo inválido")

        if sexo not in ["M", "F"]:
            raise ValueError("Sexo inválido")

        self.__nome = nome
        self.__senha = senha
        self.__idade = int(idade)
        self.__peso = float(peso)
        self.__altura = float(altura)
        self.__objetivo = int(objetivo)
        self.__sexo = sexo
        self.__atividade = float(atividade)

        self.__alimentos = []

    # Getters
    def get_nome(self):
        return self.__nome

    def get_alimentos(self):
        return self.__alimentos

    # Segurança
    def verificar_senha(self, senha):
        return self.__senha == senha

    # TMB - Fórmula de Mifflin-St Jeor
    # https://reference.medscape.com/calculator/846/mifflin-st-jeor-equation
    def calcular_tmb(self):
        altura_cm = self.__altura * 100

        if self.__sexo == "M":
            return 10*self.__peso + 6.25*altura_cm - 5*self.__idade + 5
        else:
            return 10*self.__peso + 6.25*altura_cm - 5*self.__idade - 161

    # GET - Peguei a formulinha que o gemini me deu, não achei informações em site algum
    def calcular_get(self):
        return self.calcular_tmb() * self.__atividade

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