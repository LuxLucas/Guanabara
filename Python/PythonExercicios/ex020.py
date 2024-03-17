#   Importa a biblioteca
import random
#   Função que retorna um valor para o UserMessage
def confirmarResposta():
     print(f'{"PERGUNTA":=^50}')
     resposta = input('Deseja continuar ? (1:Sim/2:Não): ')
     if resposta == '1':
         return True
     else:
         print('\n')
         return False
#   Controlador do "While" primário    
UserMessage = True
#   "While" primário, responsável por reexecutar o programa
while UserMessage:
#   Declaração de vetores
    NomeAluno = []
    OrdemAluno = []

    print(f'\n{"SORTEIO DE ALUNOS":=^50}')
#   "While" secundário que recebe os nomes
    while True:
        try:
            for i in range(4):
                NomeAluno.append(input('Digite o nome do aluno {}: '.format(i+1)))
            else:
                break
        except (TypeError, ValueError) as erro:
            print(f'\n{"CARACTERE INVÁLIDO":=^50}')
            print(erro, '\n')

    print(f'{"SORTEANDO ORDEM":=^50}')
#   "While" secundário que sorteia os nomes
    while len(OrdemAluno) < 4:
        LimiteSorteio = len(NomeAluno) - 1
        NumeroSorteado = random.randint(0, LimiteSorteio)
        OrdemAluno.append(NomeAluno[NumeroSorteado])
        NomeAluno.remove(NomeAluno[NumeroSorteado])

    print(f'Alunos: {OrdemAluno}')
    Posicao = 1
#   "For" responsável por imprimir resultado
    for i in OrdemAluno:
        print(f'{Posicao}° Aluno: {i}')
        Posicao += 1
#   UserMessage recebendo um novo valor
    UserMessage = confirmarResposta()
