dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
#para adicionar elementos a "dados"
dados['sexo'] = 'M'
print(dados)
#deletar elemento de "dados"
del dados['idade']
print(f'Dados com idade removido: {dados}')
print('~'*60)

filme = dict()
filme = {'Título': 'Star Wars', 'Ano': 1977, 'Diretor': 'George Lucas'}
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

for keys, values in filme.items():
    print(f'Na chave {keys} encontrei o valor {values}')
print('~'*60)

#adiciona os dois dicionários dentro de uma lista
lista = list()
lista.append(dados)
print(lista)
lista.append(filme)
print(lista)
#pode mostrar o print dessa lista de forma específica
print(f'No 2° dicionário o Título é: {lista[1]['Título']}')
print('~'*60)

pessoas = {'nome': 'Alejandro', 'sexo': 'M', 'idade': 22}
print(f'Dicionário: {pessoas}')
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('Keys: ')
for keys in pessoas.keys():
    print(keys)
print('~'*60)

print('Values: ')
for values in pessoas.values():
    print(values)
print('~'*60)

print('Keys e values: ')
for keys, values in pessoas.items():
    print(f'Na posição {keys} achei o valor {values}')
print('~'*60)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
    #função .copy() no dicionário semelhante ao fatiamento [:] usado em listas
    #para fazer a cópia sem criar uma relaçõa

print('~'*60)
for dados in brasil:
    print(dados)
print('~'*60)

print(f'Dicionário: {estado}')
print(f'Lista: {brasil}')
print('~'*60)

for e in brasil:
    print(e)
    print('^'*30)
    for keys, values in e.items():
        print(f'O campo {keys} tem valor {values}')

