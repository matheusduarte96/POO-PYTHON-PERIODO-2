#Questão 02
"""Crie uma classe Ponto2D que contenha os seguintes atributos:
X # valor da coordenada X
Y # valor da coordenada Y
❖ Crie um construtor que crie uma instância da classe ponto de duas formas (usar parâmetros opcionais):
1ª : passando as coordenadas X, Y
2ª : sem passar as coordenadas X,Y. Neste caso a instância seria criada na origem,
ou seja, nas coordenadas (0,0)
❖ Crie um método para comparar se dois pontos(objetos) estão nas mesmas coordenadas:
Ex: def ÉIgual(Ponto2D outroPonto2D). Este método retorna
True se os pontos tiverem as mesmas coordenadas e False, caso contrário."""

class Ponto2D():
    #Atributos
    X = None
    Y = None

    #Construtor
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    #Método
    def Eigual(self, outroponto):
        X = outroponto
        Y = outroponto
        if self.X == X:
            print("X", True)
        elif self.Y == Y:
            print("Y", True)
        else: print(False)

#Objetos
PontoX = Ponto2D(X=6)
PontoX.Eigual(6)
PontoY = Ponto2D(Y=6)
PontoY.Eigual(7)
