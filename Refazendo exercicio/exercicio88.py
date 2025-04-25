from random import randint
from time import sleep
temp = []
lista = []
cont = 0
qntd = int(input('Quantos jogos quer que eu sorteie? '))
while cont < qntd:
    while len(temp) < 6:
        x = randint(1, 60)
        if x not in temp: 
            temp.append(x)
    temp.sort()
    lista.append(temp[:])
    temp.clear()
    cont += 1

print('Gerando valores...')
for pos, valor in enumerate(lista): 
    sleep(1)
    print(f'Jogo {pos + 1}: {lista[pos]}')
sleep(1)
print('Boa sorte! ')