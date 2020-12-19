#Questão 01
"""1. Reescreva a classe Carro descrita no exercício anterior,
acrescentando encapsulamento nos atributos.
Crie dois ou mais objetos de formas diferentes
e imprima os valores de seus respectivos atributos."""

class carro:
    #Construtor para a classe carro.
    def __init__(self, estado, veloc_atual,veloc_max, cor="sem cor",nome= "sem nome"):
        self.__estado = estado
        self.__veloc_atual = veloc_atual
        self.veloc_max = veloc_max
        self.cor = cor
        self.nome = nome
        
    #Métodos       
    def getligar(self):
        if self.__estado == True:
            return "ligado"
        else: return carro.getdesligar(self)
        
    def getacelerar(self):
        if self.__estado == True and self.nome == "Oroch":
            if self.__veloc_atual > self.veloc_max:
                return f"A velocidade atual da {self.nome} ultrapassa a permitida do veículo que é {self.veloc_max}."
            else:
                return f"A velocidade atual do {self.nome} é {self.__veloc_atual}."
            
        elif self.__estado == True and self.nome == "Corolla":
            if self.__veloc_atual > self.veloc_max:
                return f"A velocidade atual da {self.nome} ultrapassa a permitida do veículo que é {self.veloc_max}."
            else:
                return f"A velocidade atual do {self.nome} é {self.__veloc_atual}."
         
        else: return ""
        
    def getparar(self):
        if self.__veloc_atual == 0:
            return "carro parado"
        else: return ""
        
    def getdesligar(self):
        if self.__estado == False:
            return "desligado"

    
#Criação dos objetos     
#Oroch
meu_carro1 = carro(True, 0, 80, "Preto", "Oroch")
print(f"O carro é um: {meu_carro1.nome}.")
print(meu_carro1.getligar())
print(meu_carro1.getacelerar())
print(meu_carro1.getparar())
print(f"A cor do carro é: {meu_carro1.cor}.")

print("-="*37)

#Corolla
meu_carro2 = carro(True, 87, 100, "Vermelho","Corolla")
print(f"O carro é um: {meu_carro2.nome}.")
print(meu_carro2.getligar())
print(meu_carro2.getacelerar())
print(meu_carro2.getparar())
print(f"A cor do carro é: {meu_carro2.cor}.")
