lista = []
resp = 'S'
while resp == 'S':
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print("O valor não foi adicionado pois já existe\n")
    resp = input('Deseja continuar? [S/N]: ').upper()
    if resp == 'N':
        break
print(sorted(lista))
