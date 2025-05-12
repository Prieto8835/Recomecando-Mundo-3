from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de trabalho (0 caso não tenha): '))

if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados["Ano de Contratação"] + 35) - datetime.now().year)
print('~'*60)

for keys, values in dados.items():
    print(f'{keys} = {values}')
