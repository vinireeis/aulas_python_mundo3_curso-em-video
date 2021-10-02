alunos = {'nome': None,
          'media': None}
alunos['nome'] = input('Nome: ')
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] > 5.9:
    print(
        f'nome é igual a {alunos["nome"]}\nmedia é igual a {alunos["media"]}'
        f'\nsituação é igual a Aprovado')
else:
    print(
        f'nome é igual a {alunos["nome"]}\nmedia é igual a {alunos["media"]}'
        f'\nsituação é igual a Reprovado')
