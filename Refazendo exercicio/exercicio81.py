lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while res not in ['S', 'N']:
        res = str(input('Opção inválida! [S/N]: ')).upper().strip()
    if res == 'N':
        print('Programa encerrado! ')
        break

print(f'Total de números digitados foram {len(lista)}')
lista.sort(reverse=True)
print(f'A lista em ordem descrescente fica: {lista}')
if 5 in lista:
    print('O número 5 foi adicionado a lista! ')
else:
    print('Não foi encontrado o número 5 na lista! ')
