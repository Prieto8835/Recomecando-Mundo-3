lista = [[],[]]
for cont in range(0, 7):
    x = int(input(f'Digite um valor para a posição {cont + 1}: '))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
print(f'Lista completa com todos valores: {lista}')

