class ContaCorrente():
    def __init__(self, numero, saldo):
        self.numero = numero
        self._saldo = saldo

    @property
    def saldo(self):...

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
        return f"CC: {self.numero}\nSaldo: R$ {self._saldo:.2f}"
    
    
class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        self.taxa_juros = taxa_juros

    def renderJuros(self):
        self._saldo += self._saldo * (self.taxa_juros / 100)
        return self._saldo

    def __str__(self):
        return super().__str__() + "\n" + f"Saldo Atualizado após o rendimento de {self.taxa_juros}%: R$ {self._saldo:.2f}"


class ContaImposto(ContaCorrente):
    def __init__(self, numero, saldo, percentual_imposto):
        super().__init__(numero, saldo)
        self.percentual_imposto = percentual_imposto
        
    def calcularImposto(self):
        self._saldo -= self._saldo * (self.percentual_imposto/100)
        return self._saldo


    def __str__(self):
        return super().__str__() + "\n" + f"Saldo Atualizado após o imposto de {self.percentual_imposto}%: R$ {self._saldo:.2f}"





