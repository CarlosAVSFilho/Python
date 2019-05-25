import math

# print('Desafio 16: Crie um programa que leia um nº real qualquer pelo teclado e mostre na tela a sua porção inteira')
# numero = float(input('Entre com um número real qualquer: '))
# print('O numero real {} possui a parte inteira igual a: {}'.format(numero, math.trunc(numero)))

# print("""Desafio 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa""")
# cat1 = int(input('Entre com o valor de um cateto: '))
# cat2 = int(input('Entre com outro valor de cateto: '))
# print('Dados os valores dos catetos sendo {} e {}, a hipotenusa valerá {}'.format(cat1, cat2, math.hypot(cat1,cat2)))

# print("""Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# deste angulo""")
# angulo = float(input('Entre com o valor de um ângulo: '))
# ang_rad = math.radians(angulo)
# print('sen({}) = {:.2f}'.format(angulo, math.sin(ang_rad)))
# print('cos({}) = {:.2f}'.format(angulo, math.cos(ang_rad)))
# print('tan({}) = {:.2f}'.format(angulo, math.tan(ang_rad)))

# print("""Desafio 19: Um prof. quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido""")
# import random
# nome_1 = input('Entre com o nome do primeiro aluno: ')
# nome_2 = input('Entre com o nome do segundo aluno: ')
# nome_3 = input('Entre com o nome do terceiro aluno: ')
# nome_4 = input('Entre com o nome do quarto aluno: ')
# lista = [nome_1, nome_2, nome_3, nome_4]
#
# print('O(a) aluno(a) sorteado(a) foi o(a): {}'.format(random.choice(lista)))

# print("""Desafio 20: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada""")
# import random
# nome_1 = input('Entre com o nome do primeiro aluno: ')
# nome_2 = input('Entre com o nome do segundo aluno: ')
# nome_3 = input('Entre com o nome do terceiro aluno: ')
# nome_4 = input('Entre com o nome do quarto aluno: ')
# lista = [nome_1, nome_2, nome_3, nome_4]
# random.shuffle(lista)
# print('A ordem dos alunos sorteados é:')
# print(lista)

print('Desafio 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo .MP3')
import pygame

name = input('Escolha um nome da familia (Carlinhos, Mae, Pai, Lorraine): ')

pygame.mixer.init()

if name == 'Carlinhos':
                    pygame.mixer.music.load('audioeu.mp3')
elif name == 'Lorraine':
                    pygame.mixer.music.load('audiolo.mp3')
elif name == 'Pai':
                    pygame.mixer.music.load('audiopai.mp3')
else:
                    pygame.mixer.music.load('audiomae.mp3')

pygame.mixer.music.play()
input()
# pygame.event.wait()
# Outra forma de se fazer:
# from pygame import mixer
# mixer.init()
# mixer.music.load('teste.mp3')
# mixer.music.play()
# input('Agora você escuta?')