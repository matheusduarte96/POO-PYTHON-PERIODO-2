#Questão 01 e 02

"""1. Reescreva a classe Carro descrita no exercício anterior, agora utilizando construtores.
2. Crie os objetos descritos no exercício anterior, agora utilizando construtores.
Considerar como padrão os valores:
ligado=False ou estado=”desligado”, velocidade_atual=0. Atributos obrigatórios: cor, nome e veloc.máx"""

class carro:
    
    #Atributos
    nome = None
    ano = None
    cor = None
    veloc_max = None
    veloc_atual = 0
    ligado=False

    #Construtor para a classe carro.
    def __init__(self, nome, cor, veloc_max, ligado):
        self.nome = nome
        self.cor = cor
        self.veloc_max = veloc_max
        self.ligado = ligado

    #Métodos 
    def ligar(self):
        ligado = self.ligado
        if self.ligado == True:
            print("ligado")
        else:
            carro.desligar(self, ligado)
        
    def acelerar(self, veloc_atual):
        if self.ligado == True and self.nome == "fusca":
            self.veloc_max = 80
            self.veloc_atual = veloc_atual
            if self.veloc_atual > self.veloc_max:
                print(f"A velocidade atual do {self.nome} ultrapassa a permitida do veículo que é {self.veloc_max}.")
                return
            else:
                print(f"A velocidade atual do {self.nome} é {self.veloc_atual}.")
               
        elif self.ligado == True and self.nome == "ferrari":
            self.veloc_max = 300
            self.veloc_atual = veloc_atual
            if self.veloc_atual > self.veloc_max:
                print(f"A velocidade atual da {self.nome} ultrapassa a permitida do veículo que é {self.veloc_max}.")                
            else:
                print(f"A velocidade atual da {self.nome} é {self.veloc_atual}.")

    def desligar(self, ligado):
        if self.ligado == False:
            print("desligado")
        
    def parar(self, veloc_atual):
        if self.veloc_atual:
            print("carro parado")
        

#Criação dos objetos     
#Fusca
meu_carro1 = carro("fusca","preto",80, True)
meu_carro1.acelerar(40)
meu_carro1 = carro("fusca","preto",80, False)
meu_carro1.ligar()
meu_carro1 = carro("fusca","preto",80, True)
meu_carro1.ligar()
meu_carro1.acelerar(100)
meu_carro1 = carro("fusca","preto",80, False)
meu_carro1.ligar()

print("-="*37)

#Ferrari
meu_carro2 = carro("ferrari","vermelho",300, True)
meu_carro2.acelerar(200)
meu_carro2.ligar()
meu_carro2.acelerar(320)
meu_carro2.parar(0)
meu_carro2 = carro("ferrari","vermelho",300, False)
meu_carro2.ligar()


