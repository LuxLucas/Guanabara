from math import hypot

def confirmarResposta():
     print(f'{"PERGUNTA":=^50}')
     resposta = input('Deseja continuar ? (1:Sim/2:Não): ')
     if resposta == '1':
         return True
     else:
         return False
     
userMessage = True
while userMessage == True:
    print(f'\n{"TEOREMA DE PITÁGORAS":=^50}')
    while True:
        try:
            catetoOposto = float(input('Digite o valor do cateto oposto: '))
            catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
            hipotenusa = hypot(catetoOposto, catetoAdjacente)
            break
        except ValueError as erro:
            print(f'\n{"CARACTERE INÁLIDO, REPITA":=^50}')
    print(f'{"RESPOSTA":=^50}')
    print('Cateto Oposto: {}\nCateto Adjacente: {}\nHipotenusa: {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))
    userMessage = confirmarResposta()
