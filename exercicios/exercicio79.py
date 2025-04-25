lista = []
res = 'S'
while res == 'S':
    lista.append(int(input('Digite um valor: ')))
    res = input('Valor adicionado com SUCESSO! Quer continuar? [S/N]? ').upper().strip()    
    while res not in ['S', 'N']:
        res = input('ERRO! Digite novamente [S/N]: ').upper().strip()
    if res == 'N':
        print('Programado ENCERRADO!')
        break
listav2 = []
for pos, n in enumerate(lista):
    if lista[pos] not in listav2:
        listav2.append(n)
print(f'Valores digitados foram {lista}')
listav2.sort()
print(f'Valores sem repetir e em ordem: {listav2}')
