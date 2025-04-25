matriz = []
pares = []
linha = []
coluna = []
for cont in range(0, 9):
    matriz.append(int(input(f'Digite um valor para a posição {cont + 1}: ')))
for pos in range(0, 3):
    print(f'[{matriz[pos]:^6}]',end='   ')
print()
for pos in range(3, 6):
    print(f'[{matriz[pos]:^6}]',end='   ')
    linha.append(matriz[pos])
print()
for pos in range(6, 9):
    print(f'[{matriz[pos]:^6}]',end='   ')
print()

for valor in matriz:
    if valor % 2 == 0:
        pares.append(valor)

for pos, valor in enumerate(matriz):
    if pos == 2 or pos == 5 or pos == 8:
        coluna.append(valor)

print(f'Números pares: {pares}')
print(f'Terceira coluna: {coluna}')
print(f'Segunda linha: {linha}')

print(f'A soma dos valores pares foram: {sum(pares)}')
print(f'A soma dos valores da terceira coluna foram: {sum(coluna)}')
print(f'O maior valor da segunda linha é: {max(linha)}')



matriz = []
pares = []
coluna = []

for cont in range(0, 9):
    matriz.append(int(input(f'Digite um valor para a posição {cont + 1}: ')))
for pos in range(0, 3):
    print(f'[{matriz[pos]:^6}]',end='   ')
print()
for pos in range(3, 6):
    print(f'[{matriz[pos]:^6}]',end='   ')
print()
for pos in range(6, 9):
    print(f'[{matriz[pos]:^6}]',end='   ')
print()

for valor in matriz:
    if valor % 2 == 0:
        pares.append(valor)

for pos, valor in enumerate(matriz):
    if pos == 2 or pos == 5 or pos == 8:
        coluna.append(valor)

print(f'A soma dos valores pares foram: {sum(pares)}')
print(f'A soma dos valores da terceira coluna foram: {sum(coluna)}')
print(f'O maior valor da segunda linha é: {max(matriz[3], matriz[4], matriz[5])}')
