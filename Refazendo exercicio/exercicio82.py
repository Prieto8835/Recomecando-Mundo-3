num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while res not in ['S', 'N']:
        res = str(input('Opção inválida! [S/N]: ')).upper().strip()
    if res == 'N':
        print('Programa encerrado! ')
        break

for valor in num:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'Lista completa: {num}')
print(f'Lista dos pares: {pares}')
print(f'Lista dos impares: {impares}')

