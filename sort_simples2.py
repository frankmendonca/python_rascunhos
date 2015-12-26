class ArvoreBinaria(object):

    def __init__(self, numeros, unique=False):
        self.numeros_tree = []
        self.numeros_list = numeros[:]
        self.unique = unique
        self.popular()

    def popular(self):
        for i in self.numeros_list:
            numero = int(i)
            self.incluir(self.numeros_tree, numero, 0)

    def incluir(self, celula_pai, numero, seq):

        if celula_pai:
            if self.unique and numero == celula_pai[0]:
                return
            elif numero <= celula_pai[0]:
                celula = celula_pai[1]
            else:
                celula = celula_pai[2]

            self.incluir(celula, numero, seq+1)
        else:
            celula = celula_pai
            celula.append(numero)
            celula.append([])
            celula.append([])

    def add_sort(self, lista, numeros):
        if numeros:
            self.add_sort(lista, numeros[1])
            lista.append(numeros[0])
            self.add_sort(lista, numeros[2])

    def to_tree(self):
        return self.numeros_tree

    def to_list_original(self):
        return self.numeros_list

    def to_list_orded(self):
        lista = []
        self.add_sort(lista, self.numeros_tree)
        return lista

    def show_tree(self):
        self.print_numeros(self.numeros_tree, 0)


# entrada = '7 21 -14 19 20 0 -1 0'
entrada = '1 7 21 -14 19 8 20 21 21 0 -1 0'
numeros = [int(x) for x in entrada.split()]

arvore = ArvoreBinaria(numeros)

print(arvore.to_tree())
print(arvore.to_list_original())
print(arvore.to_list_orded())

print()

arvore = ArvoreBinaria(numeros, unique=True)

print(arvore.to_tree())
print(arvore.to_list_original())
print(arvore.to_list_orded())
