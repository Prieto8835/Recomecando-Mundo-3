lista = []
maior = menor = 0
for pos in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {pos}: ')))
    if pos == 0:
        maior = menor = lista[pos]
    else:
        if lista[pos] < menor:
            menor = lista[pos]
        if lista[pos] > maior:
            maior  = lista[pos]

print(f'Lista completa: {lista}')
print(f'Maior valor: {maior}! Apareceu na(s) posição(ões): ',end='')
for pos, valor in enumerate(lista):
    if valor == maior:
        print(f'{pos}...',end='')
print()
print(f'Menor valor: {menor}! Apareceu na(s) posição(ões): ',end='')
for pos, valor in enumerate(lista):
    if valor == menor:
        print(f'{pos}...',end='')
print()


num = []
for p in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {p}: ')))
    
print(f'Lista completa: {num}')
print(f'Maior valor foi: {max(num)} encontrado na(s) posição(ões): ',end='')
for pos, valor in enumerate(num): 
    if valor == max(num):
        print(f'{pos}...',end='')
print()
print(f'Menor valor foi: {min(num)} encontrado na(s) posição(ões): ',end='')
for pos, valor in enumerate(num):
    if valor == min(num):
        print(f'{pos}...',end='')
print()



lista = []
for pos in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {pos}: ')))

print(f'O maior valor digitado foi {max(lista)} e está na(s) posição(ões) ',end='')
for pos, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{pos}...',end='')
print()
print(f'O menor valor digitado foi {min(lista)} e está na(s) posição(ões) ',end='')
for pos, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{pos}...',end='')
print()

