lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print("O valor não foi adicionado pois já existe")
    resp = input('Deseja continuar? [S/N]: ').upper()
    if resp == 'N':
        break
print(sorted(lista))
