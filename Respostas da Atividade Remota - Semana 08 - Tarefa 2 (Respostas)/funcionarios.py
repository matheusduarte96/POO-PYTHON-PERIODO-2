class Funcionario():
    def __init__(self, nome, cpf, salarioBase):
        self.__nome = nome
        self._cpf = cpf
        self._salarioBase = salarioBase

    def reajusteSalario(self, percentual):
        self._salarioBase += (self._salarioBase *(percentual / 100))
        return self._salarioBase

    @property
    def nome(self):
        return self.__nome

    def getSalarioMensal(self):
        return self._salarioBase

    def __str__(self):
        return f"Salário Base: {self._salarioBase}"


class Vendedor(Funcionario):
    def __init__(self, nome, cpf, salarioBase, valor_vendas_mes):
        super().__init__(nome, cpf, salarioBase)
        self.valor_vendas_mes = valor_vendas_mes
   
    def reajusteSalario(self, percentual):
        self._salarioBase += (self._salarioBase *(percentual / 100))
        return self._salarioBase

    def getSalarioMensal(self):
        return self._salarioBase + (self.valor_vendas_mes * 0.1)
    

class Vigilante(Funcionario):
    def __init__(self, nome, cpf, salarioBase, valor_adicional_noturno):
        super().__init__(nome, cpf, salarioBase)
        self.valor_adicional_noturno = valor_adicional_noturno    
   
    def reajusteSalario(self, percentual):
        self._salarioBase += (self._salarioBase *(percentual / 100))
        self.valor_adicional_noturno += (self.valor_adicional_noturno *(percentual / 100))
        return self._salarioBase

    def getSalarioMensal(self):
        return self._salarioBase + (self.valor_adicional_noturno  * 12)
    
