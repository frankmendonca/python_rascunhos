A = input()


def mostra_sequencia(palavra):
    palavra = ''.join(sorted(palavra))

    for seq, letra in enumerate(palavra):
        print(letra)
        proxima_sequencia(palavra, letra, seq+1)


def proxima_sequencia(palavra, letra, seq):
    if seq < len(palavra):
        nova_letra = letra + palavra[seq]
        print(nova_letra)
        proxima_sequencia(palavra, nova_letra, seq+1)
        proxima_sequencia(palavra, letra, seq+1)

mostra_sequencia(A)
