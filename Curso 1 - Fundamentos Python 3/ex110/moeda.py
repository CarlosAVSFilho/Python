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
    print("-"*33)
    print(' '*6, 'RESUMO DO VALOR')
    print("-"*33)
    print(f'Preço analisado:{moeda(n):>14}')
    print(f'Dobro do preço:{dobro(n):>16}')
    print(f'Metade do preço:{metade(n):>14}')
    print(f'{aumento}% de aumento:{aumentar(n, aumento):>15}')
    print(f'{decrescimo}% de redução:{diminuir(n, decrescimo):>15}')
    print("-"*33)


