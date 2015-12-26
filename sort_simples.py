#entrada = input()
entrada = '7 21 -14 19 20 0 -1 0'
numeros = []


def incluir(celula_pai, numero, seq):

    if celula_pai:
        if numero == celula_pai[0]:
            return
        elif numero < celula_pai[0]:
            celula = celula_pai[1]
        else:
            celula = celula_pai[2]

        incluir(celula, numero, seq+1)
    else:
        celula = celula_pai
        celula.append(numero)
        celula.append([])
        celula.append([])

    #print('seq', seq, 'numeros', numeros)

for i in entrada.split():
    numero = int(i)
    incluir(numeros, numero, 0)

print(numeros)


def print_numeros(numeros):
    if numeros:
        print_numeros(numeros[1])
        print(numeros[0])
        print_numeros(numeros[2])

print_numeros(numeros)
