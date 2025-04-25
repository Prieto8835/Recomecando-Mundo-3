lista = []

num = int(input('Digite um valor: '))
lista.insert(0, num)
num1 = int(input('Digite um valor: '))
if num1 < num:
    lista.insert(0, num1)
else:
    lista.insert(1, num1)

num2 = int(input('Digite um valor: '))
if num2 < lista[0]:
    lista.insert(0, num2)
elif num2 > lista[0] and num2 < lista[1]:
    lista.insert(1, num2)
else:
    lista.insert(2, num2)

num3 = int(input('Digite um valor: '))   
if num3 < lista[0]:
    lista.insert(0, num3)
elif num3 > lista[0] and num3 < lista[1]:
    lista.insert(1, num3)
elif num3 > lista[1] and num3 < lista[2]:
    lista.insert(2, num3)
else:
    lista.insert(3, num3)

num4 = int(input('Digite um valor: '))
if num4 < lista[0]:
    lista.insert(0, num4)
elif num4 > lista[0] and num4 < lista[1]:
    lista.insert(1, num4)
elif num4 > lista[1] and num4 < lista[2]:
    lista.insert(2, num4)
elif num4 > lista[2] and num4 < lista[3]:
    lista.insert(3, num4)
else:
    lista.insert(4, num4)

print(lista)
#este primeiro código apresenta erro caso seja colocado números repetidos.
#quando é utilizado números diferentes ele funciona perfeitamente.
#segundo código não apresenta erros, funciona com números diversos e iguais.

lista = list()
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
print(f'Os valores em ordem são: {lista}')
