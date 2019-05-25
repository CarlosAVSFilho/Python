print('=======Desafio 05: Programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor=======')
n_int = int(input('Entre com um número inteiro: '))
print('O antecessor de {} é: {}'.format(n_int, n_int-1))
print('O sucessor de {} é: {}'.format(n_int, n_int+1))


print('=======Desafio 06: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada=======')
n_qualquer = float(input('Entre com um número qualquer: '))
print('O dobro de {} é: {}'.format(n_qualquer, n_qualquer*2))
print('O triplo de {} é: {}'.format(n_qualquer, n_qualquer*3))
print('A raíz quadrada de {} é: {:.2f}'.format(n_qualquer, n_qualquer**(1/2)))


print('=======Desafio 07: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média=======')
nota1 = float(input('Entre com a primeira nota do aluno: '))
nota2 = float(input('Entre com a segunda nota do aluno: '))
media = (nota1+nota2)/2
print('A média entre as notas {} e {} é: {}'.format(nota1, nota2, media))


print('=======Desafio 08: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros=======')
metros = float(input('Entre com um valor em metro(s): '))
print('{} metro(s) equivale(m) a {} centímetros e a {:.1f} milímetros'.format(metros, metros*100, metros*1000))


print('=======Desafio 09: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada=======')
n_tabuada = int(input('Entre com um número inteiro: '))
print('{} x  1 = {}'.format(n_tabuada, n_tabuada*1))
print('{} x  2 = {}'.format(n_tabuada, n_tabuada*2))
print('{} x  3 = {}'.format(n_tabuada, n_tabuada*3))
print('{} x  4 = {}'.format(n_tabuada, n_tabuada*4))
print('{} x  5 = {}'.format(n_tabuada, n_tabuada*5))
print('{} x  6 = {}'.format(n_tabuada, n_tabuada*6))
print('{} x  7 = {}'.format(n_tabuada, n_tabuada*7))
print('{} x  8 = {}'.format(n_tabuada, n_tabuada*8))
print('{} x  9 = {}'.format(n_tabuada, n_tabuada*9))
print('{} x 10 = {}'.format(n_tabuada, n_tabuada*10))


print(""""=======Desafio 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
dólares ela poderia comprar=======""")
carteira = float(input('Entre com a quantidade em reais de dinheiro disponível: '))
cotacao_dolar = 3.27
print('Com R${:.2f} disponível, é possível adquirir US${:.2f} a uma cotação de R${} por dólar.'.format(carteira, carteira/cotacao_dolar, cotacao_dolar))


print("""=======Desafio 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²=======""")
altura = float(input('Entre com a altura da parede em metros: '))
largura = float(input('Entre com a largura da parede em metros: '))
rendimento_tinta = 2  # pinta 2 m² por litro
print('A área desta parede é de {}m² e a quantidade de tinta necessária será de {} litros'.format(altura*largura, (altura*largura)/rendimento_tinta))


print(""""=======Desafio 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto=======""")
preco = float(input('Entre com o valor do produto sem desconto: '))
print('O preço do produto sem desconto é de R${:.2f} e com 5% de desconto custará R${:.2f}'.format(preco, preco*0.95))


print("""=======Desafio 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento=======""")
salario = float(input('Entre com o seu salário atual: '))
print('Parabéns! Você teve 15% de aumento e seu salário passará de R${:.2f} para R${:.2f}'.format(salario, salario*1.15))