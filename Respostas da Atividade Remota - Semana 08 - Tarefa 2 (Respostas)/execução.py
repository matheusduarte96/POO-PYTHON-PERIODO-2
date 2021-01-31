from funcionarios import *
class ControleDeFuncionarios:
    def __init__(self, total_pago=0):
        self._total_pago = total_pago
        self._funcionarios = []
        
    @property
    def funcionarios(self):
        return self._funcionarios
    
    def AdicionarFuncionario(self, funcionario):
        self._funcionarios.append(funcionario)

    def AtualizarSalario(self, percen_aumento):
        for i in self._funcionarios:
            if type(i):
                i.reajusteSalario(percen_aumento)
                   
    def RelatorioDePagamento(self):
        self._total_pago = 0
        for i in self._funcionarios:
            self._total_pago += i.getSalarioMensal()
            print(f"{i.nome:<15}R$ {i.getSalarioMensal()}")

    @property
    def total_pago(self):
        return self._total_pago                   

        
controle = ControleDeFuncionarios()
controle.AdicionarFuncionario(Funcionario('Matheus', '111111111-11', 1000.0))
controle.AdicionarFuncionario(Vendedor('Lucas', '333333333-33', 1000.0, 5000))
controle.AdicionarFuncionario(Vigilante('Augusto', '444444444-44', 1000.0, 20))
controle.AtualizarSalario(10)
controle.RelatorioDePagamento()
print(f"\nO total pago é: R$ {controle._total_pago:.2f}")
