idade = []
peso = []
dados = []
while True:
    idade.append(int(input('Quantos anos você tem? ')))
    peso.append(int(input('Quantos kg você tem? ')))
    res = input('Quer continuar? [S/N]? ').upper().strip()
    while res not in ['S', 'N']:
        res = input('Opção inválida! [S/N]: ').upper().strip()
    if res == 'N':
        print('Programa encerrado! ')
        break
    
for x in idade:
    if x not in dados:
        dados.append(x)

for y in peso:
    if y not in dados:
        dados.append(y)

idade.clear()
peso.clear()

print(f'Dados finais: {dados}')

