class SalarioComAumento(object):
    """ Salário com Aumento (class Pai) """

    @staticmethod
    def calcular(salario):
        if 0 <= salario <= 400.00:
            return _SalarioComAumento15(salario)
        elif 400.01 <= salario <= 800.00:
            return _SalarioComAumento12(salario)
        elif 800.01 <= salario <= 1200.00:
            return _SalarioComAumento10(salario)
        elif 1200.01 <= salario <= 2000.00:
            return _SalarioComAumento7(salario)
        else:
            return _SalarioComAumento4(salario)

    def __init__(self, salario):
        self.__salario_antigo = salario
        self.__salario_novo = salario * (1 + self.percentual_reajuste())

    def salario(self):
        return self.__salario_novo

    def percentual_reajuste(self):
        return 0.00

    def reajuste_ganho(self):
        return self.__salario_novo - self.__salario_antigo


class _SalarioComAumento15(SalarioComAumento):
    """ Salário com Aumento de 15 % """
    def percentual_reajuste(self):
        return 0.15


class _SalarioComAumento12(SalarioComAumento):
    """ Salário com Aumento de 12 % """
    def percentual_reajuste(self):
        return 0.12


class _SalarioComAumento10(SalarioComAumento):
    """ Salário com Aumento de 10 % """
    def percentual_reajuste(self):
        return 0.10


class _SalarioComAumento7(SalarioComAumento):
    """ Salário com Aumento de 7 % """
    def percentual_reajuste(self):
        return 0.07


class _SalarioComAumento4(SalarioComAumento):
    """ Salário com Aumento de 4 % """
    def percentual_reajuste(self):
        return 0.04
