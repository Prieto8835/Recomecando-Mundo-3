L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
x = y = 0
while x < len(L):
    if L[x] == p:
        y += 1
        break
    x += 1

if y == 1:
    print(f'{p} achado na posição {x}')
else:
    print(f'{p} não encontrado! ')




L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar:"))
x = 0
while x < len(L):
    if L[x] == p:
        break
    x += 1
if x < len(L):
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")