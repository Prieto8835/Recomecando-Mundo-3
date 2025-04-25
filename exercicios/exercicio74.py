from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram {num}')
print(f'O menor valor da tupla é {min(num)}')
print(f'O mairo valor da tupla é {max(num)}')
