def area(a, b):
    terreno = a * b
    print(f'A área desse terreno é de {terreno}m² ')


print('Área do terreno! ')
area(a=int(input('Largura (m): ')), b=int(input('Comprimento (m): ')))
print('-' * 60)

def area(a, b):
    terreno = a * b
    print(f'A área desse terreno é de {terreno}m² ')


larg = int(input('Largura (m): '))
comp = int(input('Comprimento (m): '))
area(larg, comp)
