dados = dict()
lista = list()

while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    while dados['Sexo'] not in ['M', 'F']:
        dados['Sexo'] = str(input('ERRO! Apenas M ou F: ')).upper().strip()
    dados['Idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while res not in ['S', 'N']:
        res = str(input('Resposta inválida! Apenas S ou N: ')).upper().strip()
    if res == 'N':
        print('Programa encerrado! ')
        break
print('~'*60)

media = 0
print(f'Total de pessoas cadastradas: {len(lista)}')
for anos in lista:
    media += anos['Idade']
print(f'Média de idade é: {media/len(lista):.2f}')
print('~'*60)

print('Mulheres cadastradas: ')
for mulher in lista:
    if mulher['Sexo'] == 'F':
        print(f'-----> {mulher["Nome"]}')
print('~'*60)

print('Pessoas acima da média de idade: ')
for acima in lista:
    if acima['Idade'] >= media/len(lista):
      print(f'-----> {acima["Nome"]}')
