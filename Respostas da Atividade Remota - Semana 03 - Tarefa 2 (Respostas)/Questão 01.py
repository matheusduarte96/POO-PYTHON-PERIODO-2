#Questão 01

class televisao():
    #Construtor da classe televisao
    def __init__(self, ligada=False, canal=0, volume=0, canal_min=2, canal_max=99,volume_min=2, volume_max=100):
        self.ligada = ligada
        self.canal = canal
        self.volume = volume
        self.canal_min = canal_min
        self.canal_max = canal_max
        self.volume_min = volume_min
        self.volume_max = volume_max

    #Métodos
    def ligar(self):
        self.ligada = True
        self.volume = volume_min
        print(f"A TV está ligada e está no volume {self.volume}.")

    def desligar(self):
        self.ligada = False
        print("A TV está desligada.")

    def mudar_canal(self, valor):
        if self.ligada == True:
            if valor > self.canal_max:
                print("O valor ultrapassa o limite máximo de canais.")
            elif valor < self.canal_min:
                print("O valor está abaixo do limite mínimo de canais.")
            else:
                self.canal = valor
                print(f"O canal escolhido foi {self.canal}.")
                
    def aumentar_canal(self, valor):
        if self.ligada == True:
            self.canal += valor
            if self.canal > self.canal_max:
                print("O canal ultrapassa o limite máximo de canais na TV.")
            elif valor == 0:
                self.canal += 1
                print(f"Canal atual: {self.canal}.")
            else:
                print(f"Canal atual: {self.canal}.")

    def diminuir_canal(self, valor):
        if self.ligada == True:
            self.canal -= valor
            if self.canal < self.canal_min:
                print("O canal está abaixo do limite máximo de canais na TV.")
            elif valor == 0:
                self.canal -= 1
                print(f"Canal atual: {self.canal}.")
            else: print(f"Canal atual: {self.canal}.")

    def aumentar_volume(self, valor):
        if self.ligada == True:
            self.volume += valor
            if self.volume > self.volume_max:
                print("O volume ultrapassa o limite máximo permitido da TV.")
            elif valor == 0:
                self.volume += 1
                print(f"Volume atual: {self.volume}.")
            else: print(f"Volume atual: {self.volume}.")

    def diminuir_volume(self, valor):
        if self.ligada == True:
            self.volume -= valor
            if self.volume < self.volume_min:
                print("O volume está abaixo do permitido da TV.")
            elif valor == 0:
                self.volume -= 1
                print(f"Volume atual: {self.volume}.")
            else: print(f"Volume atual: {self.volume}.")


#Criação dos objetos  
tv_da_sala = televisao(True, 2)
tv_da_sala.aumentar_volume(10)
for d in range(2, 12):
    d*=2
tv_da_sala.aumentar_volume(d-1)    
tv_da_sala.mudar_canal(120)
for j in range(2, 23):
    j -= 15
tv_da_sala.aumentar_volume(j-1)
tv_da_sala.aumentar_canal(0)
tv_da_sala.desligar()

print("-="*30)

tv_do_quarto = televisao(True, 13)
tv_do_quarto.aumentar_volume(50)
tv_do_quarto.diminuir_canal(10)
for f in range(2, 54):
    f //= 3
tv_do_quarto.diminuir_volume(f+1)
tv_do_quarto.desligar()
tv_do_quarto = televisao(True, 13)
tv_do_quarto.aumentar_canal(4)
tv_do_quarto.aumentar_canal(5)



            
