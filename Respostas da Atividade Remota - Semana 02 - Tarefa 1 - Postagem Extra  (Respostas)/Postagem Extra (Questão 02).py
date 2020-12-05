#Postagem Extra (Questão 02)
"""2. Melhore a classe Bicicleta, colocando limites máximos e mínimos para os estados:
veloc_atual, altura_cela e calibragem_pneus através de seus respectivos métodos.
Altere os métodos: regular_cela e calibrar_pneus para só
permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0)."""

class Bicicleta():
    #Atributos
    peso = None
    altura = None
    veloc_atual = 0
    cor = None
    aro = None
    altura_cela = 0
    calibragem_pneus = 0

    #métodos
    def pedalar(self):
        veloc_maxima = 40
        veloc_minima = 10
        if self.veloc_atual > veloc_maxima:
            print("Velocidade acima do permitido.")
        elif self.veloc_atual < veloc_minima:
            print("Velocidade abaixo do permitido.")
        else:
            self.veloc_atual += 1
            if self.veloc_atual > veloc_maxima:
                pass
            else:
                print(f"velocidade atual: {self.veloc_atual}.")

    def frear(self):
        veloc_minima = 10
        if self.veloc_atual < veloc_minima:
            pass
        else:
            self.veloc_atual -= 1
            print(f"velocidade atual: {self.veloc_atual}.")

    def regular_cela(self, valor, velocidade):
        altura_cela = 10
        self.altura_cela = valor
        self.veloc_atual = velocidade
        if self.veloc_atual == 0:
            if self.altura_cela > altura_cela:
                print("Altura acima do permitido.")
            elif self.altura_cela < 5:
                print("Altura abaixo do permitido.")
            else:
                self.altura_cela = valor
                print(f"Altura atual da cela: {self.altura_cela} cm.")

    def calibrar_pneus(self, valor, velocidade):
        calibragem_pneus = 35
        self.veloc_atual = velocidade
        self.calibragem_pneus = valor
        if self.veloc_atual == 0:
            if self.calibragem_pneus > calibragem_pneus:
                print("Calibragem acima do permitido.")
            elif self.calibragem_pneus < 25:
                print("Calibragem abaixo do permitido.")
            else:
                self.calibragem_pneus = valor           
                print(f"Calibragem atual dos pneus: {self.calibragem_pneus} libras.")
        

# criação dos objetos
minha_bicicleta = Bicicleta()
minha_bicicleta.peso = 10
minha_bicicleta.altura = 100
minha_bicicleta.veloc_atual = 0
minha_bicicleta.cor = 'amarela'
minha_bicicleta.aro = 29
minha_bicicleta.regular_cela(5, minha_bicicleta.veloc_atual)
minha_bicicleta.calibrar_pneus(25, minha_bicicleta.veloc_atual)
minha_bicicleta.pedalar()
minha_bicicleta.frear()
print(f"Cor: {minha_bicicleta.cor}.")
print(f"Aro: {minha_bicicleta.aro}.")
