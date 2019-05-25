# Desafio 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e
# metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# from ex107 import moeda
#
# p = float(input('Digite o preço: R$ '))
# print(f'A metade de {p} é { moeda.metade(p)}')
# print(f'O dobro de {p} é { moeda.dobro(p)}')
# print(f'Aumentando 10%, temos { moeda.aumentar(p, 10)}')
# print(f'Diminuindo 13%, temos { moeda.diminuir(p, 13)}')


# Desafio 108: Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os
# valores como um valor monetário formatado.

# from ex108 import moeda
#
# p = float(input('Digite o preço: R$ '))
# print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
# print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
# print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
# print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')


# Desafio 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# from ex109 import moeda
#
# p = float(input('Digite o preço: R$ '))
# print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
# print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
# print(f'Aumentando 10%, temos { moeda.aumentar(p, 10, True)}')
# print(f'Diminuindo 13%, temos { moeda.diminuir(p, 13, True)}')


# Desafio 110: Adicione ao módulo moeda.py criando nos desafios anteriores, uma função chamada resumo(), que mostre na
# tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.


# from ex110 import moeda
#
# p = float(input('Digite o preço: R$'))
# moeda.resumo(p, 10, 45)


# Desafio 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

# from ex111.utilidadescev import moeda
#
# p = float(input('Digite o preço: R$'))
# moeda.resumo(p, 35, 22)


# Desafio 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função
# chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar
# apenas valores que sejam monetários.


from ex112.utilidadescev import dado, moeda

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
