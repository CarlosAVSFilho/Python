# UTILIZAR IF E FOR

# Desafio 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de
# 10 até 0, com uma pausa de 1 segundo entre eles.

# import time
# for c in range(10, -1, -1):
#     if c != 0:
#         print(c)
#         time.sleep(1)
#     else:
#         print('Feliz Ano Novo!')



# Desafio 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# valor_min_entrada = int(input('Entre com o valor mínimo do intervalo: '))
# valor_max = int(input('Entre com o valor máximo do intervalo: '))
#
# if valor_min_entrada % 2 == 1:
#     valor_min = valor_min_entrada + 1
# else:
#     valor_min = valor_min_entrada
#
# print(f'Números Pares entre {valor_min_entrada} e {valor_max}:')
#
# for c in range(valor_min, valor_max+1, 2):
#     print(c, end=' ')



# Desafio 48: Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se
# encontram no intervalo de 1 até 500.

# int_min = int(input('Entre com o valor mínimo: '))
# int_max = int(input('Entre com o valor máximo: '))
#
# if int_min % 2 != 0:
#     valor_min = int_min
# else:
#     valor_min = int_min + 1
#
# soma = 0
# print(f'Números ímpares múltiplos de 3 entre {int_min} e {int_max}: ')
#
# for c in range(valor_min, int_max+1, 2):
#     if c % 3 == 0:
#         print(c, end=' ')
#         soma = soma + c
#
# print('')
# print(f'A soma total destes números é: {soma}')



# Desafio 49: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
# um laço FOR.

# import time
# numero = int(input('Entre com o valor que deseja a tabuada: '))
#
# for c in range(1, 11):
#     print(f'{c} x {numero} = {c*numero}')
#     time.sleep(0.5)



# Desafio 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

# n1 = int(input('1 - Entre com um número qualquer: '))
# n2 = int(input('2 - Entre com um número qualquer: '))
# n3 = int(input('3 - Entre com um número qualquer: '))
# n4 = int(input('4 - Entre com um número qualquer: '))
# n5 = int(input('5 - Entre com um número qualquer: '))
# n6 = int(input('6 - Entre com um número qualquer: '))
#
# lista = [n1, n2, n3, n4, n5, n6]
# soma = 0
#
# for c in range(0, 6):
#     teste = lista[c]
#     if teste % 2 == 0:
#         soma = soma + teste
#
# print(f'A soma dos números pares é: {soma}')



# Desafio 51: Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. No final, mostre os 10 primeiros
# termos dessa progressão.

# termo = int(input('Entre com o 1º termo de uma P.A: '))
# razao = int(input('Entre com a razão destaa P.A: '))
#
# print('Os 10 primeiros termos desta P.A:')
# print(termo, end=' ')
# for c in range(1, 10):
#     print(termo+razao*c, end=' ')



# Desafio 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# numero = int(input('Entre com um número qualquer: '))
#
# soma = 0
# for c in range(numero, 0, -1):
#     if numero % c == 0:
#         soma += 1
#
# if soma == 2:
#     print(f'O número {numero} É primo')
# else:
#     print(f'O número {numero} NÃO É primo')



# Desafio 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# frase = str(input('Entre com uma frase qualquer: ')).strip()
# frase_separada = frase.split()
# frase_junta_sem_espacos = ''.join(frase_separada)
# frase_minusculo = frase_junta_sem_espacos.lower()
# frase_ao_contrario = frase_minusculo[::-1]
# print(f'A frase original: {frase_minusculo}')
# print(f'A frase ao contrário: {frase_ao_contrario}')
# print('')
# if frase_minusculo == frase_ao_contrario:
#     print(f'A frase "{frase}" É um palíndromo')
# else:
#     print(f'A frase "{frase}" NÃO É um palíndromo')



# Desafio 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.

# from datetime import date
# atual = date.today().year
# maior = menor = 0
#
# for c in range(1, 8):
#     nascimento = int(input(f'Ano de nascimento da {c}ª pessoa: '))
#
#     if nascimento > atual:
#         nascimento = int(input(f'Por favor, entre com um ano válido de nascimento da {c}ª pessoa: '))
#     else:
#         if atual - nascimento < 18:
#             menor += 1
#         elif atual - nascimento >= 18:
#             maior += 1
#
# print(f'Total de pessoas menores de idade: {menor}.')
# print(f'Total de pessoas maiores de idade: {maior}.')



# Desafio 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# for c in range(1, 6):
#     peso = int(input(f'Entre com o peso da {c}ª pessoa [kg]: '))
#     if c == 1:
#         menor = peso
#         maior = peso
#     else:
#         if peso > maior:
#             maior = peso
#         elif peso < menor:
#             menor = peso
#
# print(f'O maior peso é: {maior}kg')
# print(f'O menor peso é: {menor}kg')



# Desafio 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo, qual é o nome do homem mais velho, quantas mulheres têm menos de 20 anos.

# total_idade = 0
# idade_inicial = 0
# idade_h_velho = 0
# nome_h_velho = ''
# somat_m_idade = 0
#
# for c in range(1, 5):
#     nome = str(input(f'Entre com o nome da {c}ª pessoa: ')).strip()
#     idade = int(input(f'Entre com a idade da {c}ª pessoa: '))
#     sexo = str(input(f'Entre com o sexo da {c}ª pessoa (M/F): ')).strip()
#     print('-'*45)
#     total_idade = total_idade + idade
#     if sexo == 'M':
#         if idade > idade_h_velho:
#             idade_h_velho = idade
#             nome_h_velho = nome
#     if sexo == 'F':
#         if idade < 20:
#             somat_m_idade += 1
#
# print(f'A média da idade do grupo é: {total_idade/4} anos')
#
# if nome_h_velho != '':
#     print(f'O nome do homem mais velho é: {nome_h_velho}')
# else:
#     print('Não houve nenhum homem na pesquisa.')
#
# print(f'Quantidade de mulheres com menos de 20 anos: {somat_m_idade}')