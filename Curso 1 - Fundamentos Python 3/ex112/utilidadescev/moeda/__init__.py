def metade(n, formatacao=True):
    if formatacao is True:
        return moeda(n/2)
    else:
        return n/2


def dobro(n, formatacao=True):
    if formatacao is True:
        return moeda(n*2)
    else:
        return n*2


def aumentar(n, aumento, formatacao=True):
    if formatacao is True:
        return moeda((1+aumento/100)*n)
    else:
        return (1+aumento/100)*n


def diminuir(n, decrescimo, formatacao=True):
    if formatacao is True:
        return moeda((1-decrescimo/100)*n)
    else:
        return (1-decrescimo/100)*n


def moeda(n):
    n_string = ('%.2f' % n).replace('.', ',')
    return 'R$' + n_string


def resumo(n, aumento, decrescimo):
    print("-"*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print("-"*30)
    print(f'{"Preço analisado:":<15}', end='')
    print(f'{moeda(n):>14}')

    print(f'{"Dobro do preço:":<15}', end='')
    print(f'{dobro(n):>15}')

    print(f'{"Metade do preço:":<15}', end='')
    print(f'{metade(n):>14}')

    aumt = f'{aumento}% de aumento:'
    print(f'{aumt:<15}', end='')
    print(f'{aumentar(n, aumento):>15}')

    rdco = f'{decrescimo}% de redução:'
    print(f'{rdco:<15}', end='')
    print(f'{diminuir(n, decrescimo):>15}')
    print("-"*30)

