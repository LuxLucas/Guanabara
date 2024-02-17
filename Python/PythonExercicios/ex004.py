import os

def verificarResposta():
    while True:
        resposta = input('\nDeseja repetir ? (1:SIM/0:NÃO):')
        if resposta.isnumeric():
            if resposta != '1' and resposta != '0':
                print('\nValor INVÁLIDO, responda novamente.')
            else:
                resposta = int(resposta)
                break
        else:
            print('\nValor INVÁLIDO, responda novamente.')
    return resposta

respostaUsuario = 1

while respostaUsuario == 1:
    variavelTestada = input('\nDigite algo para ser analisado: ')
    print('É um número ?:', variavelTestada.isnumeric())
    print('É alfabética ?:', variavelTestada.isalpha())
    print('É alfa-numérico ?:', variavelTestada.isalnum())
    print('É um espaço ?:', variavelTestada.isspace())
    print('É do tipo ASCII ?:', variavelTestada.isascii())

    respostaUsuario = verificarResposta()
