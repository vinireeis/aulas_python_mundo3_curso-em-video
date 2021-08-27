from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10))  # também pode ser sorteado com um for
print('-' * 60)
print(f'Os números sorteados foram: {n}')
print('-' * 60)
print(f'O maior valor é: {max(n)}')
print('-' * 60)
print(f'O menor valor é: {min(n)}')
print('-' * 60)
