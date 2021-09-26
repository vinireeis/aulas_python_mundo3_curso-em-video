from random import randint

qtd_j = int(input('QUANTOS JOGOS DESEJA QUE EU SORTEIE? '))
lista_numeros = []
todos_jogos = []
for jogos in range(1, qtd_j + 1):
    while True:
        n = randint(1, 60)
        if n not in lista_numeros:
            lista_numeros.append(n)
        if len(lista_numeros) < 6:
            pass
        else:
            break
    print(f' Jogo {jogos}: {sorted(lista_numeros)}')
    lista_numeros = []
        