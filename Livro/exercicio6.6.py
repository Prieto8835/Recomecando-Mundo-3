último = 10
último_2 = 10
fila = list(range(1, último + 1))
fila_2 = list(range(1, último_2 + 1))
while True:
    print(f'Existem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print(f'Existem {len(fila_2)} clientes na fila 2')
    print(f'Fila 2 atual: {fila_2}')
    print(f'Digite F para adicionar um cliente ao fim da fila 1, G para fila 2')
    print(f'ou A para realizar o atendimento da fila 1, B para fila 2. S para sair. ')
    operação = input('Operação(F, A, G, B ou S): ')
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == 'A':
            if len(fila) > 0:
                atendido1 = fila.pop(0)
                print(f'Cliente {atendido1} atendido')
            else:
                print('Fila vazia! Ninguém para atender. ')
        elif operação[x] == 'B':
            if len(fila_2) > 0:
                atendido2 = fila_2.pop(0)
                print(f'Cliente {atendido2} atendido')
            else:
                print(f'Fila vazia! Ninguém para atender. ')
        elif operação[x] == 'F':
            último += 1 #incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == 'G':
            último_2 += 1
            fila_2.append(último_2)
        elif operação[x] == 'S':
            print('Programa encerrado! ')
            sair = True
            break
        else:
            print('Operação inválida! Digite apenas F, A ou S! ')
        x += 1
    if sair:
        break
