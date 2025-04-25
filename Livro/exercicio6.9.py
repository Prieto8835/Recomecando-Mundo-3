L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
v = int(input('Digite outro valor a procurar: '))
x = y = a = 0
encontrou = False
while x < len(L):
    if L[x] == p:
        y += 1
        encontrou = True
        break
    x += 1
if y == 1:
    print(f'{p} foi o primeiro a ser achado na posição {x}')
else: 
    x = 0
    while x < len(L):
        if L[x] == v:
            a += 1
            encontrou = True
            break
        x += 1
    if a == 1:
        print(f'{v} foi o primeiro a ser achado na posição {x}')
    elif not encontrou:
        print('Nenhum valor encontrado! ')

