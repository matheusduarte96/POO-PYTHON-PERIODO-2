from contas import *

contacorrente1 = ContaCorrente(1, 4000)
contapoupanca1 = ContaPoupanca(1, 4000, 4)
contacorrente1.creditar(200)
contacorrente1.debitar(300)
contacorrente1.transferir(200, contapoupanca1)
contapoupanca1.renderJuros()
contaimposto = ContaImposto(1, contapoupanca1._saldo, 5)
contaimposto.calcularImposto()
print(contacorrente1)
print()
print(contapoupanca1)
print()
print(contaimposto)
print('-='*30)
contacorrente2 = ContaCorrente(2, 5647)
contapoupanca2 = ContaPoupanca(2, 5647, 3.5)
contacorrente2.creditar(300)
contacorrente2.debitar(1580)
contacorrente2.transferir(450, contapoupanca2)
contapoupanca2.renderJuros()
contaimposto = ContaImposto(2, contapoupanca2._saldo, 2.5)
contaimposto.calcularImposto()
print(contacorrente2)
print()
print(contapoupanca2)
print()
print(contaimposto)
