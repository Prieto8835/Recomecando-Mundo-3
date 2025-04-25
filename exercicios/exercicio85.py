num = []
pares = []
ímpares = []
for cont in range(0, 7):
    num.append(int(input(f'Digite o {cont + 1}° valor: ')))
for x in num:
    if x % 2 == 0:
        pares.append(x)
    else:
        ímpares.append(x)
num.clear()
pares.sort()
ímpares.sort()
num.append(pares[:])
num.append(ímpares[:])
pares.clear()
ímpares.clear()
print(f'Os valores pares foram: {num[0]}')
print(f'Os valores ímpares foram: {num[1]}')
print(f'Lista completa: {num}')


num = []
pares = []
impares = []
for cont in range(0, 7):
    x = int(input(f'Digite o {cont + 1}° valor: '))
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

num.append(pares[:])
num.append(impares[:])
pares.clear()
impares.clear()

num[0].sort()
num[1].sort()
print(f'Números pares {num[0]}')
print(f'Número ímpares {num[1]}')
