dados = []
dados.append('Pedro')
dados.append(25)

pessoas = []
pessoas.append(dados[:])
print(pessoas)

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)
print(pessoas[0][1])
print('*'*60)

galera = [['João', 19], ['Ana', 13], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(pessoa[0])

for idade in galera:
    print(idade[1])

for p in galera:
    print(f'A pessoa {p[0]} tem {p[1]} anos de idade ')
print('*'*60)


grupo = list()
info = list()

for cont in range(0, 3):
    info.append(str(input('Nome: ')))
    info.append(int(input('Idade: ')))
    grupo.append(info[:])
    info.clear()
    #.clear para excluir dado

print(grupo)

galera = []
dado = []
maior = menor = 0
for cont in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'A {pessoa[0]} já é maior de idade! ')
        maior += 1
    else:
        print(f'{pessoa[0]} é de menor! ')
        menor += 1

print(f'Quantidade de maiores de idade: {maior}')
print(f'Quantidade de menores de idade: {menor}')
