times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Vitória', 
'Atlético Mineiro', 'Fluminense', 'Grêmio', 'Juventude', 'Red Bull Bragantino', 'Athletico Paranaense', 'Criciúma', 'Atlético Goianiense', 'Cuiabá')
print(f'Os 5 primeiros times da tabela são: {times[:5]}')
print(f'Os 4 útlimos colocados são: {times[-4:]}')
print(f'Em ordem alfabética ficaria: {sorted(times)}')
print(f'O time do Juventude está em {times.index('Juventude') + 1}° colocado')
