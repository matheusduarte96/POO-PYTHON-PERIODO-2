class Banco():
    def __init__(self, nome, valor_total=0):
        self.__nome = nome
        self.__contas = []
        self.valor_total = valor_total

    @property
    def nome(self):
        return self.__nome

    @nome.getter
    def nome(self):
        return self.__nome
    
    @property
    def contas(self):
        return self.__contas
    
    def Adicionar(self, conta):
        self.__contas.append(conta)
        
    def Remover(self):
        for i in self.__contas:
            if i.saldo == 0:
               del i
               print("\nConta removida com sucesso")
            else:
                print(i)
            
    def valorTotal(self):
        for i in self.__contas:
            self.valor_total += i.saldo
            

    def __str__(self):
        return f"\nBanco: {self.__nome}\nSaldo Total: R$ {self.valor_total:.2f}"


class Conta():
    def __init__(self, numero, titular, saldo=0):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = titular

    @property
    def numero(self):
        return self.__numero

    @numero.getter
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @saldo.getter
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    def Depositar(self, valor):
        self.__saldo += valor
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso na conta {self.__numero}")
        return self.__saldo

    def Sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso na conta {self.__numero}.")
        else:
            print(f"Saque na conta {self.__numero} com valor acima do saldo. Operação não realizada.")
        return self.__saldo

 
    def __str__(self):
        return f"\nNúmero da CC: {self.__numero}\nSaldo da Conta: R$ {self.__saldo:.2f}"


class Cliente():
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.getter
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @nome.getter
    def nome(self):
        return self.__nome

    def __str__(self):
        return f"\nNome: {self.__nome}\nCPF: {self.__cpf}"

