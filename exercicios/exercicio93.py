dados = dict()
partidas = list()
cont = 0
dados['Nome'] = str(input('Digite seu nome: '))
qntd = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
while cont < qntd:
    partidas.append(int(input(f'Quantos gols na partida {cont + 1}? ')))
    cont += 1
dados['Gols'] = partidas[:]
dados['Total'] = sum(partidas)
print('~'*60)

print(dados)
print('~'*60)

for keys, values in dados.items():
    print(f'O campo {keys} tem o valor {values}')
print('~'*60)

print(f'O jogador {dados["Nome"]} jogou {qntd} partidas. ')
for i, v in enumerate(partidas):
    print(f'Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {dados["Total"]} gols. ')
