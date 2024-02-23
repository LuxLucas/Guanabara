print(f'{"ALUGUEL DE CARROS":=^50}')
while True:
    try:
        kilometragem = float(input('Quantos KM foram percorridos com o veículo ?: '))
        quantidadeDeDias = float(input('Por quantos dias foi alugado ?: '))
        break
    except ValueError as erro:
        print(f'\n{"CARACTERE INVÁLIDO":=^50}')
print(f'\n{"RESULTADO":=^50}')
print("Kilômetros percorridos: {} Km".format(kilometragem))
print('Dias alugados: ', quantidadeDeDias)
print('Valor à pagar: R$ {:.2f}'.format((quantidadeDeDias * 60)+(kilometragem * 0.15)))
