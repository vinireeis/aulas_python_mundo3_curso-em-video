def calc_area(base, altura):
    re = base * altura
    return f'{re}m²'


def escreva(msg):
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))


def contagem(inicial, final, pulo):
    for x in range(1, 10+1):
        print(x, end=' ')
    print()
    for x in range(10, 0, -2):
        print(x, end=' ')
    print()
    for x in range(inicial, final, pulo):
        print(x, end=' ')


if __name__ == '__main__':
    x = calc_area(4.5, 8)
    print(x)

    escreva('Amo a larissinha')

    contagem(7, 0, -2)
