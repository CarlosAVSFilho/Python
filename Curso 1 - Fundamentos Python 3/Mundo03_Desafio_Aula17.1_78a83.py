# Desafio 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
# e o menor valor digitado e as suas respectivas posições na lista.

# lista = list()
# for i in range(0, 5):
#     lista.append(int(input(f'Digite o {i+1}º número da lista: ')))
#
# print(f'A lista digitada apresenta os seguintes números: {lista}')
# print(f'O menor número da lista é: {min(lista)} e ele é o {lista.index(min(lista))+1}º número da lista.')
# print(f'O maior número da lista é: {max(lista)} e ele é o {lista.index(max(lista))+1}º número da lista.')



# Desafio 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o
# número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em
# ordem crescente.

# lista = list()
# i = 0
#
# while True:
#     lista.append(int(input('Entre com um número: ')))
#
#     while lista.count(lista[i]) != 1:
#         lista.pop()
#         lista.append(int(input('Este valor já foi adicionado, por favor, entre com outro número: ')))
#
#     flag = str(input('Deseja adicionar mais números[S/N]? ')).strip().upper()
#     i = i+1
#
#     while flag not in 'SsNn':
#         flag = str(input('Digite S para continuar ou N para parar: ')).strip().upper()
#
#     if flag in 'N':
#         break
# print(f'Os números digitados em ordem crescente foram: {sorted(lista)}')



# Desafio 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
# posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# lista = list()
# for i in range(0, 5):
#     lista.append(int(input(f'Digite {i+1}º número da lista: ')))
#
#     for j in range(0, i):
#         if lista[j] > lista[i]:
#             a = lista[j]
#             b = lista[i]
#             lista[j] = b
#             lista[i] = a
#         elif lista[i] >= lista[j]:
#             lista[i] = lista[i]
#
# print(lista)



# Desafio 81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado
# e está ou não na lista.

# lista = list()
#
# while True:
#     lista.append(int(input('Entre com um número: ')))
#     flag = str(input('Deseja adicionar mais números[S/N]? ')).strip().upper()
#
#     while flag not in 'SsNn':
#         flag = str(input('Digite S para continuar ou N para parar: ')).strip().upper()
#
#     if flag in 'N':
#         break
#
# print(f'A lista digitada: {lista}')
# print('')
# print(f'A - Foram digitados {len(lista)} números.')
# print(f'B - Numeros em ordem decrescente: {sorted(lista, reverse=True)}')
# print(f'C - O 5 foi digitado' if lista.count(5) > 0 else 'C - O 5 não foi digitado') # podia usar "if 5 in lista"



# Desafio 82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
# que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

# lista = list()
# lista_par = list()
# lista_impar = list()
#
# i = 0
#
# while True:
#     lista.append(int(input('Entre com um número: ')))
#     flag = str(input('Deseja adicionar mais números[S/N]? ')).strip().upper()
#
#     while flag not in 'SsNn':
#         flag = str(input('Digite S para continuar ou N para parar: ')).strip().upper()
#
#     if lista[i] % 2 == 0:
#         lista_par.append(lista[i])
#     else:
#         lista_impar.append(lista[i])
#
#     i = i+1
#
#     if flag in 'N':
#         break
#
# print(f'Lista original: {lista}')
# print(f'Lista par: {lista_par}')
# print(f'Lista impar: {lista_impar}')



# Desafio 83: Crie um programa onde o usuário digita uma expressão qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# lista = list()
#
# lista.append(str(input('Entre com sua expressão: ')))
#
# # lista_separada = lista[0].strip()
#
#
# if lista[0].count('(') == lista[0].count(')'):
#     print('OK!')
# else:
#     print('not OK!')


# VERSÃO GUANABARA:
# expr = str(input('Digite a expressão: '))
# pilha = []
# for simb in expr:
#     if simb == '(':
#         pilha.append('(')
#     elif simb == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('OK!')
# else:
#     print('Não OK!')
