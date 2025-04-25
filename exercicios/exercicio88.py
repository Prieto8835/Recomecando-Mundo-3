from random import randint
from time import sleep
num = []
jogos = []
cont = 0
res = int(input('Quantos jogos quer gerar? '))
print('Gerando os valores...')
sleep(3)
while cont < res:
    while len(num) < 6:
        n = (randint(1, 60))
        if n not in num:
            num.append(n)
    num.sort()
    print(f'{cont + 1}° jogo: {num}')
    sleep(1.2)
    jogos.append(num[:])
    num.clear()
    cont += 1
print('Boa sorte! ')
