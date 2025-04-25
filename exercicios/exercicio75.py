num = (int(input('Digite o primeiro valor: ')), int(input('Agora o segundo valor: ')),
       int(input('Digite o terceiro valor: ')), int(input('Digite o último valor: ')))
print(num)
print(type(num))
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu pela primeira vez na posição: {num.index(3) + 1}')
else:
    print('O valor 3 não foi encontrado ')
cont = pares = 0
print('Números pares:',end=' ')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')
        pares += 1
if pares == 0:
    print('Não foram encontrados números pares ')
