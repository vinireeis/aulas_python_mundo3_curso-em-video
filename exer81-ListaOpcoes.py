lista = []
while True:
    lista.append(int(input("Informe um valor: ")))
    resp = input("Deseja continuar? [S/N]: ").upper()
    if resp == 'N':
        break
print('-' * 40)
print(f'Foram digitados {len(lista)} números.')
print('-' * 40)
print(sorted(lista, reverse=True))
print('-' * 40)
if 5 in lista:
    print(f'Existe o número 5 na lista e está na'
          f'posição {lista.index(5)}')
else:
    print('Não existe o número 5 na lista.')
