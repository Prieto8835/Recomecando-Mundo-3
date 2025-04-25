larg = 60
print('-'*60)
print('Tabela de preços'.center(larg))
print('-'*60)
itens = ('Lápis', '1.75', 'Borracha', '2.00')
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}',end='')
    else:
        print(f'R${float(itens[pos]):>8.2f}')
