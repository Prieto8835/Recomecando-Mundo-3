num = list()
for pos in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {pos}: ')))
print(f'Números digitados: {num}')
print(f'Maior número digitado {max(num)} nas posições {num.index(max(num))}')
print(f'Menor número digitado {min(num)} nas posições {num.index(min(num))}')






listanum = []

for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    mai = max(listanum)
    men = min(listanum)

print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')

print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
