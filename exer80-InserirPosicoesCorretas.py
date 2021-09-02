lista = []

for x in range(0, 4+1):
    num = int(input("Informe um valor: "))
    if x == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print('-' * 30)
print(lista)
