lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    res = input('Quer continuarw [S/N]? ').upper().strip()
    while res not in ['S', 'N']:
        res = input('Resposta INVÁLIDA! Selecione uma opção CORRETA: [S/N]: ').upper().strip()
    if res == 'N':
        print('Programado ENCERRADO! ')
        break
print(f'Valores digitados: {lista}')

pares = []
impares = []

for pos, n in enumerate(lista):
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Lista dos números pares: {pares}')
print(f'Lista dos números ímpares: {impares}')
