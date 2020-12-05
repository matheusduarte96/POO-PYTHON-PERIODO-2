#Questão 01 e 02

"""3. Implemente em python o objeto que você escolheu no exercício da 1ª semana,
agora utilizando o conceito de construtores.
Crie pelo menos 2 objetos e teste seus métodos."""

class notebook:
    #Atributos
    nome = None
    ano = None
    tela = None
    processador = None
    cor = None
    abas = 0
    ligado=False

    #Construtor para a classe carro.
    def __init__(self, nome, cor, ligado, processador, ano, tela):
        self.nome = nome
        self.cor = cor
        self.ligado = ligado
        self.processador = processador
        self.ano = ano
        self.tela = tela

    #Métodos 
    def ligar(self):
        ligado = self.ligado
        if self.ligado == True:
            print(f"O notebook {self.nome} está ligado.")
        else:
            notebook.desligar(self, ligado)

    def processo(self, abas):
        self.abas = abas
        if self.ligado == True:
            if self.abas > 15:
                print("Processador sobrecarregado, pc travando.")
                print("Por favor, você precisa fechar algumas abas.\n")
            else:
                print(f"O processador {self.processador} está em ótimo funcionamento.\n")
                
        print("INFORMAÇÕES DO NOTEBOOK")
        print(".."*15)
        print(f"""Nome: {self.nome};
Tela: {self.tela} polegadas;
Processador: {self.processador};
Cor: {self.cor};
Ano: {self.ano}.\n""")

    def desligar(self, ligado):
        if self.ligado == False:
            print(f"O notebook {self.nome} está desligado.")

#Criação dos objetos     
#Asus
meu_notebook1 = notebook("Asus","Cinza",True, "i5", 2018, 14)
meu_notebook1.ligar()
meu_notebook1.processo(12)

print("-="*37)

#Positivo
meu_notebook2 = notebook("Positivo","Preto",True, "i3", 2020, 15.6)
meu_notebook2.ligar()
meu_notebook2.processo(17)


