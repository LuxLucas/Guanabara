# Recebe valor da velocidade
Velocidade = float(input('Velocidade capturada (KM/h): '))

print(f'{"RESULTADO":=^50}')

# Verifica se passou da velocidade máxima
if Velocidade > 80:

    # Calcula valor da multa
    Multa = (Velocidade - 80) * 7

    print(f'Meliante deve R$ {Multa:,.2f}')
else:
    print(f'Tudo em ordem')
