valores = [9, 8, 7, 12, 0, 13, 21]
pares = []
ímpares = []
for num in valores:
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)
print(f'Pares: {pares}')
print(f'ìmpares: {ímpares}')
