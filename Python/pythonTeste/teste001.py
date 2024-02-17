print('REALIZANDO SOMA')

while True:
    try:
        userPrimeiraResposta = float(input('Digite seu primeiro número: '))
        userSegundaResposta = float(input('Digite seu segundo número: '))
        somaDasRespostas = userPrimeiraResposta + userSegundaResposta
        break
    except (ValueError, TypeError) as erro:
        print('\nCaractere INVÁLIDO, repita, por favor, o processo.')
        print('Tipo de erro:', erro, '\n')

print('\nO resultado de sua soma é: {}'.format(somaDasRespostas))
