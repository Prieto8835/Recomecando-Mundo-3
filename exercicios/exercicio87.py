'''''''''
lista = []
terceira_coluna = []
segunda_linha = []
x = 1
for cont in range(0, 9):
    lista.append(int(input(f'Digite um valor para a {x}° posição: '))) 
    x += 1

pos = 2
cont = 0
while cont <= 2:
    terceira_coluna.append(lista[pos])
    pos += 3
    cont += 1

pos = 3
cont = 0
while cont <= 2:
    segunda_linha.append(lista[pos])
    pos += 1
    cont += 1
    
par = []
for pos, pares in enumerate(lista):
    if pares % 2 == 0:
        par.append(pares)

y = 0
for cont in range(0, 3):
    print(lista[y],end='    ')
    y += 1
print()

for cont in range(0, 3):
    print(lista[y],end='    ')
    y += 1
print()

for cont in range(0, 3):
    print(lista[y],end='    ')
    y += 1
print()
print('*'*30)

print(f'Os valores pares digitados foram {par} e a soma entre eles foi {sum(par)} ')
print(f'A soma dos valores da terceira coluna é {sum(terceira_coluna)}')
print(f'O maior valor da segunda linha é {max(segunda_linha)}')
'''''''''


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
x = 2
pares = []
segunda = []
terceira = []

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares.append(matriz[linha][coluna])
if matriz[linha][1]:
    print(matriz[linha][1])
    segunda.append(matriz[linha][1])


print('-=' * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print(f'Os pares digitados foram {pares} e a soma entre eles é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {max(segunda)}')
