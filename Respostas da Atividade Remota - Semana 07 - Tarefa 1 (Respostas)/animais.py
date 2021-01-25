class Animal():
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def __str__(self):
        return f"Nome: {self.nome}\nPeso: {self.peso:.2f}"


class Peixe(Animal):
    def __init__(self, nome, peso, tipo_habitat):
        super().__init__(nome, peso)
        self.tipo_habitat = tipo_habitat

    def __str__(self):
        return super().__str__()+"\n"+f"Habitat: {self.tipo_habitat}"


class Cachorro(Animal):
    def __init__(self, nome, peso, raca):
        super().__init__(nome, peso)
        self.raca = raca

    def __str__(self):
        return super().__str__()+"\n"+f"Raça: {self.raca}"    
    
