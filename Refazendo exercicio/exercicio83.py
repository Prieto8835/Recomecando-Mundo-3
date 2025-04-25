exp = str(input('Digite uma expressão matemática: '))
pilha = list()
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) > 0:
    print('Sua expressão está inválida! ')
else:
    print('Sua expressão está válida! ')

#pego de um comentário do vídeo no YouTube
expre = str(input('Digite a expressao: '))
cont = 0 # 0 Seria o equilibrio,
# Se no final continuar zero o numero de abre e
# fecha são iguais, se ele ficar negativo quer dizer
# que fechou parenteses antes da hora

for x in expre:
    if x == '(':
        cont += 1
    elif x == ')':
        cont -= 1
        if cont < 0: ## Fechou antes de abrir
            print('Expressao invalida')
            exit(0) # Termina programa

if cont != 0: ## Tem parenteses sem seu par
    print('Expressao invalida')
else:
    print('Expressao valida')
