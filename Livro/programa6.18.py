produto1 = ['maça', 10, 0.30]
produto2 = ['pera', 5, 0.75]
produto3 = ['kiwi', 4, 0.98]
compras = [produto1, produto2, produto3]
for item in compras:
    print(f'Produto {item[0]}')
    print(f'Quantidade: {item[1]}')
    print(f'Preço: {item[2]:5.2f}')
