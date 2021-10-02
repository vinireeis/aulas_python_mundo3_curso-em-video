dic = {'nome': None,
       'media': None}
dic['nome'] = input('Nome: ')
dic['media'] = float(input(f'Média de {dic["nome"]}: '))
if dic['media'] > 5.9:
    print(f'nome é igual a {dic["nome"]}\nmedia é igual a {dic["media"]}\nsituação é igual a Aprovado')
else:
    print(f'nome é igual a {dic["nome"]} media é igual a {dic["media"]}\nsituação é igual a Reprovado')

    
