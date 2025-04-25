extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True: 
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('ERRO! Somente números entre 0 e 20. Tente novamente: '))
    print(f'O número {num} escrito por extenso fica: {extenso[num]}')
    res = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
    #strip para tirar os espaços e upper para deixar as letras em MAIÚSCULAS
    if res == 'N':
        print('Obrigado! Volte sempre! ')
        break
