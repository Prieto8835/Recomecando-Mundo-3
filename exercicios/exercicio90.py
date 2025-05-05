dados = dict()
dados['nome'] = str(input('Escreva seu nome: '))
dados['media'] = float(input('Digite sua média: '))
print('~'*60)

print(f'Nome do aluno: {dados["nome"]}')
print(f'Média: {dados["media"]}')
if dados['media'] >= 7:
    print('Situação é igual a APROVADO! ')
else:
    print('Situação é igual  a REPROVADO! ')
