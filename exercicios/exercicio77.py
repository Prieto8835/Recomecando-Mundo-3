palavras = ('abacaxi', 'caixa', 'flor', 'janela', 'caminho', 'sol', 'fogo', 'gato', 'livro', 
            'escola', 'banco', 'amigo', 'tempo', 'cidade', 'piano')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    vogais = 0
    for letra in p:
    #for letra in p para analisar cada letra
        if letra.lower() in 'aeiou':
            vogais += 1
            print(letra.upper(),end=' ')
    print(f'totalizando {vogais} vogais nessa palavra! ')
