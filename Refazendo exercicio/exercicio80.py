lista = list()
for valor in range(0, 5):
    x = int(input('Digite um valor: '))
    if valor == 0 or x > lista[-1]:
        lista.append(x)
    else:
        pos = 0
        while pos < len(lista):
            if x <= lista[pos]:
                lista.insert(pos, x)
                break
            pos += 1
print(f'Lista em ordem: {lista}')

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista! ')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista! ')
                break
            pos += 1

print(f'Os valores digitados em ordem foram: {lista}')


lista = list()
for valor in range(0, 5):
    x = int(input('Digite um valor: '))
    if valor == 0 or x > lista[-1]:
        lista.append(x)
    else:
        for pos, v in enumerate(lista):
            if x <= lista[pos]:
                lista.insert(pos, x)
                break

print(f'Lista em ordem: {lista}')
