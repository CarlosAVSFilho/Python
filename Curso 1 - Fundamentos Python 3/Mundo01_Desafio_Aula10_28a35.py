# print("""Desafio 28: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se
# o usuário venceu ou perdeu..""")
# print('')
# import random
# valor_pc = random.randint(0, 5)
# valor_humano = int(input('Advinhe o número inteiro que o pc escolheu entre 0 e 5: '))
#
# if valor_pc == valor_humano:
#     print('ACERTÔ MIZERAVI')
# else:
#     print('ERROUUUU')


# print("""Desafio 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar os 80km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km/h acima do limite""")
#
# velocidade_carro = float(input('Entre com a velocidade do carro: '))
#
# if velocidade_carro > 80:
#     multa = (velocidade_carro - 80)*7
#     print('A sua velocidade foi de {}km/h, portanto sua multa será de R${:.2f}'.format(velocidade_carro, multa))
# else:
#     print('Você não foi multado.')


# print('Desafio 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR')
# numero = int(input('Entre com um número inteiro: '))
#
# par_impar = numero % 2
#
# if par_impar == 0:
#     print('O número digitado ({}) é par.'.format(numero))
# else:
#     print('O númeero digitado ({}) é impar.'.format(numero))


# print("""Desafio 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
# cobrando R$ 0,50 por km para viagens até 200km e R$ 0,45 para viagens mais longas""")
#
# distancia_viagem = int(input('Qual a distância da sua viagem? '))
#
# if distancia_viagem <= 200:
#     custo = 0.50*distancia_viagem
# else:
#     custo = 0.45*distancia_viagem
#
# print('O valor da sua viagem foi de R${:.2f}'.format(custo))
#
# #Uma alternativa usando if simplified: custo = distancia_viagem * 0.50 if distancia_viagem <= 200 else distancia*0.45


# print('Desafio 32: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO')
#
# ano = int(input('Entre com um ano: '))
#
# if ((ano % 4) == 0 and (ano % 100) > 0) or ((ano % 100) == 0 and (ano % 400) == 0):
#     print('O ano {} É um ano bissexto.'.format(ano))
# elif (ano % 4) > 0 or ((ano % 100) == 0 and (ano % 400) > 0):
#     print('O ano {} NÃO É um ano bissexto.'.format(ano))


# print('Desafio 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor')
#
# n1 = float(input('Entre com o primeiro número: '))
# n2 = float(input('Entre com o segundo número: '))
# n3 = float(input('Entre com o terceiro número: '))
#
# if (n1 != n2) and (n1 != n3):
#     if n1 > n2 and n1 > n3:
#         print('O maior número é {}'.format(n1))
#     elif n2 > n1 and n2 > n3:
#         print('O maior número é {}'.format(n2))
#     elif n3 > n1 and n3 > n2:
#         print('O maior número é {}'.format(n3))
#
#     if n1 < n2 and n1 < n3:
#         print('O menor número é {}'.format(n1))
#     elif n2 < n1 and n2 < n3:
#         print('O menor número é {}'.format(n2))
#     elif n3 < n1 and n3 < n2:
#         print('O menor número é {}'.format(n3))
# else:
#     print('Digite 3 valores diferentes.')


# print("""Desafio 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor de aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os  inferiores ou iguais, o aumento é de 15%""")
#
# salario = float(input('Entre com o valor do salário: '))
#
# if salario <= 1250:
#     print('Você recebeu aumento de 15%. Seu novo salário será de R${:.2f}.'.format(salario*1.15))
# else:
#     print('Você recebeu aumento de 10%. Seu novo salário será de R${:.2f}.'.format(salario*1.1))


# print("""Desafio 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo""")
# a = float(input('Entre com o valor da 1ª aresta: '))
# b = float(input('Entre com o valor da 2ª aresta: '))
# c = float(input('Entre com o valor da 3ª aresta: '))
#
# if ((abs(b-c) < a) and (a < b+c)) and ((abs(a-c) < b) and (b < a+c)) and ((abs(a-b) < c) and (c < a+b)):
#     print('{}, {} e {} podem formar um triângulo'.format(a, b, c))
# else:
#     print('Os lados não formam um triângulo')
