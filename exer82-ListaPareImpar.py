lista = []
par = []
ímpar = []

while True:
    lista.append(int(input('Informe um valor: ')))
    r = input('Quer continuar? [S/N]').upper()
    if r == 'N':
        break

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        ímpar.append(i)

print(f'Esta é a lista completa: {lista}')
print('-' * 35)
print(f'Esta é a lista de números pares: {par}')
print('-' * 35)
print(f'Esta é a lista de números ímpares: {ímpar}')
