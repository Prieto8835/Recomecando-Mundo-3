lista = list()
while True:
    x = int(input('Digite um número: '))
    if x not in lista:
        lista.append(x)
        print(f'O valor {x} foi adicionado a lista com sucesso! ')
    else:
        print(f'O valor {x} já existe na lista portanto não adicionarei novamente! ')
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while res not in ['S', 'N']:
        res = str(input('Opção inválida! [S/N]: ')).upper().strip()
    if res == 'N':
        print('Programa encerrado! ')
        break

lista.sort()
print(f'A lista em sua ordem crescente fica: {lista}')

