# UTILIZAR IF, FOR E WHILE e break

# Desafio 66: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando a flag).

# numero = 0
# cont = 0
# soma = 0
#
# while numero != 999: #podemos usar while True:
#     numero_digitados = int(input('Digite um número inteiro (999 para parar): '))
#     numero = numero_digitados
#
#     if numero == 999:
#         break
#
#     cont = cont + 1
#     soma = soma + numero
# print(f'Você digitou {cont} números e a soma foi {soma}.')



# Desafio 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
# usuário. O programa será interrompido quando o número solicitado for negativo.

# while True:
#     tabuada = int(input('Entre com o valor que queira ver a tabuada: '))
#     if tabuada < 0:
#         break
#     for c in range(1, 11):
#         print(f'{c} x {tabuada} = {c*tabuada}')
#
# print('Programa finalizado.')



# Desafio 68: Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador
# PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# import random
# vitorias = 0
#
# while True:
#     par_impar = str(input('PAR OU IMPAR?: ')).strip().upper()
#     jogador = int(input('Escolha um valor: '))
#     pc = random.randint(0, 10)
#
#     if par_impar == 'PAR':
#         if (pc + jogador) % 2 == 0:
#             print(f'Você ganhou! Deu par! Você jogou {jogador} e o PC {pc}. Total = {jogador+pc}.')
#             vitorias += 1
#         else:
#             print(f'Você perdeu! Deu impar! Você jogou {jogador} e o PC {pc}. Total = {jogador+pc}.')
#             break
#     elif par_impar == 'IMPAR':
#         if (pc + jogador) % 2 == 1:
#             print(f'Você ganhou! Deu impar! Você jogou {jogador} e o PC {pc}. Total = {jogador+pc}.')
#             vitorias += 1
#         else:
#             print(f'Você perdeu! Deu par! Você jogou {jogador} e o PC {pc}. Total = {jogador+pc}.')
#             break
#
# print(f'Você teve {vitorias} vitória(s) consecutiva(s).')




# Desafio 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos, B) quantos homens foram cadastrados, C) quantas mulheres tem menos de 20 anos.

# maioridade = homens = mulher_vinte = 0
#
# while True:
#     idade = int(input('Entre com a idade: '))
#     sexo = ' '
#     while sexo not in 'MF':
#         sexo = str(input('Entre com o sexo [M/F]:')).strip().upper()[0]
#
#     flag = ' '
#     while flag not in 'SN':
#         flag = str(input('Deseja cadastrar mais alguém? [S/N]: ')).strip().upper()[0]
#
#     if idade > 18:
#         maioridade += 1
#     if sexo == 'M':
#         homens += 1
#     if idade < 20 and sexo == 'F':
#         mulher_vinte += 1
#     if flag == 'N':
#         break
# print('Programa finalizado')
# print(f'Foram cadastrados {maioridade} pessoas maiores de idade.')
# print(f'Foram cadastrados {homens} homens.')
# print(f'Foram cadastrados {mulher_vinte} mulheres com menos de 20 anos.')



# Desafio 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
# vai continuar. No final, mostre:
# A) Qual é o total gasto na compra, B) Quantos produtos custam mais de 1000 reais, C) Qual é o nome do produto mais
# barato.

# valor_total = 0
# valor_mil = 0
# produto_caro = ''
# valor_mais_caro = 0
# while True:
#     produto = str(input('Nome do produto: '))
#     valor = float(input('Valor do produto: R$'))
#     flag = str(input('Deseja cadastrar outro produto? [S/N]: ')).strip().upper()[0]
#     print('=-' * 15)
#
#     valor_total = valor_total + valor
#
#     if valor > 1000:
#         valor_mil += 1
#
#     if valor > valor_mais_caro:
#         valor_mais_caro = valor
#         produto_caro = produto
#
#     if flag == 'N':
#         break
#
# print(f'O valor total da compra foi R${valor_total:.2f}.')
# print(f'Na compra, tem-se {valor_mil} itens acima de R$ 1000,00')
# print(f'O produto mais caro custou R${valor_mais_caro:.2f} e foi o: {produto_caro}.')



# Desafio 71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
# será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# saque = int(input('Entre com o valor a ser sacado: R$'))
#
# notas_cinquenta = saque//50
# notas_vinte = (saque - notas_cinquenta*50)//20
# notas_dez = (saque - (notas_cinquenta*50 + notas_vinte*20))//10
# notas_um = (saque - (notas_cinquenta*50 + notas_vinte*20 + notas_dez*10))//1
#
# print(f"""Um saque de R${saque} você terá:
# {notas_cinquenta} notas de cinquenta
# {notas_vinte} notas de vinte
# {notas_dez} notas de dez
# {notas_um} notas de um""")