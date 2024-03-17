# Importação de bibliotecas/módulos
from random import randint
from time import sleep

# Número int escolhido pelo usuário
NumeroUsuario = int(input('Escola um número entre 0 a 5: '))

# Número int sorteado para o computador
NumeroComputador = randint(0, 5)

# Faz o programa aguardar alguns segundos
sleep(2)

print(f'{"RESULTADO":=^50}')

# Comparação entre os números
if NumeroUsuario == NumeroComputador:
    print('COMPUTADOR VENCEU')
else:
    print('VOCÊ VENCEU')

# Mostrando os números de ambos
print(f'Seu número: {NumeroUsuario}')
print(f'Computador número: {NumeroComputador}')
