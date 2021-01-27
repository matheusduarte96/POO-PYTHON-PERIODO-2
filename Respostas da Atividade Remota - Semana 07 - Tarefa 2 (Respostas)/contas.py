
class ContaCorrente():
    def __init__(self, numero, saldo):
        self.numero = numero
        self.__saldo = saldo

    @property
    def saldos(self):
        return self.__saldo

    @saldos.getter
    def saldos(self):
        return self.__saldo

    def creditar(self, valor):
        self.__saldo += valor
        return self.__saldo 

    def debitar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return self.__saldo 
        else:
            print("Valor acima do saldo permitido")
        
    def transferir(self, valor, conta):
        if self.__saldo > 0:
            self.__saldo -= valor
            conta.saldo = self.__saldo
        return self.__saldo
    
    def __str__(self):
        return f"CC: {self.numero}\nSaldo: R$ {self.__saldo:.2f}"
    
    
class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        self.taxa_juros = taxa_juros

    def renderJuros(self):
        self.saldo += self.saldo * (self.taxa_juros / 100)
        return self.saldo

    def __str__(self):
        return super().__str__() + "\n" + f"Saldo Atualizado após o rendimento de {self.taxa_juros}%: R$ {self.saldo:.2f}"


class ContaImposto(ContaCorrente):
    def __init__(self, numero, saldo, percentual_imposto):
        super().__init__(numero, saldo)
        self.percentual_imposto = percentual_imposto
        self.saldo = saldo

        
    def calcularImposto(self):
        self.saldo -= self.saldo * (self.percentual_imposto/100)
        return self.saldo

    def __str__(self):
        return super().__str__() + "\n" + f"Saldo Atualizado após o imposto de {self.percentual_imposto}%: R$ {self.saldo:.2f}"





