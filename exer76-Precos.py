tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Mochila', 119.90)
print('-' * 38)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 38)
for item in range(0, len(tupla)):
    if item % 2 == 0:
        print(f'{tupla[item]:.<30}', end='')
    else:
        print(f'R${tupla[item]:>6.2f}')
