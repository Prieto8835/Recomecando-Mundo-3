lista = []
x = input('Digite uma expressão: ')
for parenteses in x:
    if parenteses == '(':
        lista.append(')')
    elif parenteses == ')':
        if len(lista) > 0:
            lista.pop(-1)
        else:
            print('Expressão inválida! ')
            break
else:
    if len(lista) > 0:
        print('Expressão inválida! ')
    else:
        print('Expressão correta! ')

