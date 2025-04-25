T = [-10, -8, 0, 1, 2, 5, -2, -4]
mínimo = T[0]
máximo = T[0]
soma = 0
for temp in T:
    if temp < mínimo:
        mínimo = temp
    if temp > máximo:
        máximo = temp
    soma += temp
print(f'Temperatura mínima: {mínimo}°')
print(f'Temperatura máxima: {máximo}°')
print(f'Média da temperatura é {soma/len(T)}° ')
