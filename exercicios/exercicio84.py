temp = []
principal = []
mai = men = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Digite seu peso: ')))
    if len(principal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    principal.append(temp[:])
    temp.clear()
    res = str(input('Quer continuar [S/N]? ')).upper().strip()
    while res not in ['S', 'N']:
        res = str(input('Opção inválida! [S/N]: ')).upper().strip()
    if res == 'N':
        print('Programa encerrado! ')
        break

print(f'Total de pessoas cadastradas foram: {len(principal)}')
print(f'O maior peso foi {mai:.2f}kg da(s) pessoa(s):',end=' ')
for pessoa in principal:
    if pessoa[1] == mai:
        print(pessoa[0])
print(f'O menor peso foi {men:.2f}kg da(s) pessoa(s):',end=' ')
for pessoa in principal:
    if pessoa[1] == men:
        print(pessoa[0])

