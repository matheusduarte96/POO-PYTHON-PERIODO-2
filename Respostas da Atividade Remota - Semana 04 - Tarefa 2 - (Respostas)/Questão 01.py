#Questão 01

class Pessoa():
    def __init__(self, nome, idade, peso, altura, sexo, estado="vivo", estado_civil="solteiro", conjuge=None):
        self.nome = nome
        self.__idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.estado = estado
        self.estado_civil = estado_civil
        self.conjuge = conjuge          


    @property
    def idade(self):
        return self.__idade  
    
    @idade.setter
    def idade(self, idade):
        I = self.__idade
        i = idade
        if self.estado == "morto(a)":
            print(f"{self.nome} está morto.")
        elif I == i:
            self.__idade = idade
            print(f"A idade de {self.nome} é {self.__idade}.")
        else:
            print("sem permissão")
  
                    
    def envelhecer(self):
        if self.estado == "morto(a)":
            print(f"{self.nome} está {self.estado}.")
        else:
            self.__idade += 1
            if self.__idade <= 21:
                self.altura += 5
                print(f"{self.nome} tem {self.__idade} anos e {self.altura} cm de altura.")


    def crescer(self, valor):
        if self.__idade <= 21:
            self.altura += valor
            print(f"{self.nome} tem {self.altura} cm de altura.")
        else:
            print(f"{self.nome} não pode mais crescer pois está com 21 anos ou mais.")

        
    def engordar(self, valor):
        if self.estado == "morto(a)":
            print(f"Operação não realizada. {self.nome} está morto(a).")
        else:
            self.peso += valor
            print(f"{self.nome} está pesando {self.peso}.")


    def emagrecer(self, valor):
        self.peso -= valor
        print(f"{self.nome} emagreceu e está pesando {self.peso}.")


    def casar(self, nome_conjuge):
        self.estado_civil = "casado(a)"
        self.conjuge = nome_conjuge

        if self.estado == "morto(a)":
            print(f"Casamento não realizado. {self.nome} está morto.")
            
        elif self.conjuge == "Maria" or self.conjuge == "Carlos" or self.conjuge == "João":
            print(f"Casamento não permitido. {self.conjuge} é de menor.")
            
        else:
            print(f"{self.nome} está {self.estado_civil} com {self.conjuge}.")

        
    def morrer(self):
        self.estado = "morto(a)"
        print(f"{self.nome} está {self.estado}.")
            


maria = Pessoa("Maria", 5, 20, 100, "F")
maria.idade = 10
maria.envelhecer()
maria.morrer()
maria = Pessoa("Maria", 5, 20, 100, "F", "morto(a)")
maria.engordar(5)

print("-="*25)

joão = Pessoa("João", 12, 40, 140, "M")
joão.idade = 50

print("-="*25)

pedro = Pessoa("Pedro", 22, 65, 170, "M")
pedro.crescer(2)
pedro.casar("Maria")
pedro.casar("Julia")
pedro = Pessoa("Pedro", 22, 65, 170, "M", "vivo","casado(a)")
pedro.morrer()
pedro = Pessoa("Pedro", 22, 65, 170, "M", "morto(a)")
pedro.casar("Bia")
pedro.idade = 22


print("-="*25)

bia = Pessoa("Bia", 18, 55, 160, "F")
bia.casar("Carlos")
bia.casar("Jonas")
bia.morrer()

julia = Pessoa("Julia", 30, 65, 170, "F")
cadu = Pessoa("Carlos", 2, 11, 80, "M")

print("-="*25)

jonas = Pessoa("Jonas", 34, 70, 180, "M")
jonas.casar("Júlia")









