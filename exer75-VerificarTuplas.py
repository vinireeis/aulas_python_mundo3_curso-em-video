tup = ()
for x in range(0, 4):
    num = (int(input('Digite um valor: ')),)
    tup += num

print(f'Os valores digitados foram: {num}')
print('-' * 60)
print(f'O número 9 apareceu {tup.count(9)} vezes')
print('-' * 60)
if 3 in tup:
    print(f'O valor 3 apareceu na {tup.index(3)+1}ª posição')
else:
    print('O valor 3 não foi informado')
print('-' * 60)
print('Os valores pares digitados foram: ', end='')
for x in tup:
    if x % 2 == 0:
        print(x, end=' ')
