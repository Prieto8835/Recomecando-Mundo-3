from random import randint
from operator import itemgetter
jogo = {
        'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)
        }

print('Valores sorteados: ')
for key, values in jogo.items():
    print(f'O {key} retirou {values} no dado! ')
print('~'*60)

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
