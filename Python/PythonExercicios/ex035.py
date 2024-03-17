# Recebendo segmentos
Segmentos = [
    float(input('Segmento 01: ')),
    float(input('Segmento 02: ')),
    float(input('Segmento 03: '))
]

# Declarando maior segmento
MaiorSegmento = max(Segmentos)

# Retirando o maior segmento da lista
Segmentos.remove(MaiorSegmento)

# Soma os segmentos restantes
SomaRestante = sum(Segmentos)

print(f'{"RESULTADO":=^50}')

# Imprimindo resultado
if MaiorSegmento > SomaRestante:
    print('NÃO É POSSÍVEL criar um triângulo')
else:
    print('É POSSÍVEL criar um triângulo')
