temp = []
p = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ').capitalize()))
    temp.append(float(input('Peso: ')))
    if len(p) == 0:
        maior = menor = temp[1]  # o valor do peso está sendo adicionado
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    p.append(temp[:])
    temp.clear()
    resposta = str(input('Deseja continuar? [S/N]')).upper()
    if resposta == 'N':
        break

print(p)
print('-' * 30)
print(f'Foram cadastrados {len(p)} pessoas.')
print(f'O maior peso foi {maior:.2f}kg')
for pessoa in p:
    if p[1] == maior:
        print(p[0])
print(f'O menor peso foi {menor:.2f}')
