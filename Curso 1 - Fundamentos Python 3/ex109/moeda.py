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


