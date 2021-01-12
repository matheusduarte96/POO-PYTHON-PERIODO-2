#Questão 01

total = []
class Bomba_de_Combustivel():
    def __init__(self, numero, valorLitro, quantidadeCombustivel, capacidade_da_bomba=30000, valor_faturado=0, quantidade_vendida=0, tipoCombustivel=1):
        self.__numero = numero
        self.__valorLitro = valorLitro
        self.__capacidade_da_bomba = capacidade_da_bomba
        self.__quantidadeCombustivel = quantidadeCombustivel
        self.__valor_faturado = valor_faturado
        self.__quantidade_vendida = quantidade_vendida
        self.__tipoCombustivel = tipoCombustivel 

    @property
    def quantidade_vendida(self):
        return self.__quantidade_vendida

    @property
    def valor_faturado(self):
        return self.__valor_faturado
    
    @property
    def capacidade_da_bomba(self):
        return self.__capacidade_da_bomba
    
    @property
    def quantidadeCombustivel(self):
        return self.__quantidadeCombustivel

    @property
    def tipoCombustivel(self):
        return self.__tipoCombustivel
    
    @property
    def valorLitro(self):
        return self.__valorLitro

    @tipoCombustivel.setter
    def tipoCombustivel(self, valor):
        self.__tipoCombustivel = valor


    def esvaziarBomba(self):
        self.__quantidadeCombustivel = 0
        return self.__quantidadeCombustivel

            
    def abastecerBomba(self, quantidade):
        if self.__quantidadeCombustivel + quantidade <= self.__capacidade_da_bomba:
            self.__quantidadeCombustivel += quantidade
        else:
            self.__quantidadeCombustivel = self.__capacidade_da_bomba            
        return self.__quantidadeCombustivel

    
    def abastecerVeiculoPorValor(self, valor):
        litro = valor / self.__valorLitro
        self.__quantidade_vendida += litro
        
        return self.__quantidade_vendida
    

    def abastecerVeiculoPorLitro(self, quantidade):
        valor = quantidade * self.__valorLitro
        self.__valor_faturado += valor
        
        total.append(self.__valor_faturado)
        return self.__valor_faturado


    def __str__(self):
        return f"Bomba nº {self.__numero}\nA quantidade atual do litro da bomba é {self.__quantidade_vendida:.2f}L\nO valor faturado é R$ {self.__valor_faturado:.2f}"


bomba1 = Bomba_de_Combustivel(1, 4.36, 2000)
bomba1.tipoCombustivel = 1
bomba1.esvaziarBomba()
bomba1.abastecerBomba(25000)
bomba1.abastecerVeiculoPorValor(30)
bomba1.abastecerVeiculoPorLitro(15)
print(bomba1)

print("-="*25)

bomba2 = Bomba_de_Combustivel(2, 4.54, 2000)
bomba2.tipoCombustivel = 2
bomba2.esvaziarBomba()
bomba2.abastecerBomba(2000)
bomba2.abastecerVeiculoPorValor(60)
bomba2.abastecerVeiculoPorLitro(20)
print(bomba2)

print("-="*25)

bomba3 = Bomba_de_Combustivel(3, 3.45, 2000)
bomba3.tipoCombustivel = 3
bomba3.esvaziarBomba()
bomba3.abastecerBomba(5000)
bomba3.abastecerVeiculoPorValor(40)
bomba3.abastecerVeiculoPorLitro(25)
print(bomba3)        

print("-="*25)

bomba4 = Bomba_de_Combustivel(4, 4.29, 2000)
bomba4.tipoCombustivel = 4
bomba4.esvaziarBomba()
bomba4.abastecerBomba(7500)
bomba4.abastecerVeiculoPorValor(55)
bomba4.abastecerVeiculoPorLitro(35)
print(bomba4) 

print("-="*25)

print(f"O faturamento do posto é R$ {sum(total):.2f}")
