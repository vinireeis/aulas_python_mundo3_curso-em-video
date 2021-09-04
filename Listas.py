lista = [2, 5, 9, 1]
print(lista)
lista[2] = 10  # alterando um elemento da lista
print(lista)
lista.append(3)  # adicionando um elemento no fim da lista
print(lista)
lista.sort(reverse=True)  # ordenação decrescente
print(lista)
lista.sort()
print(lista)  # ordenação crescente
lista.insert(2, 0)
# inserindo um valor num index específico (2 é o index, 0 é o valor)
print(lista)
lista.pop(2)  # removendo um elemento pelo index
print(lista)
lista.remove(5)  # remove o primeiro '5' da lista
print(lista)
print(len(lista))  # verificar o tamanho da lista
print('-' * 60)  # criando cópia e ligação entre lista
a = [2, 3, 7, 1]
b = a  # cria uma ligação entre as listas, fazendo com que ao alterar uma>
#  ambas sejam alteradas
b[2] = 9  # alterando o elemento da posição 2
print('Listas interligadas')
print(f'lista A: {a}, \nlista B:{b} ')
''' agora se fizer da seguinte maneira
C = [2, 3, 7, 1]
D = C[:]
Você estará fazendo uma cópia da lista, sem ligação, do qual ao alterar um
elemento da lista B não afetará nenhum elemento da lista A
'''
print('-' * 60)
print('Cópia de Lista')
c = [2, 3, 7, 1]
d = c[:]
d[1] = 15
print(f'lista C: {c}, \nlista D: {d} ')

print(lista.index(1))
print(lista)
print('-' * 60)
print('-' * 60)
galera = [['João', 19], ['Ana', 25], ['Larissa', 22], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print('-' * 60)
print(galera[0])
print('-' * 60)
print(galera[2][1])
print('-' * 60)
for dados in galera:
    print(dados)
print('-' * 60)
# se quiser só os nomes ou só as idades
for dados in galera:
    print(dados[0], end=' ')  # ou dados[1]
print('')
print('-' * 60)

