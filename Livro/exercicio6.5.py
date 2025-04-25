último = 10
fila = list(range(1, último + 1))
while True:
    print(f'Existem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print(f'Digite F para adicionar um cliente ao fim da fila,')
    print(f'ou A para realizar o atendimento. S para sair. ')
    operação = input('Operação(F, A ou S): ')
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} atendido')
            else:
                print('Filza vazia! Ninguém para atender. ')
        elif operação[x] == 'F':
            último += 1 #incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == 'S':
            print('Programa encerrado! ')
            sair = True
            break
        else:
            print('Operação inválida! Digite apenas F, A ou S! ')
        x += 1
    if sair:
        break
