
class Bateria():
    def __init__(self, codigo, capacidade, percentual_carga):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self.__percentual_carga = percentual_carga

    @property
    def codigo(self):
        return self.__codigo

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def percentual_carga(self):
        return self.__percentual_carga

    def Carregar(self, valor):
        if self.__percentual_carga + valor <= 100:
            self.__percentual_carga += valor
        return self.__percentual_carga

    def Descarregar(self, valor):
        if self.__percentual_carga + valor > 0 and self.__percentual_carga + valor <=100:
            self.__percentual_carga -= valor
        return self.__percentual_carga

class Celular():
    def __init__(self, ligado, mei, bateria, wifi):
        self.__ligado = ligado
        self.__mei = mei
        self.__bateria = bateria
        self.__wifi = wifi

    @property
    def ligado(self):
        return self.__ligado
    
    @property
    def mei(self):
        return self.__mei

    @property
    def bateria(self):
        return self.__bateria

    @property
    def wifi(self):
        return self.__wifi

    def LigarDesliga(self):
        if self.__percentual_carga == 0:
            self__ligado = False
            print("sem carga de bateria")
        else:
            self__ligado = True
            print(f"Percentual da bateria é de {self.__percentual_carga}")

    def colocarBateria(self, bateria):
        if self.__percentual_carga == None:
            if type(bateria) == Bateria:
                self.__bateria = bateria

    def retirarBateria(self):
        if self.__percentual_carga == None:
            print("celular sem bateria")
        else:
            self.__bateria = None

    def LigarDesligarWifi(self):
        if self.__ligado == True:
            self.__wifi = True
        else:
            self.__wifi = False

    def assistirVideo(self, tempo):
        carga = tempo * 5
        if carga <= 50:
            self.__percentual_carga = 0
        else:
            if self.__wifi == True and self.__percentual_carga > 50:
                print("permitido assistir um video")
            self.__percentual_carga
        return self.__percentual_carga
            
    def carregar(self, valor):
        if type(valor) == Bateria:
            self.valor.Carregar()#falta passar um argumento

    def descarregar(self, valor):
        if type(valor) == Bateria:
            self.valor.Descarregar()#falta passar um argumento
        
    def __str__(self):
        return f"A bateria está em {self.__percentual_carga}"
            
        















