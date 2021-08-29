palavras = ('aprender', 'programar', 'estudar', 'praticar', 'python',
            'programador', 'trabalhar', 'mercado', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra in 'AaeEiIoOuU':
            print(letra, end=' ')
