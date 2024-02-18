print(f'{"SUCESSOR E ANTECESSOR INTEIROS":=^50}')
while True:
    try:
        numero = int(input('Digite seu número:'))
        break
    except ValueError as erro:
        print(f'\n{"Valor INVÁLIDO, repita":=^50}')
print('Anterior de {} é {} \nSucessor de {} é {}'.format(numero, numero-1, numero, numero+1))

