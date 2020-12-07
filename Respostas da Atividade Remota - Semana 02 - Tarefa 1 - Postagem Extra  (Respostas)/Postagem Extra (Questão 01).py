#Postagem Extra (Questão 01)
"""1. Exercitando o processo de abstração, modele uma classe Rádio com seus estados e comportamentos.
Crie a respectiva classe em python e depois crie 2 objetos,
imprima os valores de seus atributos e execute os métodos criados.
Recomendação: criar estados que possam ter seus valores alterados por seus métodos."""

class Radio():
    #Atributos
    estado = None
    cor = None
    frequencia = None #AM/FM
    peso = None
    estacao = None
    volume = 0

    #Métodos
    def ligar(self):
        self.estado = "ligado"
        print(f"O rádio está {self.estado}.")

    def desligar(self):
        if self.estado == "ligado": 
            self.estado = "desligado"
            print(f"O rádio está {self.estado}.")

    def mudar_frequencia(self):
        if self.estado == "ligado":
            print(f"A frequncia atual da rádio é a {self.frequencia}.")

    def mudar_estacao_cima(self):
        if self.estado == "ligado":
            self.estacao += 10
            print(f"A estação atual é {self.estacao}.")

    def mudar_estacao_baixo(self):
        if self.estado == "ligado":
            self.estacao -= 5
            print(f"A estação atual é {self.estacao}.")
            
    def aumentar_volume(self):
        if self.volume > 10:
            print("Volume acima do permitido.")
        elif self.volume < 0:
            print("Volume abaixo do permitido.")
        else:
            self.volume += 1
            print(f"O volume atual é {self.volume}.")
    def diminuir_volume(self):
        if self.volume < 0:
            print("Volume abaixo do permitido.")
        elif self.volume > 10:
            print("Volume acima do permitido.")
        else:
            self.volume -= 1
            print(f"O volume atual é {self.volume}.") 


#Criação dos objetos
meu_radio = Radio()
meu_radio.ligar()
meu_radio.cor = "preto"
meu_radio.frequencia = "FM"
meu_radio.mudar_frequencia()
meu_radio.volume = 8
meu_radio.aumentar_volume()
meu_radio.estacao = 80
meu_radio.mudar_estacao_baixo()
meu_radio.volume = 9
meu_radio.diminuir_volume()
meu_radio.mudar_estacao_cima()
meu_radio.desligar()
print(f"A Cor do rádio é {meu_radio.cor}.")
        
    
