tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
         'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

x = int(input('Informe um número de 0 a 20: '))

while x < 0 or x > 20:
    x = int(input('Você digitou um valor incorreto. Informe um novo número de'
                  ' 0 a 20: '))
print(f'Você digitou o número {tupla[x]}.')
