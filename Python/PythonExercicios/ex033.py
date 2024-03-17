# Recebendo valores
Valores = [
    float(input('Valor 01: ')),
    float(input('Valor 02: ')),
    float(input('Valor 03: '))
]

# Propondo "maior" e "menor" para comparações
MaiorNumero = Valores[0]
MenorNumero = Valores[0]

# Compara se o segundo valor é maior que o "maior" valor
if Valores[1] > MaiorNumero:
    MaiorNumero = Valores[1]
else:
    MenorNumero = Valores[1]

# Compara o 'maior' valor com o terceiro
if Valores[2] > MaiorNumero:
    MaiorNumero = Valores[2]

# Compara o 'menor' valor com o terceiro
elif Valores[2] < MenorNumero:
    MenorNumero = Valores[2]

# Removo o maio e o menor valor, ficando apenas o médio
Valores.remove(MaiorNumero)
Valores.remove(MenorNumero)

print(f'{"RESULTADO":=^50}')

# Imprimindo resultados
print(f'Valor maior: {MaiorNumero}')
print(f'Valor médio: {Valores[0]}')
print(f'Valor menor: {MenorNumero}')

