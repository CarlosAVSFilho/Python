print("""Desafio 04: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as"
informações possíveis sobre ele""")
a = input('Digite qualquer coisa: ')

print('A frase digitada:')
print('O tipo primitivo dessa frase é', type(a))
print('Só tem espaços?', a.isspace())
print('Tem só números?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Tem só letras maiúsculas?', a.isupper())
print('Tem só letras minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())
