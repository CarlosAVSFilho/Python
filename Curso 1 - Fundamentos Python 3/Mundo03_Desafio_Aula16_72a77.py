# Desafio 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero a vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
#            'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
#
# while True:
#     usuario = int(input('Entre com um número inteiro de 0 a 20: '))
#
#     if 0 <= usuario <= 20:
#         break
# print(f'Você digitou: {numeros[usuario]}.')



# Desafio 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Brasileirão, na ordem de colocação.
# Depois mostre: A) Apenas os 5 primeiros. B) Os últimos 4 colocados da tabela. C) Uma lista com os times em ordem
# alfabética. D) Em que posição na tabela está o time da Chapecoense.

# brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
#                'Atlético-MG', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
#                'Bahia', 'Corinthians', 'Fluminense', 'Vasco', 'Ceará',
#                'Chapecoense', 'Sport', 'América-MG', 'Vitória', 'Paraná')
#
# escolha = str(input("""O que você deseja ver?
# A) Os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Posição de algum time.
# """)).strip().upper()[0]
#
# if escolha == 'A':
#     print(brasileirao[0:5])
# elif escolha == 'B':
#     print(brasileirao[16:20]) #poderia fazer tbm [-4:]
# elif escolha == 'C':
#     print(sorted(brasileirao))
# elif escolha == 'D':
#     posicao = 0
#     time = str(input('Entre com o time que deseja saber a posição: ')).capitalize()
#     teste = ''
#     while teste != time:
#         teste = brasileirao[posicao]
#         posicao += 1
#
#     print(f'O time {time} está na {posicao}ª posição.') #também poderia usar times.index("time") para achar a posicao


# Desafio 74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
# listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# import random
#
# lim_sup = int(input('Pretende gerar números aleatórios até qual número? '))
#
# aleatorios = (random.randint(0, lim_sup), random.randint(0, lim_sup), random.randint(0, lim_sup),
#               random.randint(0, lim_sup), random.randint(0, lim_sup))
#
# print(f'1 - Os números gerados aleatoriamente foram: {aleatorios}')
#
# maior = menor = 0
# for i in range(0, len(aleatorios)):
#     if i == 0:
#         maior = aleatorios[i]
#         menor = aleatorios[i]
#     else:
#         if aleatorios[i] > maior:
#             maior = aleatorios[i]
#         elif aleatorios[i] < menor:
#             menor = aleatorios[i]
#
# print(f'2 - O menor valor é: {menor}') #posso usar max(aleatorios) para tuplas
# print(f'3 - O maior valor é: {maior}') #posso usar min(aleatorios) para tuplas ao invés dos laços



# Desafio 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3.C) Quais foram os números pares

# n1 = int(input('Entre com o 1º valor: '))
# n2 = int(input('Entre com o 2º valor: '))
# n3 = int(input('Entre com o 3º valor: '))
# n4 = int(input('Entre com o 4º valor: '))
#
# valores = (n1, n2, n3, n4) #posso pegar os valores diretamente dentro da tupla, sem este passo aqui
# cont_9 = 0
# pos_3 = -1
# aparicao_3 = False
#
# for posicao in range(0, len(valores)):
#     if valores[posicao] == 9:
#         cont_9 += 1
#     if valores[posicao] == 3 and aparicao_3 is False:
#         pos_3 = posicao+1
#         aparicao_3 = True
#
# print(f'1 - O número 9 apareceu {cont_9} vez(es).') #posso usar diretamente valores.count(9)
#
# if pos_3 == -1:
#     print(f'2 - O número 3 não apareceu em nenhuma posição.') #posso usar diretamente valores.index(3)
# else:
#     print(f'2 - O número 3 apareceu pela primeira vez na {pos_3}ª posição.')
#
# print('3 - Números pares que apareceram: ', end='')
# posicao = 0
# for posicao in range(0, len(valores)):
#     if valores[posicao] % 2 == 0:
#         print(f'{valores[posicao]} - ', end='')



# Desafio 76: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# produtos = ('Sabão', 12, 'Macarrão', 4, 'Alface', 2.50, 'Frango', 8, 'Arroz', 7, 'Calabresa', 12, 'Morango', 9)
#
#
#
# print('-'*37)
# print('        TABELA DE COMPRAS')
# print('-'*37)
#
# for i in range(0, len(produtos), 2):
#     if len(produtos[i]) < 20:
#        pontilhados = 25 - len(produtos[i])
#        print(f'{produtos[i]}', '.'*pontilhados, f'R$ {produtos[i+1]:>6.2f}') #posso formatar com produtos[i]:.<20 por ex
#
# print('-'*37)



# Desafio 77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve
# mostrar, para cada palavra, quais são as suas vogais.

# palavras = ('Ronaldo', 'Ronaldinho', 'Neymar', 'Messi', 'Cristiano', 'Pele', 'Mbappe', 'Cavani', 'Suarez', 'Hazard')
#
# for cont in range(0, len(palavras), 1):
#     a = palavras[cont].count('a')
#     e = palavras[cont].count('e')
#     i = palavras[cont].count('i')
#     o = palavras[cont].count('o')
#     u = palavras[cont].count('u')
#     print(f'Na palavra {palavras[cont].upper()} temos: ', end='')
#     if a != 0:
#         print('a '*a, end='')
#     if e != 0:
#         print('e '*e, end='')
#     if i != 0:
#         print('i '*i, end='')
#     if o != 0:
#         print('o '*o, end='')
#     if u != 0:
#         print('u '*u, end='')
#     print('')

# Outra forma de se fazer este desafio:
# palavras = ('Ronaldo', 'Ronaldinho', 'Neymar', 'Messi', 'Cristiano', 'Pele', 'Mbappe', 'Cavani', 'Suarez', 'Hazard')
#
# for p in palavras:
#     print(f'\nNa palavra {p.upper()} temos ', end='')
#     for letra in p:  # a propria palavra é uma lista de letras
#         if letra.lower() in 'aeiou':
#             print(letra, end='')
