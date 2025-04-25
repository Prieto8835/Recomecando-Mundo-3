lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    res = input('Quer continuar? [S/N]? ').upper().strip()
    while res not in ['S', 'N']:
        res = input('OPÇÃO INVÁLIDA! Selecione uma correta: [S/N]: ').upper().strip()
    if res == 'N':
        print('Programado ENCERRADO! ')
        break

print(f'Números digitados foram: {lista}')
print(f'Total de números digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Em ordem decrescente fica: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na lista! ')
else:
    print('O valor 5 não foi encontrado na lista! ')
