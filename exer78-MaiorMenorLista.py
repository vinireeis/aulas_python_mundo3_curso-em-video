lista = []
posA = []
posB = []
for x in range(0, 4+1):
    lista.append(int(input(f"Digite um novo valor para a posição {x}: ")))
x = max(lista)
y = min(lista)
print('-' * 50)
for pos, elem in enumerate(lista):
    if x == elem:
        posA.append(pos)
    elif y == elem:
        posB.append(pos)


print(f'O maior valor é {x} e está na posição {posA}')
print(f'O menor valor é {y} e está na posição {posB}')
