import os


def limpar():
    # Limpa o console
    os.system('cls')


while True:

    # Testa se não haverá valores inválidos
    try:

        # Declaração de lista
        Nota = []
        # Controlador de loop
        contador = 0

        # Recebe notas
        while contador != 3:
            ValorInserido = float(input(f'Nota {contador+1}: '))

            # Se nota MAIOR que o permitido
            if ValorInserido > 10:
                ValorInserido = 10

            # Se nota MENOR que o permitido
            if ValorInserido < 0:
                ValorInserido = 0

            # Lista recebe nota
            Nota.append(ValorInserido)
            contador += 1

        break
    except (ValueError, TypeError) as TipoErro:
        limpar()
        print(f'\n{"VALOR INVÁLIDO":=^50}\n')

# Calculo de média
Media = sum(Nota)/3

# Verificação de situação do aluno
if Media >= 6:
    Situacao = 'APROVADO(A)'
elif Media >= 5:
    Situacao = 'EM RECUPERAÇÃO'
else:
    Situacao = 'REPROVADO'

print(f'{"RESULTADO":=^50}')

# Declaração dos resultados
print(f'Nota 01: {Nota[0]}')
print(f'Nota 02: {Nota[1]}')
print(f'Nota 03: {Nota[2]}')
print(f'Média Final: {Media:.2f}')
print(f'Situação: {Situacao}')
