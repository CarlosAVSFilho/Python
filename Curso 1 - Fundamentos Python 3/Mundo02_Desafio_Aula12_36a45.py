# # UTILIZAR APENAS IF E ELIF



# # Desafio 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
# # o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# # Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então empréstimo será negado.
#
# print('-'*20)
# print('EMPRÉSTIMO BANCÁRIO')
# print('-'*20)
#
# valor_casa = float(input('Entre com o valor da casa: R$ '))
# salario = float(input('Entre com o seu salário: R$ '))
# anos = int(input('Entre com a quantidade de anos a se pagar: '))
# prestacao_mensal = valor_casa/(anos*12)
#
# if prestacao_mensal/salario <= 0.3:
#     print(f'O valor a ser pago mensalmente será de R${prestacao_mensal:.2f}.')
#     print(f'Esta parcela corresponde a {(prestacao_mensal/salario)*100:.2f}% do seu salário.')
# else:
#     print(f'A sua parcela mensal de R${prestacao_mensal:.2f} corresponde a ', end='')
#     print(f'{(prestacao_mensal/salario)*100:.2f}% do seu salário.')
#     print('Portanto não será possível realizar o financiamento.')
#     print('Para realizar um financiamento, parcele com no máximo 30% de seu salário.')



# # Desafio 37: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# # conversão: 1 para binário, 2 para octal ou 3 para hexadecimal.
#
# numero = int(input('Entre com um número inteiro: '))
# print('Pressione:')
# conversor = int(input("""[1] Para converter para Binário
# [2] Para converter para Octal
# [3] Para converter para Hexadecimal\n"""))
#
# if conversor == '1':
#     print(f'Binário: {bin(numero)[2:]}')
# elif conversor == '2':
#     print(f'Octal: {oct(numero)[2:]}')
# elif conversor == '3':
#     print(f'Hexadecimal: {hex(numero)[2:]}')
# else:
#     print('Você não pressionou 1, 2 ou 3.')



# # Desafio 38: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# # # O PRIMEIRO VALOR é maior, O SEGUNDO VALOR é maior ou NÃO EXISTE valor maior, os dois são iguais.
# #
# # n1 = int(input('Entre com um número inteiro: '))
# # n2 = int(input('Entre com outro número inteiro: '))
# #
# # if n1 > n2:
# #     print(f'O PRIMEIRO valor ({n1}) é maior.')
# # elif n2 > n1:
# #     print(f'O SEGUNDO valor ({n2}) é maior.')
# # elif n1 == n2:
# #     print('Os dois números são iguais.')



# # Desafio 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# # Se ele ainda vai se alistar ao serviço militar. Se é a hora de se alistar ou se já passou do tempo do alistamento.
# # Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#
# from datetime import datetime
# now = datetime.now()
#
# ano_nasc = int(input('Entre com o ano de seu nascimento: '))
#
# idade = now.year - ano_nasc
#
# if idade < 18:
#     print(f'Você deve se alistar em {18-idade} ano(s)')
# elif idade == 18:
#     print('Chegou o ano de você se alistar!')
# elif idade > 18:
#     print(f'Você está atrasado {idade-18} ano(s) para se alistar!')



# # Desafio 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de
# # acordo com a média atingida: Média abaixo de 5.0: REPROVADO, Média entre 5.0 e 6.9: RECUPERAÇÃO e Média 7.0 ou
# # superior: APROVADO.
#
# nota1 = float(input('Entre com sua primeira nota: '))
# nota2 = float(input('Entre com sua segunda nota: '))
#
# media = (nota1 + nota2)/2
#
# if media < 5.0:
#     print(f'Você foi\033[0;31;m REPROVADO\033[m com média igual a: {media}')
# elif media >= 5.0 and media < 7.0:
#     print(f'Você está de\033[0;33;m RECUPERAÇÃO\033[m com média igual a: {media}')
# elif media >= 7.0:
#     print(f'Você foi\033[0;34;m APROVADO\033[m com média igual a: {media}')



# # Desafio 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# # mostre sua categoria, de acordo com sua idade.
# # Até 9 anos: MIRIM, Até 14 anos: INFANTIL, Até 19 anos: JUNIOR, Até 25: SÊNIOR e Acima de 19: MASTER.
#
# from datetime import datetime
# now = datetime.now()
#
# ano_nasc = int(input('Entre com o seu ano de nascimento: '))
# idade = now.year - ano_nasc
#
# if idade <= 9:
#     print(f'Um atleta nascido em {ano_nasc} pertence à classe Mirim.')
# elif idade > 9 and idade <= 14: #posso fazer direto idade <= 14
#     print(f'Um atleta nascido em {ano_nasc} pertence à classe Infantil.')
# elif idade > 14 and idade <= 19: #posso fazer direto idade <= 19
#     print(f'Um atleta nascido em {ano_nasc} pertence à classe Junior.')
# elif idade > 19 and idade <= 25: #posso fazer direto idade <= 25
#     print(f'Um atleta nascido em {ano_nasc} pertence à classe Master.')
# elif idade > 25:
#     print(f'Um atleta nascido em {ano_nasc} pertence à classe Master.')



