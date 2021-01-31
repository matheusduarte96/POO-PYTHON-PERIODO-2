from contas import *
class Banco:
    def __init__(self, saldo_total = 0):
        self._saldo_total = saldo_total
        self._contas = []

    @property
    def contas(self):
        return self._contas

    def CadastrarConta(self, conta):
        self._contas.append(conta)

    def Relatorio(self):
        c = p = 0
        for i in self._contas:
            self._saldo_total += i.getSaldo()
            if type(i) is ContaCorrente:
                c += 1 
            else:
                p += 1

        print(f"""Constam {len(self._contas)} contas cadastradas
            \nConta Corrente tem: {c}\nConta Poupança tem: {p}""")
                          
    @property
    def saldo_total(slef):
        return self._saldo_total
    
    
controle = Banco()
controle.CadastrarConta(ContaCorrente(1, 300))
controle.CadastrarConta(ContaPoupanca(2, 400.0, 2))
controle.CadastrarConta(ContaPoupanca(3, 900.0, 3))
controle.Relatorio()
print(f"\nO saldo total é: R$ {controle._saldo_total:.2f}")


    
