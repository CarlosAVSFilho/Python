# Desafio 96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

# def area(larg, compr):
#     area = larg*compr
#     print(f'A área de largura {larg}m e comprimento {compr}m vale: {area}m².')
#
#
# largura = int(input('Largura [m]: '))
# comprimento = int(input('Comprimento [m]: '))
#
# area(largura, comprimento)



# Desafio 97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.


# def escreva(msg):
#     tam = len(msg) + 4
#     print(f'~'*tam)
#     print(f'  {msg}')
#     print(f'~'*tam)
#
#
# nome = str(input('Entre com um nome: '))
# escreva(nome)



# Desafio 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
# e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1. B) De 10 até 0, de 2 em 2. C) Uma contagem personalizada.

# from time import sleep
#
#
# def contador(initial, end, pace):
#     print('=-' * 20)
#     if pace == 0:
#         pace = 1
#     if initial > end:
#         pace = -pace
#         passo_end = end-1
#     elif initial < end:
#         passo_end = end+1
#     print(f'De {initial} a {end} de {pace} em {pace}:')
#     for i in range(initial, passo_end, pace):
#         print(f'{i}  ', end='')
#         sleep(0.5)
#     print('FIM!')
#
#
# contador(1, 10, 1)
# contador(10, 0, 2)
# print('=-' * 20)
# print('Agora é a sua vez de personalizar a contagem!')
#
# inicio = int(input('Início: '))
# fim = int(input('Fim: '))
# passo = abs(int(input('Passo: ')))
#
# contador(inicio, fim, passo)



# Desafio 99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# numeros = list()
#
# def maior(num): #caso fossem numeros sortidos, era só alterar num para * num, onde usa-se o acumulador de nmros
#     for i in range(0, len(num)):
#         if i == 0:
#             maior = num[i]
#         else:
#             if num[i] > maior:
#                 maior = num[i]
#
#     print(f'O maior número é {maior}.')
#
#
# while True:
#     numeros.append(int(input('Entre com um número: ')))
#
#     resp = str(input('Deseja add mais? [S/N]: '))
#
#     if resp in 'Nn':
#         break
#
# maior(numeros[:]) #poderia ser apenas os numeros sortidos



# Desafio 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A
# primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre to-
# dos os valores pares sorteados pela função anterior.

# from random import randint
#
# numeros = list()
#
# def sorteia(lista):
#     for i in range(0, 5):
#         num = randint(0, 99)
#         lista.append(num)
#     print(f'A lista sorteada foi: {lista}')
#
# def somaPar(lista):
#     soma = 0
#     for i in range(0, len(lista)):
#         if lista[i] % 2 == 0:
#             soma = soma + lista[i]
#     print(f'A soma dos números pares da lista é: {soma}')
#
#
# sorteia(numeros)
# somaPar(numeros)













