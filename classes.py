# Classes legais

class User:
    # Construtor
    def __init__(self, nome, senha, idade, peso, altura, objetivo, sexo, atividade, meta_calorica):
        # __ Encapsulamento
        self.__nome = nome
        self.__senha = senha
        self.__idade = int(idade)
        self.__peso = float(peso)
        self.__altura = float(altura)
        self.__objetivo = int(objetivo)
        # Meta calórica pode ser None, caso o objetivo do usuário seja apenas manter o corpinho, então o que aparecerá como sua meta, será apenas o que ele precisa
        # "queimar" para não engordar
        self.__meta_calorica = float(meta_calorica) if meta_calorica is not None else None
        
        # Os dois abaixo são importantes para o cálculo correto do GET e TMB
        self.__sexo = sexo
        self.__atividade = float(atividade)

        # O usuário TEM um cardápio (composição)
        self.__cardapio = Cardapio()

    # Getters

    def get_nome(self):
        return self.__nome

    def get_cardapio(self):
        return self.__cardapio

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

    # Meta
    def calcular_meta_calorica(self):
        if self.__objetivo == 2:  # manutenção
            return self.calcular_get()
            # o que foi comentado lá no início, return GET, pois é o mínimo necessário para não engordar
            # (pelo oq eu entendi)
        return self.__meta_calorica

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
            "alimentos": self.__cardapio.to_list(),
            "meta_calorica": self.__meta_calorica
        }

class Alimento:
    def __init__(self, nome, quantidade, caloria, macronutrientes):
        self.nome = nome
        self.quantidade = float(quantidade)
        self.caloria = float(caloria)
        self.macronutrientes = macronutrientes

    def calcular_caloria_total(self):
        return self.caloria

    def to_dict(self):
        return {
            "nome": self.nome,
            "quantidade": self.quantidade,
            "caloria": self.caloria,
            "macronutrientes": self.macronutrientes
        }


class Cardapio:
    def __init__(self):
        self.alimentos = []

    def adicionar_alimento(self, alimento):
        self.alimentos.append(alimento)

    def calcular_total_calorias(self):
        # Pega cada um dos alimentos salvado na lista pelo método acima, puxa a sua respectiva
        # caloria pelo método puxado da classe alimento e soma geral :D
        return sum(a.calcular_caloria_total() for a in self.alimentos)

    def to_list(self):
        return [a.to_dict() for a in self.alimentos]
