Numero = input('Digite um número de 0 a 9999: ').lstrip('0')

if len(Numero) == -1:
    Numero = '0'

Numero = Numero[::-1]
indice = 0

while indice != len(Numero):
    if indice == 0:
        print(f'UNIDADE(S): {Numero[indice]}')

    if (indice == 1) and (Numero[indice] != ''):
        print(f'DEZENAS(S): {Numero[indice]}')

    if (indice == 2) and (Numero[indice] != ''):
        print(f'CENTENA(S): {Numero[indice]}')

    if (indice == 3) and (Numero[indice] != ''):
        print(f'MILHAR(ES): {Numero[indice]}')

    indice += 1

#   Maneira "Matemática" de se fazer:
"""
Numero = int(input('Digite um número de 0 a 9999: '))

Unidade = (Numero // 1) % 10
Dezena = (Numero // 10) % 10
Centena = (Numero // 100) % 10
Milhar = (Numero // 1000) % 10

print(f'{"RESPOSTA":=^50}')

print(f'UNIDADE(S): {Unidade}')
print(f'DEZENA(S): {Dezena}')
print(f'CENTENA(S): {Centena}')
print(f'MILHAR(ES): {Milhar}')
"""

