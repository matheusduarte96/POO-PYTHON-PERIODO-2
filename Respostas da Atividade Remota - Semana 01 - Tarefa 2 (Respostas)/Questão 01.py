#Questão 01

"""Execute os objetos, invocando os métodos necessários de
acordo como que se pede:
a) Acelere o fusca para a velocidade 40
b) Acelere a ferrari para a velocidade 200
c) Desligue o fusca
d) Ligue a ferrari
e) acelere a ferrari para 320
f) Pare a ferrari.
g) Desligue a ferrari
h) Ligue o fusca
i) Acelere o fusca para 100
j) Desligue o fusca"""


class carro:
    Nome = None
    Ano = None
    Cor = None
    Veloc_max = None
    Veloc_atual = None
    Estado = None
    
    def ligar(self, Estado):
        if self.Estado == "ligado":
            print("ligado")
            
    def acelerar(self, Nome, Veloc_atual, Estado):
        if self.Estado == "ligado" and self.Nome == "fusca":
            self.Veloc_max = 80
            self.Veloc_atual = Veloc_atual
            if self.Veloc_atual > self.Veloc_max:
                print(f"A velocidade atual ultrapassa a permitida do veículo que é {self.Veloc_max}.")
                return
            else:
                print(f"A velocidade atual é {self.Veloc_atual}.")
                
        elif self.Estado == "ligado" and self.Nome == "ferrari":
            self.Veloc_max = 300
            self.Veloc_atual = Veloc_atual
            if self.Veloc_atual > self.Veloc_max:
                print(f"A velocidade atual ultrapassa a permitida do veículo que é {self.Veloc_max}.")
                return
            else:
                print(f"A velocidade atual é {self.Veloc_atual}.")
                
    def desligar(self, Estado):
        if self.Estado == "desligado":
            print("desligado")
        
    def parar(self, Estado, Veloc_atual):
        if self.Estado == "parar":
            self.Veloc_atual = 0
            if self.Veloc_atual == 0:
                print("carro parado")
                return

carro = carro()
carro.Nome = "fusca"
carro.Veloc_atual = 100
carro.Estado = "desligado"
carro.ligar(carro.Estado)
carro.desligar(carro.Estado)
carro.parar(carro.Estado, carro.Veloc_atual)
carro.acelerar(carro.Nome, carro.Veloc_atual, carro.Estado)



