br = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo',
      'Corinthians', 'Atlético-GO', 'Ceará', 'Athletico-PR', 'Internacional',
      'Santos', 'São Paulo', 'Juventude', 'Cuiabá', 'Bahia', 'Fluminense',
      'Grêmio', 'Sport', 'América-MG', 'Chapecoense')

print(br)
print('-' * 60)
print(br[0:5])
print('-' * 60)
print(br[16:20])  # tambem pode ser feito da forma abaixo
print(br[-4:])  # reprenta do quarto de trás para frente até o final
print('-' * 60)
print(sorted(br))
print('-' * 60)
print(' O time da Chapecoense está na ' + str(br.index('Chapecoense') + 1) +
      'ª posição')
