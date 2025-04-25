lista = []
while True: 
    nome = str(input('Digite seu nome: '))
    nota1 = float(input('Digite sua 1° nota: '))
    nota2 = float(input('Digite sua 2° nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while res not in ['S', 'N']:
        res = str(input('Opção inválida! [S/N]: ')).upper().strip()
    if res == 'N':
        print('Programa encerrado! ')
        break

print(f'{'N°':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'*30)
for pos, valor in enumerate(lista):
    print(f'{pos:<4}{valor[0]:<10}{valor[2]:>8.1f}')
 
print('-' * 50)
while True:
    x = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if x == 999:
        print('FINALIZANDO... ')
        break
    if x <= len(lista) - 1:
        print(f'Notas de {lista[x][0]} são: {lista[x][1]}')
    else:
        print('Número inválido! Por favor selecione um correto.')
 