dados = dict()
partidas = list()
lista = list()
cont = 0
while True:
    dados['Nome'] = str(input('Digite seu nome: '))
    qntd = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
    while cont < qntd:
        partidas.append(int(input(f'Quantos gols na partida {cont + 1}? ')))
        cont += 1
    dados['Gols'] = partidas[:]
    dados['Total'] = sum(partidas)
    partidas.clear()
    lista.append(dados.copy())
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while res not in ['S', 'N']:
        res = str(input('Opção inválida! Selecione apenas S ou N: ')).upper().strip()
    if res == 'S':
        cont = 0
    elif res == 'N':
        print('Programado encerrado! ')
        print('~'*60)
        break
    print('~'*60)

print(f'COD   NOME               GOLS         TOTAL')
print('-'*60)
for i, v in enumerate(lista):
    print(i,end='   ')
    for keys, values in v.items():
        print(f'{values}      ',end='')
    print()
      
while True:
    jog = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if jog == 999:
            print('Programa encerrado! ')
            break
    if jog >= len(lista):
        print(f'Nenhum jogador com código {jog} encontrado! ')
    for i, v in enumerate(lista):
        if jog == i:
            for dados, jogador in v.items():
                print(f'{dados} = {jogador}',end=' - ')
            print()      
