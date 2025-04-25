linha = []
coluna = []
for x in range(0, 3):
    
    for y in range(0, 3): 
            linha.append(int((input(f'Digite um valor para a linha {x}: '))))
            coluna.append(int(input(f'Digite um valor para a coluna {y}: ')))


print(linha)
print(coluna)

