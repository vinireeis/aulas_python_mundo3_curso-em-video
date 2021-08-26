lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#   tuplas são representadas entre parenteses ('Hambúrguer', 'Suco', 'Pizza',
#  'Pudim') porém o python identifica que é uma tupla mesmo sem parenteses
print(lanche)

print(lanche[1])  # mostra o valor na posição 1

print(lanche[:2])  # vai do inicio até o 1, pois ele ignora o último

print(lanche[1:3])  # começa na posição 1 e vai até 2, ignorando o 3

print(len(lanche))

for contador in range(0, len(lanche)):
    print(f"Vou comer {lanche[contador]} que está na posição "
          f"{contador} ")
print('-' * 60)
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} que está na posição {pos}')
print('-' * 60)
for comida in lanche:
    print(f'Vou comer {comida}')
print('-' * 60)

print(sorted(lanche))  # ordenação da tupla porém não alterae pois é imutavel
print('-' * 60)

a = (2, 5, 4)
b = (5, 8, 2)
c = a + b

print(c)
print('-' * 60)
print(c.count(5))  # conta quantas vezes aparece o valor específicado no count
print('-' * 60)
print(c.index(8))  # index informa em qual posição está o valor específicado
print('-' * 60)
print(c.index(2))  # e só pega a primeira ocorrência
print('-' * 60)
#  é possível escolher onde o index começa a verificar da seguinte forma >>
print(c.index(2, 3))
#  assim o index começa a verificar a partir do elemento 3 e não 0
print('-' * 60)
pessoa = ('Vinicius', 27)
print(pessoa)
print('-' * 60)
del(pessoa)  # é possível apagar uma variável de tupla
#  print(pessoa) aqui já apresenta pessoa undefined ou seja foi excluido
print('-' * 60)
