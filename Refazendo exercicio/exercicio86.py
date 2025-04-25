matriz = []
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
