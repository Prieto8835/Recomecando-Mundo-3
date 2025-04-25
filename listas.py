"""""""""
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
print(lanche[2])
lanche[3] = 'Picolé'
#substitui na posição 3 o pduim por picolé
print(lanche)
lanche.append('Biscoito')
#acrescenta biscoito em lanche, na última posição
print(lanche)
lanche.insert(0, 'Hot Dog')
#na posição 0 ele adiciona hot dog e reagrupa as demais em ordem
print(lanche)
del(lanche[3])
#deleta o item na posição 3
print(lanche)
lanche.pop()
#elimina o último elemento. Pode ser usado também pra remover um item na posiçaõ específica
lanche.pop(2)
print(lanche)
lanche.remove('Hot Dog')
#remove da lista o item hot dog
print(lanche)
if 'Pizza' in lanche:
    lanche.remove('Pizza')
    print(lanche)
#lista.index() mostra a posição do valor
print('-'*60)

valores = list(range(4, 11))
print(valores)  
print(len(valores))
#mostra quantidade de elementos em valores
valores = [0, 9, 5, 6, 3]
valores.sort()
#ordena os valores
print(valores)
valores.sort(reverse=True)
#ordena os valores em ordem decrescente
print(valores)
valores.insert(2, 0)
#adiciona na posição 2 o número 0
print(valores)
while 0 in valores:
    valores.remove(0)
print(valores)
print('-'*60)

lista = []
cont = numero = 0
while cont < 4:
    lista.append(numero)
    cont += 1
    numero += 2
for pos, num in enumerate(lista):
    print(f'Na posição {pos} encontrei o valor: {num}! ')
#enumerate muito usado pra citar a posição e o valor específico 
print('-'*60)

a =[2, 4, 6, 8]
b = a[:]
#duplica a lista mas caso algo seja alterado vai ser somente em uma
b[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
"""""""""



lista = []
lista.append('ITEM')
lista.append('SAL')
lista.append('AÇÚCAR')
lista.insert(0, 'Mouse') #na posição 0 adiciona o 'Mouse'
print(lista)
del lista[0] #apaga o valor da posição 0
lista.pop(1) #apaga o valor da posição 1
if 'AÇÚCAR' in lista:
    lista.remove('AÇÚCAR') #apaga o item em específico 'AÇÚCAR'
    print('AÇÚCAR foi removido com SUCESSO! ')
else:
    print('Item não encontrado! Não vou apagá-lo! ')
print(lista)
print('~' * 30)


valores = list(range(4, 11))
print(valores)
from random import randint
cont = 0
num = []
while cont < 5:
    num.append(randint(0, 99))
    cont += 1
print(f'Fora de ordem: {num}')
num.sort()
print(f'Em ordem crescente: {num}')
num.sort(reverse=True)
print(f'Em ordem decrescente fica: {num}')
print(f'A lista num possui {len(num)} valores ')
#função len para contar quantos elementos possui em uma lista
for valor in num:
    print(f'{valor}...',end='')
print()
for pos, valor in enumerate(num):
    print(f'Na posição {pos} encontrei o valor {valor}! ')



