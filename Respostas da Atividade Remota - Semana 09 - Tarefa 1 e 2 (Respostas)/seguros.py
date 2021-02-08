class Cliente:
    def __init__(self, cpf, nome, idade):
        self._cpf = cpf
        self._nome = nome
        self._idade = idade
        
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade

    def __str__(self):
        return f"CPF: {self._cpf}\nNome: {self._nome}\nIdade: {self._idade}"

    
class Seguro:
    def __init__(self, num_apolice, proprietario):
        self._num_apolice = num_apolice
        
        if type(proprietario) == Cliente:
            self._proprietario = proprietario
        else:
            self._proprietario = None

    def calcularValor(self):
        pass
    
    def calculaPremio(self):
        pass

    def __str__(self):
        pass
    

class SeguroVida(Seguro):
    def __init__(self, num_apolice, proprietario, nome_beneficiario):
        super().__init__(num_apolice, proprietario) 
        self.__nome_beneficiario = nome_beneficiario
               
    
    def nome_beneficiario(self):
        return nome_beneficiario


    def calculaValor(self):
        valor = 0
        if self._proprietario.idade <= 30:
            valor = 800
        elif self._proprietario.idade >= 31 and self._proprietario.idade <= 50:
            valor = 1300
        elif self._proprietario.idade > 50:
            valor = 1600
        return valor
    
    def calculaPremio(self):
        valor = 0
        if self._proprietario.idade <= 30:
            valor = 50000
        elif self._proprietario.idade >= 31 and self._proprietario.idade <= 50:
            valor = 30000
        elif self._proprietario.idade > 50:
            valor = 20000
        return valor

    def __str__(self):
        return f"Nº Apólice: {self._num_apolice}\nBeneficiário: {self.__nome_beneficiario.nome}\nValor: R$ {self.calculaValor():.2f}\nPrêmio: R$ {self.calculaPremio():.2f}"

    
class SeguroAutomovel(Seguro):
    def __init__(self, num_apolice, proprietario, numero_licenca, nome_modelo, ano, valorAutomovel):
        super().__init__(num_apolice, proprietario)
        self.__numero_licenca = numero_licenca
        self.__nome_modelo = nome_modelo
        self.__ano = ano
        self.__valorAutomovel = valorAutomovel
    
    @property
    def numero_licenca(self):
        return self.__numero_licenca

    @property
    def nome_modelo(self):
        return self.__nome_modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def valorAutomovel(self):
        return self.__valorAutomovel
    
    def calculaValor(self):
        valor = self.__valorAutomovel * 0.03 
        return valor

    def calculaPremio(self):
        premio = self.__valorAutomovel * 0.8
        return premio

    def calculaFranquia(self):
        franquia = (self.__valorAutomovel * 0.03) * 0.4
        return franquia

    def __str__(self):
        return f"""Nº Apólice: {self._num_apolice}\nSegurado: {self._proprietario.nome}
Valor: R$ {self.calculaValor():.2f}\nPrêmio: R$ {self.calculaPremio():.2f}\nValor Franquia: R$ {self.calculaFranquia():.2f}"""
    
    








