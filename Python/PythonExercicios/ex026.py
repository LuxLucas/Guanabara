# Poderia ter usado A.rfind()

# Recebe uma palavra
Palavra = input('Digite uma palavra: ').upper().strip()

# Quantidade de "A" na palavra
Quantidade = Palavra.count('A')

# Primeira posição que aparece "A" na palavra
PosicaoInicial = Palavra.find('A')

# Verifica a última posição de "A" na palavra
if Quantidade > 1:
    PosicaoFinal = (len(Palavra) - 1) - (Palavra[::-1].find('A'))
else:
    PosicaoFinal = PosicaoInicial

print(f'{"RESPOSTA":=^50}')

# Retorna os resultados
print(f'Quantidade de "A": {Quantidade}')
print(f'Posicao inicial de "A": {PosicaoInicial}')
print(f'Posicao final de "A": {PosicaoFinal}')
