temp = []
pesos = []
principal = []
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(int(input('Digite seu peso: ')))
    principal.append(temp[:])
    #Função específica para separar os números inteiros de uma lista que contém também STR:
    for num in temp:
        if isinstance(num, int):
            pesos.append(num)
    temp.clear()
    res = str(input('Quer continuar? [S/N]? ')).strip().upper()
    while res not in ['S', 'N']:
        res = str(input('Opção inválida! [S/N]: ')).strip().upper()
    if res == 'N':
        print('Programa encerrado! ')
        break
print(f'Total de pessoas cadastradas foram: {len(principal)}')
print(f'As pessoas mais pesadas foram: ',end='')
for peso in principal:
    if peso[1] == max(pesos):
        print(f'{peso[0]} com {peso[1]}kg...',end='')
print()
print(f'As pessoas mais leves foram: ',end='')
for peso in principal:
    if peso[1] == min(pesos):
        print(f'{peso[0]} com {peso[1]}kg...',end='')
print()



#Considerando as pessoas mais pesadas com 100kg ou mais e as mais leves com 70kg ou menos:
temp = []
principal = []
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(int(input('Digite seu peso: ')))
    principal.append(temp[:])
    temp.clear()
    res = str(input('Quer continuar? [S/N]? ')).strip().upper()
    while res not in ['S', 'N']:
        res = str(input('Opção inválida! [S/N]: ')).strip().upper()
    if res == 'N':
        print('Programa encerrado! ')
        break
print(principal)
print(f'Total de pessoas cadastradas foram: {len(principal)}')
print(f'As pessoas mais pesadas foram: ',end='')
for peso in principal:
    if peso[1] >= 100:
        print(f'{peso[0]} com {peso[1]}kg...',end='')
print()
print(f'As pessoas mais leves foram: ',end='')
for peso in principal:
    if peso[1] <= 70:
        print(f'{peso[0]} com {peso[1]}kg...',end='')
print()

