# UTILIZAR IF, FOR E WHILE

# Desafio 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça
# a digitação novamente até ter um valor correto.

# sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()[0]
# while sexo != 'M' and sexo != 'F':
#     sexo = str(input('Entre com um valor válido [M/F]: ')).strip().upper()[0]
#
# if sexo == 'M':
#     print('Você é do sexo masculino.')
# elif sexo == 'F':
#     print('Você é do sexo feminino.')



# Desafio 58: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# import random #pode ser from random import randint aí depois usa apenas randint(1,10)
#
# palpite = int(input('Entre com um número entre 0 e 10: '))
# pc = random.randint(0, 10)
# soma = 1
#
# while palpite != pc:
#     palpite = int(input('ERROU! Entre com um número entre 0 e 10: '))
#     soma += 1
#
# print(f'ACERTOU!! Você precisou de {soma} jogadas para vencer o PC!')



# Desafio 59: Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar,  [2]multiplicar, [3]maior, [4]novos números, [5]sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.

# n1 = int(input('Entre com um número: '))
# n2 = int(input('Entre com mais um número: '))
# comando = 1
#
# while comando != 5:
#     print('-='*20)
#     print('MENU:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
#     comando = int(input(''))
#
#     if comando == 1:
#         soma = n1 + n2
#         print(f'{n1} + {n2} = {soma}')
#     elif comando == 2:
#         multiplicacao = n1*n2
#         print(f'{n1} x {n2} = {multiplicacao}')
#     elif comando == 3:
#         if n1 > n2:
#             print(f'O maior número entre {n1} e {n2} é: {n1}')
#         elif n1 < n2:
#             print(f'O maior número entre {n1} e {n2} é: {n2}')
#         else:
#             print(f'Os dois números são iguais.')
#     elif comando == 4:
#         n1 = int(input('Entre com um número novo: '))
#         n2 = int(input('Entre com mais um número novo: '))
#     elif comando > 4 and comando != 5:
#         print('Entre com um comando de [1] a [5].')
#
# print('Volte sempre.')



# Desafio 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.

# n = int(input('Entre com um número: '))
# fatorial = 1
#
# print(f'{n}! = ', end='')
# for c in range(n, 1, -1):
#     fatorial = fatorial*c
#
# while n >= 1:
#     print(n, 'x ' if n > 1 else '= ', end='')
#     n = n - 1
# print(f'{fatorial}')


# Desafio 61: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura while.

# termo = float(input('Entre com o primeiro termo da P.A: '))
# razao = float(input('Entre com a razão da P.A: '))
#
# cont = 1
# print(termo, end=' ')
# while cont < 10:
#     print(termo+(razao*cont), end=' ')
#     cont = cont+1



# Desafio 62: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
# encerra quando ele disser que quer mostrar 0 termos.

# termo = int(input('Entre com o primeiro termo da P.A: '))
# razao = int(input('Entre com a razão da P.A: '))
#
# cont = 1
# qnt_termos = 10
#
# while qnt_termos != 0:
#     print(f'Os {qnt_termos} primeiros termos desta P.A são:')
#     print(termo, end=' ')
#     while cont < qnt_termos:
#         print(termo+(razao*cont), end=' ')
#         cont = cont+1
#     print('')
#     qnt_termos = int(input('Entre com a quantidade de termos você deseja exibir (0 para encerrar): '))
#     cont = 1
# print('Programa encerrado.')



# Desafio 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# sequência de fibonacci.

# elemento = int(input('Quantos elementos quer mostrar na sua sequência? '))
# t1 = 0
# t2 = 1
#
# print(f'Os {elemento} primeiros elementos são:')
# print(f'{t1} -> {t2} ->', end=' ')
#
# cont = 3
# t_ultimo = t2
# t_penultimo = t1
#
# while cont <= elemento:
#     t_atual = t_ultimo + t_penultimo
#
#     print(f'{t_atual} ->' if cont < elemento else f'{t_atual}', end=' ')
#
#     t_penultimo = t_ultimo
#     t_ultimo = t_atual
#     cont = cont+1



# Desafio 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando a flag).

# numero = 0
# somatoria = 0
# cont = 0
#
# while numero != 999:
#     numero = int(input('Entre com um número inteiro (999 para sair): '))
#     if numero != 999:
#         somatoria = somatoria+numero
#         cont = cont+1
# print(f'A somatória dos {cont} números digitados é: {somatoria}')



# Desafio 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

# flag = 'S'
# numero = int(input('Entre com um número inteiro: '))
# maior = numero
# menor = numero
# somatorio = numero
# cont = 0
#
# while flag != 'N':
#     numero = int(input('Entre com um número inteiro: '))
#     flag = str(input('Deseja continuar adicionando números? [S/N]: ')).strip().upper()
#     if numero > maior:
#         maior = numero
#     elif numero < menor:
#         menor = numero
#     somatorio = somatorio + numero
#     cont = cont+1
#
# print(f'A média dos valores digitados é:{somatorio/(cont+1)}')
# print(f'O maior número digitado é: {maior}')
# print(f'O menor número digitado é: {menor}')
