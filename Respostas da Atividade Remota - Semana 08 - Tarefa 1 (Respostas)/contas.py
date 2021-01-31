class ContaCorrente():
    def __init__(self, numero, saldo):
        self.numero = numero
        self._saldo = saldo

    def getSaldo(self):
        return self._saldo

    def creditar(self, valor):
        self._saldo += valor
        return self._saldo
        
    def debitar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return self._saldo 
        else:
            print("Valor acima do saldo permitido")
        
    def transferir(self, valor, conta):
        if self._saldo >= valor:
            self.debitar(valor)
            self.creditar(valor)
        return self._saldo   

    def __str__(self):
        return f"Saldo: {self._saldo}"
    
    
class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        self.taxa_juros = taxa_juros

    def renderJuros(self):
        return self._saldo + (self._saldo * (self.taxa_juros / 100))

    def getSaldo(self):
        return self._saldo + (self._saldo * (self.taxa_juros / 100))
    

class ContaImposto(ContaCorrente):
    def __init__(self, numero, saldo, percentual_imposto):
        super().__init__(numero, saldo)
        self.percentual_imposto = percentual_imposto

    def calcularImposto(self):
        return self._saldo - (self._saldo * (self.percentual_imposto/100))

