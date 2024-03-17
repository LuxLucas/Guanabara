from random import randint


def confirmar_resposta():
    print(f'{"PERGUNTA":=^50}')
    resposta = input('Deseja continuar ? (1:Sim/2:Não): ')
    if resposta == '1':
        return True
    else:
        print('\n')
        return False


NomeAluno = []
UserMessage = True

while UserMessage:
    print(f'\n{"SORTEIO DE ALUNOS":=^50}')
    while True:
        try:
            for i in range(4):
                NomeAluno.append(input(f'Digite o nome do aluno {i+1}: '))
            else:
                break
        except (TypeError, ValueError) as erro:
            print(f'\n{"CARACTERE INVÁLIDO":=^50}')
            print(erro, '\n')

    print(f'{"ALUNO SORTEADO":=^50}')
    NumeroSorteado = randint(0, 3)
    print(f'Aluno {NumeroSorteado+1}: {NomeAluno[NumeroSorteado]}')
    UserMessage = confirmar_resposta()
