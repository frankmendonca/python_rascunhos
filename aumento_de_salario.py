from calc_salario import SalarioComAumento

# salario = float(input())

for salario in (400.00, 440.01, 900.00, 1200.01, 3000.00):
    novo_salario = SalarioComAumento.calcular(salario)

    print('Salario antigo: %8.2f R$' % salario)
    print('Novo salario  : %8.2f R$' % novo_salario.salario())
    print('Reajuste ganho: %8.2f R$' % novo_salario.reajuste_ganho())
    print('Em percentual : %8.0f %%' % (novo_salario.percentual_reajuste() * 100))
    print()
