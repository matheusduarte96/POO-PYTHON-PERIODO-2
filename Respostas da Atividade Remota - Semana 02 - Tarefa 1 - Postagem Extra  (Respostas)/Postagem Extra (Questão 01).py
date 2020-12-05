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
    estacao = 80

    #Métodos
    def ligar(self, liga):
        self.liga = liga
        print(f"O rádio está {self.liga}.")

    def desligado(self, liga):
        self.estado = liga
        if self.estado == "desligado":
            print(f"O rádio está {self.estado}.")

    def mudar_frequencia(self, frequencias, liga):
        self.estado = liga
        if self.estado == "ligado":
            self.frequencia = frequencias
            print(f"A frequncia atual da rádio é a {self.frequencia}.")

    def mudar_estacao_cima(self, liga):
        self.estado = liga
        if self.estado == "ligado":
            self.estacao += 10
            print(f"A estação atual é {self.estacao}.")

    def mudar_estacao_baixo(self, liga):
        self.estado = liga
        if self.estado == "ligado":
            self.estacao -= 5
            print(f"A estação atual é {self.estacao}.")

#Criação dos objetos
meu_radio = Radio()
meu_radio.estado = 'ligado'
meu_radio.cor = "azul escuro"
meu_radio.frequencia = "AM"
meu_radio.estacao = 80
meu_radio.ligar(meu_radio.estado)
meu_radio.mudar_frequencia(meu_radio.frequencia, meu_radio.estado)
meu_radio.mudar_estacao_cima(meu_radio.estado)
meu_radio.mudar_estacao_baixo(meu_radio.estado)
print(f"A Cor do rádio é {meu_radio.cor}.")
        
    
