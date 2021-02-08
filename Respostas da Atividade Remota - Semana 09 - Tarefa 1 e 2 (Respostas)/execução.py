from seguros import *

class ControledeSeguros:
    def __init__(self, total_valores=0,total_premio=0):
        self._total_valores = total_valores
        self._total_premio = total_premio
        self._seguros = []

    @property
    def seguros(self):
        return self._seguros   

    def AdicionarSeguros(self, seguros):
        self._seguros.append(seguros)
        print("Seguro adicionado com sucesso!")

    def relatorio(self):
        sa = sv = 0
        for i in self._seguros:
            self._total_valores += i.calculaValor()
            self._total_premio += i.calculaPremio()
            if type(i) is SeguroAutomovel:
                sa += 1
            else:
                sv += 1         
            print(i)
            print()
        print(f"Seguro de Automóveis (Qtd): {sa}\nSeguro de Vida (Qtd): {sv}")

    def total_valores(self):
        return self._total_valores

    def total_premio(self):
        return self._total_premio


controle = ControledeSeguros()
cliente1 = Cliente("111111111-11", 'Jessica', 34)
cliente2 = Cliente("333333333-33", 'Matheus', 27)
cliente3 = Cliente("555555555-55", 'Lucas', 51)
controle.AdicionarSeguros(SeguroAutomovel(1, cliente1, 10, "Siena", 2019, 90000))
controle.AdicionarSeguros(SeguroAutomovel(2, cliente2, 11, "Gol", 2020, 75000))
controle.AdicionarSeguros(SeguroAutomovel(3, cliente3, 12, "Porsh", 2016, 150000))
controle.AdicionarSeguros(SeguroVida(1, cliente1, cliente3))
print()
controle.relatorio()
print(f"O Total do Valores: R$ {controle._total_valores:.2f}\nO Total dos Prêmios: R$ {controle._total_premio:.2f}")


