from math import radians, sin, cos, tan

def confirmarResposta():
     print(f'{"PERGUNTA":=^50}')
     resposta = input('Deseja continuar ? (1:Sim/2:Não): ')
     if resposta == '1':
         return True
     else:
         return False

UserMessage = True

while UserMessage:
    print(f'\n{"CO, CA E TG DE ÂNGULOS":=^50}')
    while True:
        try:
            Angulo = float(input('Qual o ângulo ?: '))
            AnguloRadiano = radians(Angulo)
            Coseno = cos(AnguloRadiano)
            Seno = sin(AnguloRadiano)
            Tangente = tan(AnguloRadiano)
            break
        except (ValueError, TypeError, ZeroDivisionError) as erro:
            print(f'\n{erro}')
    print(f'{"RESULTADO":=^50}')
    print(f'Ângulo: {Angulo:.2f}°')
    print(f'Ângulo radiano: {AnguloRadiano:.2f} rad')
    print(f'Coseno: {Coseno:.2f}')
    print(f'Seno: {Seno:.2f}')
    print(f'Tangente: {Tangente:.2f}')

    UserMessage = confirmarResposta()
