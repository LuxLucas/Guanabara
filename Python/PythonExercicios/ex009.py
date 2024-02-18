print(f'{"TABUADA ATÉ 10":=^50}')
while True:
    try:
        tabuadaEscolhida = float(input('Escolha sua tabuada:'))
        break
    except (TypeError, ValueError) as erro:
        print(f'{"CARACTERE INVÁLIDO":=^50}')
print(f'{"RESULTADO":=^50}')
i = 1
while i <= 10:
    print('{} x {} = {}'.format(i, tabuadaEscolhida, i*tabuadaEscolhida))
    i += 1
print(f'{"FIM":=^50}')
