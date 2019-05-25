# print("""Desafio 22: Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras
# maiúsculas, o nome com todas as letras minúsculas, quantas letras no total (sem considerar espaços), quantas letras
# tem o primeiro nome.""")
# print('')
# nome = str(input('Digite seu nome completo: ')).strip()
# print('Nome só com letras maiúsculas: {}'.format(nome.upper()))
# print('Nome só com letras minúsculas: {}'.format(nome.lower()))
# nome_dividido = nome.split()
# total_letras = ''.join(nome_dividido)
# print('O seu nome completo possui: {} letras'.format(len(total_letras)))  # Ou: (len(nome) - nome.count(' '))
# print('O seu primeiro nome possui: {} letras'.format(len(nome_dividido[0])))  # Ou: nome.find(' ')


# print('Desafio 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados')
# numero = input('Entre com um valor entre 0 e 9999: ')
# if len(numero) == 4:
#     print('Casa dos milhares: {}'.format(numero[0]))
#     print('Casa das centenas: {}'.format(numero[1]))
#     print('Casa das dezenas: {}'.format(numero[2]))
#     print('Casa das unidades: {}'.format(numero[3]))
# elif len(numero) == 3:
#     print('Casa das centenas: {}'.format(numero[0]))
#     print('Casa das dezenas: {}'.format(numero[1]))
#     print('Casa das unidades: {}'.format(numero[2]))
# elif len(numero) == 2:
#     print('Casa das dezenas: {}'.format(numero[0]))
#     print('Casa das unidades: {}'.format(numero[1]))
# elif len(numero) == 1:
#     print('Casa das unidades: {}'.format(numero[1]))

# Ou de uma forma mais simples, sem usar ifs, basta fazer:
# unidade = numero // 1 % 10
# dezena = numero // 10 % 10
# centena = numero // 100 % 10
# milhares = numero // 1000 % 10

# print('Desafio 24: Crie um programa que leia o nome de uma cidade e diga se a cidade começa ou não com o nome "Santo')
# nome_cidade = str(input('O nome da cidade começa com Santo? Escreva o nome de uma cidade: ')).strip()
# primeiro_nome = nome_cidade.split()[0]
# primeiro_nome = primeiro_nome.upper()
# if primeiro_nome == 'SANTO':
#     print('Sim! Sua cidade começa com o nome Santo!: {}'.format(nome_cidade))
# else:
#     print('Não! O primeiro nome da sua cidade é: {}'.format(primeiro_nome))
#     print('O nome completo da sua cidade é: {}'.format(nome_cidade))


# print('Desafio 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome')
# nome_completo = input('Entre com seu nome completo: ')
# nome_completo = ' ' + nome_completo + ' '
# nome_completo = nome_completo.upper()
# if nome_completo.find(' SILVA ') == -1:
#     print('Você NÃO TEM tem Silva no nome.')
# else:
#     print('Você TEM Silva no nome.')


# print("""Desafio 26: Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra A,
# em que posição ela aparece a primeira vez, em que posição ela aparece a última vez""")
# frase = str(input('Escreva uma frase qualquer: ')).strip()
#
# frase_minusculo = frase.lower()
#
# if frase_minusculo.count('a') > 0:
#     print('A letra "a" aparece {} vezes nesta frase.'.format(frase_minusculo.count('a')))
#     print('A primeira vez que a letra "a" aparece é na posição {}.'.format(frase_minusculo.find('a')+1))
#     print('A última vez que a letra "a" aparece é na posição {}.'.format(frase_minusculo.rfind('a')+1))
# else:
#     print('Não existe nenhuma letra "a" nesta frase')


# print("""Desafio 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente""")
# nome_completo = str(input('Entre com seu nome completo: ')).strip()
# nome_separado = nome_completo.split()
#
# print('O seu primeiro nome é: {}.'.format(nome_separado[0]))
# print('O seu último nome é: {}.'.format(nome_separado[len(nome_separado)-1]))
