# Desafio 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No
# final, mostre o conteúdo da estrutura na tela.

# classe = dict()
# classe['nome'] = str(input('Nome: '))
# classe['media'] = float(input(f'Média de {classe["nome"]}: '))
#
# if classe['media'] >= 7.0:
#     classe['situacao'] = 'Aprovado'
# else:
#     classe['situacao'] = 'Reprovado'
#
# print('=-'*15)
# print(f'Nome: {classe["nome"]}')
# print(f'Média: {classe["media"]}')
# print(f'Situação: {classe["situacao"]}')



# Desafio 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
# em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# from time import sleep
# from random import randint
# from operator import itemgetter
#
# jogadas = dict()
# ranking = list()
#
# print('Valores sorteados: ')
# for i in range(0, 4):
#     jogadas['jogador'] = i+1
#     jogadas['valor'] = randint(1, 6)
#     print(f'    O jogador {jogadas["jogador"]} jogou: {jogadas["valor"]}')
#     ranking.append(jogadas.copy())
#
#     sleep(1)
#
# print('Ranking dos jogadores:')
# ranking_ordenado = sorted(ranking, key=itemgetter('valor'), reverse=True)
#
# for i in range(0, 4):
#     print(f'{i+1}º lugar: Jogador {ranking_ordenado[i]["jogador"]}. (Jogou {ranking_ordenado[i]["valor"]})')



# Desafio 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# from datetime import datetime
# now = datetime.now()
#
# trabalhadores = dict()
#
# trabalhadores['Nome'] = str(input('Nome: '))
#
# ano_nasc = int(input('Ano de nascimento: '))
# idade = now.year - ano_nasc
# trabalhadores['Idade'] = idade
#
# trabalhadores['CTPS'] = str(input('Nº carteira de trabalho (0 caso não tenha): '))
#
# if trabalhadores['CTPS'] != '0':
#     trabalhadores['Contratação [ano]'] = int(input('Ano de contratação: '))
#     trabalhadores['Salário [R$]'] = float(input('Salário: R$ '))
#     trabalhadores['Aposentadoria [idade]'] = idade + (35 - (now.year - trabalhadores['Contratação [ano]']))
#
# print('=-'*30)
# for k, v in trabalhadores.items():
#     print(f'{k}: {v}')



# Desafio 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# estatistica = dict()
# gols = list()
#
# estatistica['Nome'] = str(input('Nome: ')).strip()
# total_partidas = int(input('Qntd de partidas disputadas: '))
#
# for partidas in range(0, total_partidas):
#     gols.append(int(input(f'Gols na {partidas+1}ª partida: ')))
#
# estatistica['Gols'] = gols[:]
# estatistica['Total gols'] = sum(estatistica['Gols'])
#
# print('=-'*30)
# print(estatistica)
# print('=-'*30)
#
# for k, v in estatistica.items():
#     print(f'{k} = {v}.')
#
# print('=-'*30)
# print(f'O jogador {estatistica["Nome"]} jogou {len(estatistica["Gols"])} partidas.')
#
# for i in range(0, len(estatistica['Gols'])):
#     print(f'    => Na partida {i+1}, fez {estatistica["Gols"][i]} gols.')
#
# print(f'Foi um total de {estatistica["Total gols"]} gols.')
# print(f'Total gols: {estatistica["Total Gols"]}')



# Desafio 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) A média de
# idade do grupo. C) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas com idade acima da média.

# cadastro = dict()
# pessoas_list = list()
# while True:
#     cadastro.clear()
#     cadastro['Nome'] = str(input('Nome: ')).strip()
#     cadastro['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
#     cadastro['Idade'] = int(input('Idade: '))
#
#     pessoas_list.append(cadastro.copy())
#
#     resp = str(input('Continuar? [S/N]: ')).strip().upper()[0]
#     if resp in 'Nn':
#         break
#
# print(pessoas_list)
#
# print(f'A - Quantidade de pessoas inscritas: {len(pessoas_list)}')
#
# soma_idade = 0
# soma_mulheres = 0
# list_mulheres = list()
# list_acimamedia = list()
#
# for i in range(0, len(pessoas_list)):
#     soma_idade = soma_idade + pessoas_list[i]['Idade']
#
# for i in range(0, len(pessoas_list)):
#     if pessoas_list[i]['Sexo'] == 'F':
#         soma_mulheres += 1
#         list_mulheres.append(pessoas_list[i]['Nome'])
#
#     if pessoas_list[i]['Idade'] > soma_idade/len(pessoas_list):
#         list_acimamedia.append(pessoas_list[i]['Nome'])
#
# print(f'B - Média de idade do grupo: {soma_idade/len(pessoas_list):.1f} anos')
# print(f'C - Quantidade de mulheres no grupo: {soma_mulheres} -> {list_mulheres}')
# print(f'D - Pessoas acima da média de idade -> {list_acimamedia}')



# Desafio 95: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

# jogador = dict()
# gols = list()
# estatistica = list()
#
# while True:
#     jogador['Nome'] = str(input('Nome: ')).strip()
#     total_partidas = int(input('Qntd de partidas disputadas: '))
#
#     for partidas in range(0, total_partidas):
#         gols.append(int(input(f'Gols na {partidas+1}ª partida: ')))
#
#     jogador['Gols'] = gols[:]
#     jogador['Total gols'] = sum(jogador['Gols'])
#
#     estatistica.append(jogador.copy())
#     gols.clear()
#
#     resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
#
#     if resp in 'Nn':
#         break
#
# print('=-'*30)
# print(f'{"Cód.":<5}{"Nome":<25}{"Gols":<15}{"Total":>10}')
#
# for i in range(0, len(estatistica)):
#     print(f'{i:<5}{estatistica[i]["Nome"]:<25}{str(estatistica[i]["Gols"]):<15}{estatistica[i]["Total gols"]:>10}')
#
# while True:
#     n_jogador = int(input('Deseja ver estatísticas de qual jogador? (999 pra sair): '))
#
#     while n_jogador >= len(estatistica) and n_jogador != 999:
#         n_jogador = int(input('Jogador invalido. Deseja ver estatísticas de qual jogador? (999 pra sair): '))
#     if n_jogador == 999:
#         break
#
#     for i in range(0, len(estatistica[n_jogador]['Gols'])):
#         print(f'No jogo {i+1} fez {estatistica[n_jogador]["Gols"][i]} gols.')
#     print('=-'*30)
#
# print('Volte sempre!')
