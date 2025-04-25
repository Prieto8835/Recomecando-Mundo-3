compras = []
while True:
    produto = input('Produto: ')
    if produto == 'fim':
        break
    quantidade = int(input('Quantidade: '))
    preço = float(input('Preço: '))
    compras.append([produto, quantidade, preço])
soma = 0.0
for item in compras:
    print(f'{item[0]:20s} x Qntd: {item[1]:5d} Preço: {item[2]:5.2f} Total: {item[1] * item[2]:6.2f}')
    soma += item[1] * item[2]
print(f'Total: {soma:7.2f}')
 