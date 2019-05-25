# Desafio 84: Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final,
# mostre: A)Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as
# pessoas mais leves.

# dados = list()
# galera = list()
#
#
# while True:
#     dados.append(str(input('Nome: ')))
#     dados.append(float(input('Peso: ')))
#     galera.append(dados[:])
#     dados.clear()
#
#     flag = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
#
#     while flag not in 'SN':
#         flag = str(input('Digite S para continuar ou N para parar: '))
#
#     if flag in 'N':
#         break
#
# i = 0
# for peso in galera:
#     if i == 0:
#         magro = peso[1]
#         gordo = peso[1]
#     else:
#         if peso[1] > gordo:
#             gordo = peso[1]
#         elif peso[1] < magro:
#             magro = peso[1]
#     i = i+1
#
# print(galera)
#
# print(f'No total você cadastrou {len(galera)} pessoas.')
#
# print(f'O menor peso foi de {magro:.1f}kg. Peso de: ', end='')
# for p in galera:
#     if p[1] == magro:
#         print(f'[{p[0]}] ', end='')
#
# print(f'\nO maior peso foi de {gordo:.1f}kg. Peso de: ', end='')
# for p in galera:
#     if p[1] == gordo:
#         print(f'[{p[0]}] ', end='')



# Desafio 85: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# matenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# numeros = [[], []]
# i = 0
#
# while i <= 6:
#     valor = int(input(f'Entre com o {i+1}º número: '))
#
#     if valor % 2 == 0:
#         numeros[0].append(valor)
#     else:
#         numeros[1].append(valor)
#
#     i += 1
#
#
# print(f'Números digitados: {numeros}')
# print(f'Números pares: {sorted(numeros[0])}')
# print(f'Números ímpares: {sorted(numeros[1])}')



# Desafio 86: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# for l in range(0, 3):
#         for c in range(0, 3):
#             matriz[l][c] = (int(input(f'Entre com o valor [{l},{c}]: ')))
#
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print('')



# Desafio 87: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma
# dos valores da terceira coluna. C) O maior valor da segunda linha.

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# pares = soma_coluna = 0
#
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = (int(input(f'Entre com o valor [{l},{c}]: ')))
#
#         if matriz[l][c] % 2 == 0:
#             pares = pares + matriz[l][c]
#
#         if c == 2: #terceira coluna
#             soma_coluna = soma_coluna + matriz[l][c]
#
#         if l == 1: #maior elemento da segunda linha
#             if c == 0:
#                 maior_elemento = matriz[l][c]
#             else:
#                 if matriz[l][c] > maior_elemento:
#                     maior_elemento = matriz[l][c]
#
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print('')
#
# print(f'A - Soma dos pares: {pares}')
# print(f'B - Soma da 3ª coluna: {soma_coluna}')
# print(f'C - Maior elemento da 2ª linha: {maior_elemento}')



# Desafio 88: Faça um programa que ajude um jogador da MEGASENA a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# from time import sleep
# from random import randint
#
# jogo = []
# megasena = []
# qnt_jogos = int(input('Entre com a quantidade de jogos: '))
#
# for i in range(0, qnt_jogos):
#     print(f'Processando jogo {i+1}...')
#
#     for c in range(1, 7):
#         valor = randint(1, 60)
#         while jogo.count(valor) >= 1:
#             valor = randint(1, 60)
#         jogo.append(valor)
#
#     megasena.append(jogo[:])
#     jogo.clear()
#     sleep(0.4)
# print(f'Finalizado!')
#
# for i in range(0, len(megasena)):
#     print(f'Jogo {i+1}: {sorted(megasena[i])}')



# Desafio 89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No
# final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

# nome = list()
# notas = list()
# lista = list()
# boletim = list()
#
# while True:
#     nome.append(str(input('Nome: ')))
#     notas.append(float(input('Nota 1: ')))
#     notas.append(float(input('Nota 2: ')))
#
#     lista.append(nome[:])
#     lista.append(notas[:])
#     nome.clear()
#     notas.clear()
#
#     boletim.append(lista[:])
#     lista.clear()
#     resp = str(input('Desejar continuar [S/N]?: ')).strip().upper()[0]
#
#     if resp in 'Nn':
#         break
#
# print('=-=-=- Média dos alunos -=-=-=')
# print(f'{"No":<4}{"Nome":<45}{"Média":>10}')
#
# for i in range(0, len(boletim)):
#     print(f'{i:<4}{boletim[i][0][0]:<45}{((boletim[i][1][0] + boletim[i][1][1])/2):>10.1f}')
#
# while True:
#     nmr_aluno = int(input('Deseja ver a nota de qual aluno? (999 pra sair): '))
#     while nmr_aluno >= len(boletim) and nmr_aluno != 999:
#         nmr_aluno = int(input('Entre com um nº de aluno válido ou digite 999 pra sair: '))
#     if nmr_aluno == 999:
#         break
#
#     print(f'Notas do aluno nº {nmr_aluno}({boletim[nmr_aluno][0][0]}):')
#     print(boletim[nmr_aluno][1])
#     print('-'*30)

