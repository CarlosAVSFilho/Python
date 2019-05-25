Nome = input('Qual o seu nome? ')
Tutorial = input('Gostaria de ler o tutorial? [sim/não]: ')

if Tutorial == 'sim':
    print('Esse jogo não tem tutorial kkk!')
elif Tutorial == 'não':
    print('Vai lá, bonzão')

print("""Qual classe você gostaria?
(1) Mago.
(2) Gladiador.
(3) Arqueiro.
""")
while True:
    escolherclasse = int(input('Qual classe seria seu personagem? '))

    if escolherclasse == 3:
        print('Vai ser Arqueiro? Ok!')
    elif escolherclasse == 2:
        print('Vai ser Gladiador? Ok!')
    elif escolherclasse == 1:
        print('Vai ser Mago? Ok!')
    elif escolherclasse > 3 or escolherclasse == 0 or escolherclasse < 0:
        print('Para de graça!')

    if escolherclasse <= 3 and escolherclasse > 0:
        break

print(f"""Escolha sua arma:
(1){Nome} começa com uma Espada Longa!
(2){Nome} começa com Arco e 30 Flechas!
(3){Nome} começa com um Escudo de Doran!
""")
while True:
    escolha = int(input('Escolha sua arma inicial: '))
    if escolha == 1:
        print('Você começou com Espada Longa!')
    elif escolha == 2:
        print('Você começou com Arco e 30 Flechas!')
    elif escolha == 3:
        print('Você começou com Escuro de Doran!')
    elif escolha > 3 or escolha == 0 or escolha < 0:
        print('Para de graça!')

    if escolha <= 3 and escolha > 0:
        break

print('Você tem 10 pontos para distribuir!')
força = int(input('Quantos pontos gostaria de distribuir em força? '))

if força <= 10:
    print('Dica: Deixe equilibrado!')

print('Você tem 10 pontos para distribuir!')
agilidade = int(input('Quantos pontos gostaria de distribuir em agilidade? '))

if agilidade <= 10:
    print('Boa escolha, ficar ágil é vantajoso!')