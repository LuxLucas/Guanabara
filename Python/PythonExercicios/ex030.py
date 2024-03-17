# Importação da função 'trunc'
from math import trunc

# Recebe o número do usuário
Numero = trunc(float(input('Número inteiro: ')))

print(f'{"RESULTADO":=^50}')

# Verifica se o número é PAR ou ÍMPAR
if Numero % 2 == 0:
    print(f'Seu número, {Numero}, é PAR')
else:
    print(f'Seu número, {Numero}, é ÍMPAR')
