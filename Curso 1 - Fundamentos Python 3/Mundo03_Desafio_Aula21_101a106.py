# Desafio 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas
# eleições.

# from datetime import datetime
# now = datetime.now()
#
#
# def voto(nascimento):
#     idade = now.year - nascimento
#     if 18 <= idade <= 65:
#         voto = 'Obrigatório'
#     elif 16 <= idade < 18 or idade > 65:
#         voto = 'Facultativo'
#     elif idade < 16:
#         voto = 'Negado'
#
#     return voto
#
#
# ano_nasc = int(input('Entre com o seu ano de nascimento: '))
#
# print(f'Para quem nasceu em {ano_nasc}, o voto é {voto(ano_nasc)}.')


# Desafio 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
# número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na
# tela o processo de cálculo de fatorial.


# def fatorial(n, show=True):
#     fat = 1
#     if show is True:
#         for c in range(n, 0, -1):
#             fat = fat*c
#             print(f'{c} x ' if c > 1 else f'{c}', end='')
#         print(f' = {fat}')
#
#     elif show is False:
#         for c in range(n, 0, -1):
#             fat = fat*c
#         print(fat)
#
#
# fatorial(7840, show=True)


# Desafio 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de
# um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
# não tenha sido informado corretamente.


# def ficha(jogador='<desconhecido>', gols=0):
#
#     print(f'O jogador {jogador} fez {gols} gol(s).')
#
#
# jogad = str(input('Jogador: '))
# gol = str(input('Gols: '))
#
# if gol.isnumeric():
#     gol = int(gol)
# else:
#     gol = 0
#
# if jogad == '':
#     ficha(gols=gol)
# else:
#     ficha(jogad, gol)


# Desafio 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n=leiaInt('Digite um n')


# def leiaInt(prompt=None):
#     resp = input(prompt)
#
#     if resp.isnumeric():
#         resp = int(resp)
#     else:
#         while resp.isnumeric() is False:
#             print('\033[0;31;0mERRO. Digite um número inteiro válido:\033[0m ')
#             resp = input(prompt)
#     return resp
#
#
# # Programa principal
# numero = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {numero}.')


# Desafio 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações: - Quantidade de notas, - A maior nota, - A menor nota, - A média da turma,
# - A situação (opcional). Adicione também as docstrings da função.


# def notas(*valores, sit=False):
#     """
#     --> Função para analisar notas e situações de vários alunos.
#     :param valores: uma ou mais notas dos alunos (aceita várias).
#     :param sit: valor opcional, indicando se deve ou não adicionar a situação.
#     :return: dicionário com várias informações sobre a situação da turma.
#     """
#
#     soma_notas = 0
#     for c in range(0, len(valores)):
#         soma_notas += valores[c]
#     media = soma_notas/len(valores)
#
#     if media >= 6:
#         situacao = 'BOA'
#     else:
#         situacao = 'RUIM'
#
#     boletim = {'Quantidade de notas': len(valores), 'Maior nota': max(valores),
#                'Menor nota': min(valores), 'Média da turma': media, 'Situação': situacao
#                }
#
#     if sit is True:
#         boletim = {'Quantidade de notas': len(valores), 'Maior nota': max(valores),
#                    'Menor nota': min(valores), 'Média da turma': media, 'Situação': situacao
#                    }
#     else:
#         boletim = {'Quantidade de notas': len(valores), 'Maior nota': max(valores),
#                    'Menor nota': min(valores), 'Média da turma': media,
#                    }
#
#     print(boletim)
#
#
# notas(8, 7, 6, 9, 5, sit=True)
#
# help(notas)


# Desafio 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
# vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Obs.: use cores.


def ajuda(funcao):
    from time import sleep
    print('\033[0;30;44m~'*41)
    print(f"   Acessando o manual do comando '{func}'")
    print('~'*41)
    sleep(1.5)
    print('\033[0;37;40m', end='')
    help(funcao)
    sleep(3)


while True:
    print('\033[0;30;42m~'*27)
    print('  SISTEMA DE AJUDA PyHELP')
    print('~'*27)
    func = input('\033[mFunção ou Biblioteca > ')

    if func == 'fim':
        print('\033[0;30;41m~' * 13)
        print('  ATÉ LOGO!')
        print('~' * 13)
        break

    ajuda(func)
