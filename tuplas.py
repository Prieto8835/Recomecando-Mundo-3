lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
for comida in lanche:
    print(f'Eu comi {comida}')
print('~'*30)
for cont in range (0, len(lanche)):
    #Do 0 até o final, ou seja, até o len de lanche
    print(lanche[cont])  
    #lanche na posição cont
print('~'*30)
for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posição {pos}')
print('~'*30)
print('Em ordem alfabética ficaria: ')
print(sorted(lanche))
#função sorted para colocar em ordem alfabética 
print('~'*30)
a = (2, 4, 6, 8)
b = (1, 3, 5, 7)
c = a + b 
print(f'O número 5 aparece {c.count(5)} vezes em C')
#quantas vezes aparece o número 5 em C
print('~'*30)
print(f'O número 2 está na posição {c.index(2)}')
#aparece a posição em que se encotnra o número 2 levando em consideração a primeira vez em que ele aparece
print(f'O número 5 aparece na posição {c.index(5, 3)}')
#aqui ele mostra a posição do número 5 a partir da posição 3
print('~'*30)
#del(c)
#apaga o C
print('~'*30)
print(c)
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)
print('~'*30)
t1 = (1)
print(type(t1))
#caso não coloque vírgulo deve ser reconhecido como um inteiro
t1 = (1,)
print(type(t1))
#colocando a vírgula ele reconhece como uma tupla
t2 = ()
print(type(t2))
print(len(t2))
#colocando apenas os parênteses vazio já pode ser reconhecido como uma tupla
