estoque = {"Tomate": [1000, 2.30],
           "Alface": [500, 0.45],
           "Batata": [2001, 1.20],
           "Feijão": [100, 1.50]
           }

vendas = list()

total = 0
while True:
    produto = (str(input('Digite o produto: ')))
    if produto in estoque:
        quantidade = int(input('Quantidade: '))
        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade
            print(f'{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}')
            print('~'*60)
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print('Quantidade solicitada não disponível! ')
    else:
        print('Produto não encontrado! ')
    res = str(input('Quer continuar? [S/N]? ')).upper().strip()
    while res not in ['S', 'N']:
        res = str(input('Resposta inválida! [S/N]: ')).upper().strip()
    if res == 'N':
        print('Programa encerrado! ')
        break

print('^'*60)
print(f'Custo total: R${total:21.2f}')
print('^'*60)
print('Estoque:')
for keys, values in estoque.items():
    print(f'Item: {keys}')
    print(f'Quantidade: {values[0]}')
    print(f'Preço: R${values[1]:6.2f}')