# # Desafio 42: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
# # formado. Equilátero: todos lados iguais, Isosceles: dois lados iguais e um diferente
# # Escaleno: todos lados diferentes.
#
# a = float(input('Entre com o valor da 1ª aresta: '))
# b = float(input('Entre com o valor da 2ª aresta: '))
# c = float(input('Entre com o valor da 3ª aresta: '))
#
# if ((abs(b-c) < a) and (a < b+c)) and ((abs(a-c) < b) and (b < a+c)) and ((abs(a-b) < c) and (c < a+b)):
#     if a == b and a == c: #posso fazer tbm a == b == c
#         print(f'{a}, {b} e {c} podem formar um Triângulo Equilátero.')
#     elif a == b or a == c:
#         print(f'{a}, {b} e {c} podem formar um Triângulo Isosceles.')
#     elif a != b and a != c: #posso fazer tbm a != b != c != a
#         print(f'{a}, {b} e {c} podem formar um Triângulo Escaleno.')
# else:
#     print('Os lados não formam um Triângulo!')



# # Desafio 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de
# # acordo com a tabela abaixo: Abaixo de 18.5: Abaixo do Peso, Entre 18.5 e 25: Peso ideal, De 25 a 30: sobrepeso, de 30
# # a 40, obesidade, acima de 40: obesidade morbida.
#
# peso = float(input('Entre com seu peso [kg]: '))
# altura = float(input('Entre com sua altura [cm]: '))
# altura_m = altura/100
#
# imc = peso/(altura_m**2)
#
# if imc < 18.5:
#     print(f'IMC = {imc:.1f}: Abaixo do peso.')
# elif imc >= 18.5 and imc < 25: #poderia escrever da seguinte forma tbm: 18.5 <= imc < 25
#     print(f'IMC = {imc:.1f}: Peso ideal.')
# elif imc >= 25 and imc < 30:
#     print(f'IMC = {imc:.1f}: Sobrepeso.')
# elif imc >= 30 and imc < 40:
#     print(f'IMC = {imc:.1f}: Obesidade.')
# elif imc >= 40:
#     print(f'IMC = {imc:.1f}: Obesidade mórbida.')



# Desafio 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento: A vista dinheiro/cheque: 10% de desconto. A vista no cartao: 5% de desconto. Em até 2x no
# cartão: preço normal e em 3x ou mais no cartão: 20% de juros.

# preco = float(input('Entre com o valor do produto: R$ '))
# print('Escolha a forma de pagamento:')
# condicao = int(input("""[1] À vista no dinheiro/cheque.
# [2] À vista no cartão.
# [3] 2x no cartão.
# [4] 3x ou mais no cartão.
# """))
#
# if condicao == 1:
#     print(f'À vista no dinheiro/cheque você tem 10% de desconto, passando de R${preco:.2f} para R${0.9*preco:.2f}.')
# elif condicao == 2:
#     print(f'À vista no cartão você tem 5% de desconto, passando de R${preco:.2f} para R${0.95*preco:.2f}.')
# elif condicao == 3:
#     print(f'Em 2x no cartão você não recebe desconto. Preço final: R${preco:.2f}.')
# elif condicao == 4:
#     print(f'Em 3x ou mais no cartão, você paga 20% de juros, passando de R${preco:.2f} para R${1.2*preco:.2f}.')
# else:
#     print('Por favor, digite uma opção de 1 a 4')



# # Desafio 45: Crie um programa que faça o computador jogar JOKENPO com você.
# import random
#
# pc = random.randint(1,3)
#
# jokenpo = int(input("""Escolha:
# [1] Pedra
# [2] Papel
# [3] Tesoura
# """))
#
# if jokenpo == 1 and pc == 1:
#     print('EMPATE - Ambos escolheram Pedra')
# elif jokenpo == 1 and pc == 2:
#     print('VOCÊ PERDEU! - Você escolheu Pedra e o PC Papel')
# elif jokenpo == 1 and pc == 3:
#     print('VOCÊ GANHOU! - Você escolheu Pedra e o PC Tesoura')
# elif jokenpo == 2 and pc == 1:
#     print('VOCÊ GANHOU! - Você escolheu Papel e o PC Pedra')
# elif jokenpo == 2 and pc == 2:
#     print('EMPATE - Ambos escolheram Papel')
# elif jokenpo == 2 and pc == 3:
#     print('VOCÊ PERDEU - Você escolheu Papel e o PC Tesoura')
# elif jokenpo == 3 and pc == 1:
#     print('VOCÊ PERDEU - Você escolheu Tesoura e o PC Pedra')
# elif jokenpo == 3 and pc == 2:
#     print('VOCÊ GANHOU - Você escolheu Tesoura e o PC Papel')
# elif jokenpo == 3 and pc == 3:
#     print('EMPATE - Ambos escolheram Tesoura')
# else:
#     print('Escolha entre [1] e [3]')

# if jokenpo == 1:
#     if pc == 1:
#         print('EMPATE: Ambos escolheram Pedra')
#     elif pc == 2:
#         print('PC GANHOU: Você -> Pedra. PC -> Papel')
#     elif pc == 3:
#         print('JOGADOR GANHOU: Você -> Pedra. PC -> Tesoura')
# elif jokenpo == 2:
#     if pc == 1:
#         print('JOGADOR GANHOU: Você -> Papel. PC -> Pedra')
#     elif pc == 2:
#         print('EMPATE: Ambos escolheram Papel')
#     elif pc == 3:
#         print('PC GANHOU: Você -> Papel. PC -> Tesoura')
# elif jokenpo == 3:
#     if pc == 1:
#         print('PC GANHOU: Você -> Tesoura. PC -> Pedra')
#     elif pc == 2:
#         print('JOGADOR GANHOU: Você -> Tesoura. PC -> Papel')
#     elif pc == 3:
#         print('EMPATE: Ambos escolheram Tesoura')
