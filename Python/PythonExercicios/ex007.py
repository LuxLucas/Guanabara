print(f'{"MÉDIA ALUNO PYTHON":=^50}')
primeiraNota = input('Primeira nota:')
segundaNota = input('Segunda nota:')
if primeiraNota.isnumeric():
    primeiraNota = float(primeiraNota)
else:
    while True:
        try:
            print(f'\n{"PRIMEIRA NOTA INVÁLIDA":=^50}')
            primeiraNota = float(input('Primeira nota:'))
            break
        except (TypeError, ValueError) as erro:
            print('ERRO:{}'.format(erro))
if segundaNota.isnumeric():
    segundaNota = float(segundaNota)
else:
    while True:
        try:
            print(f'\n{"SEGUNDA NOTA INVÁLIDA":=^50}')
            segundaNota = float(input('Segunda nota:'))
            break
        except (TypeError, ValueError) as erro:
            print('ERRO:{}'.format(erro))
print(f'{"MÉDIA":=^50}')
print('Primeira nota: {}\nSegunda nora: {}\nA média final é {}'.format(primeiraNota, segundaNota, (primeiraNota+segundaNota)/2))
print(f'{"FIM":=^50}')
