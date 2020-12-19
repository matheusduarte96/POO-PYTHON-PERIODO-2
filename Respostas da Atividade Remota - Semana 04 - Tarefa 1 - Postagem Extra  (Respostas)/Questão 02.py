#Questão 02
"""2. Reescreva a classe Gato descrita no slide da aula 4,
acrescentando encapsulamento nos atributos.
Crie pelo menos dois objetos,
imprima os valores de seus atributos antes de depois de executar os métodos definidos."""


class Gato:
    #Construtor
    def __init__(self,idade,peso=0, nome="sem nome",raça="sem raça"):
        self.__idade = idade
        self.__peso = peso
        self.nome = nome
        self.raça = raça
        
    #Métodos
    def mudar_nome(self):
        return self.nome

    def getengordar(self):
        self.__peso += self.__peso
        return self.__peso

    def getenvelhecer(self): 
        self.__idade += 1
        return self.__idade
            
#Criação de Objetos
cat1 = Gato(2, 5, "Remela", "Vira-lata")
print(f"O nome do gato é: {cat1.nome}")
print(cat1.getengordar())
print(cat1.getenvelhecer())
print(f"A raça do gato é: {cat1.raça}")

print("-="*15)

cat2 = Gato(2, 6, "Bibi", "Vira-lata")
print(f"O nome do gato é: {cat2.nome}")
print(cat2.getengordar())
print(cat2.getenvelhecer())
print(f"A raça do gato é: {cat2.raça}")
