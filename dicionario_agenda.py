agenda = dict()# Criando um dicionário vazio

while True:
    print("\nAgenda Eletrônica\n")
    print("1 - Inserir")
    print("2 - Excluir")
    print("3 - Consultar")
    print("4 - Sair")

    escolha = input("Qual sua escolha? ")
    if escolha == "1":
        nome = input("Informe o nome do contato: ")
        agenda[nome] = int(input(f"Qual o número de {nome}: "))

        print("Contato inserido com sucesso!")
        print(agenda)

    elif escolha == "2":

        resposta = input("Informe qual contato você deseja excluir: ")

        del agenda[resposta]

        print(f"O contato {resposta} foi excluído com sucesso")
        print(agenda)
        
    elif escolha == "3":
        for chave, valor in agenda.items():
            print(f"{chave}: {valor}")

    elif escolha == "4":
        break
    else:
        print("Opção inválida")        
        input("\nAperte qualquer tecla para continuar...")
        