tentativas = 3

while True:
    codigo = input("Informe o código recebido: ")

    if codigo == "ab12" and tentativas > 0:# código correto
        print("Parabéns, senha correta")
        break # parando de repetir a estrutura

    # caso erre o código iremos retirar uma das suas tentativas
    if tentativas > 0:
        tentativas = tentativas - 1

    if tentativas <= 0:
        print("Sem tentativas, só lamento")
        break # encerrando a repetição