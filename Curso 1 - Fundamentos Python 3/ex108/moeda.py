def metade(n):
    return n/2


def dobro(n):
    return n*2


def aumentar(n, aumento):
    return (1+aumento/100)*n


def diminuir(n, decrescimo):
    return (1-decrescimo/100)*n


def moeda(n):
    n_string = ('%.2f' % n).replace('.', ',')
    return 'R$' + n_string

