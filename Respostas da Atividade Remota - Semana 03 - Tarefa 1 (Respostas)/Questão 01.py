#Questão 01
"""1. Reescreva a classe Carro descrita no exercício anterior,
agora utilizando construtores com parâmetros opcionais.
Crie dois ou mais objetos de formas diferentes
e imprima os valores de seus respectivos atributos."""

class carro:
    #Construtor para a classe carro.
    def __init__(self, veloc_max, veloc_atual=0, ligado=False, cor="sem cor", nome="sem nome"):
        self.veloc_max = veloc_max
        self.veloc_atual = veloc_atual
        self.ligado = ligado
        self.cor = cor
        self.nome = nome

    #Métodos 
    def ligar(self):
        ligado = self.ligado
        if self.ligado == True:
            print("ligado")
        else:
            carro.desligar(self, ligado)
        
    def acelerar(self):
        if self.ligado == True and self.nome == "savero":
            self.veloc_max = 80
            if self.veloc_atual > self.veloc_max:
                print(f"A velocidade atual da {self.nome} ultrapassa a permitida do veículo que é {self.veloc_max}.")
                return
            else:
                print(f"A velocidade atual da {self.nome} é {self.veloc_atual}.")
               
        elif self.ligado == True and self.nome == "lamburguini":
            self.veloc_max = 300
            if self.veloc_atual > self.veloc_max:
                print(f"A velocidade atual da {self.nome} ultrapassa a permitida do veículo que é {self.veloc_max}.")                
            else:
                print(f"A velocidade atual da {self.nome} é {self.veloc_atual}.")

    def desligar(self):
        if self.ligado == False:
            print("desligado")
        
    def parar(self):
        if self.veloc_atual:
            print("carro parado")
        

#Criação dos objetos     
#Savero
meu_carro1 = carro(0, 80, True, "cinza", "savero")
meu_carro1.veloc_atual = 40
meu_carro1.acelerar()
meu_carro1.ligar()
meu_carro1 = carro(40, 80, False, "cinza", "savero")
meu_carro1.desligar()
meu_carro1 = carro(40, 80, True, "cinza", "savero")
meu_carro1.veloc_atual = 100
meu_carro1.acelerar()
meu_carro1 = carro(100, 80, True, "cinza", "savero")
meu_carro1.ligar()
print(f"A cor do carro é: {meu_carro1.cor}.")

print("-="*37)

#Lamburguini
meu_carro2 = carro(0, 200, True,"azul escuro", "lamburguini")
meu_carro2.veloc_atual = 200
meu_carro2.acelerar()
meu_carro2.ligar()
meu_carro2.veloc_atual = 320
meu_carro2.acelerar()
meu_carro2.parar()
meu_carro2 = carro(0, 200, True,"azul escuro", "lamburguini")
meu_carro2.ligar()
print(f"A cor do carro é: {meu_carro2.cor}.")

