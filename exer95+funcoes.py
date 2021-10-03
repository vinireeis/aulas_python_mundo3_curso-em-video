def calc_area(base, altura):
    re = base * altura
    return f'{re}m²'


def escreva(msg):
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))


if __name__ == '__main__':
    x = calc_area(4.5, 8)
    print(x)

    escreva('Amo a larissinha')
