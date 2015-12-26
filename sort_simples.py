#entrada = input()
entrada = '7 21 -14 19 20 0 -1 0'
numeros = []


def incluir(numero, numeros, seq):

    if len(numeros) > 0:
        if numero == numeros[0]:
            return None
        elif numero < numeros[0]:
            celula = numeros[1]
        else:
            celula = numeros[2]

        incluir(numero, celula, seq+1)
    else:
        celula = numeros
        celula.append(numero)
        celula.append([])
        celula.append([])

    #print('seq', seq, 'numeros', numeros)

for i in entrada.split():
    numero = int(i)
    incluir(numero, numeros, 0)

print(numeros)


def print_left(numeros):
    if len(numeros) > 0:
        print_left(numeros[1])
        print(numeros[0])
        print_right(numeros[2])

def print_right(numeros):
    if len(numeros) > 0:
        print_right(numeros[2])
        print(numeros[0])

def print_numeros(numeros):
    print_left(numeros[1])
    print(numeros[0])
    print_left(numeros[2])

print_numeros(numeros)
