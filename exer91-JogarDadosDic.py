from random import randint

jogadores = {}
for x in range(1, 4 + 1):
    jogadores['jogador' + str(x)] = randint(1, 6)
print(jogadores)
print()
# sorted(jogadores[], reverse=True)
for jogador in sorted(jogadores, key=jogadores.get, reverse=True):
    print(jogador, jogadores[jogador])
