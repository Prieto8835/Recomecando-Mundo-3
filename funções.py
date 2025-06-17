def soma(a, b):
    s = a + b
    print(f'A soma dos valores {a} + {b} = {s}')

soma (4, 5)
soma (8, 9)
soma (2, 4)
#pode especificar os valores de cada letra:
soma(b=3, a=5)

#desempacotamento
print('-' * 60)
def contador(* num ):
    for valores in num:
        print(f'{valores}...', end='')
    print(f'Total de {len(num)} valores.')
    print()

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print('-' * 60)

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
        
valores = [6, 3, 9, 1, 0, 2]
print(f'Valores originais: {valores}')
dobra(valores)
print(f'Valores dobrados: {valores}')
