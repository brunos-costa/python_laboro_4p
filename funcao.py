#1. FUNÇÃO SEM PARÂMETRO E SEM RETORNO
def exibirNome():
    nome = input("Qual o seu nome? ")
    print(f"Olá {nome}, tudo bom?")

#Chamando a função
#exibirNome()
#-------------------------------------------------------

#2. FUNÇÃO COM PARÂMETRO E SEM RETORNO
def somar(num1, num2):
    print(f"A soma é: {num1 + num2}")

#Chamando a função
somar(10,2)
#-------------------------------------------------------------

#3. FUNÇÃO SEM PARÂMETRO E COM RETORNO
def dobro():
    valor = float(input("Informe um valor numérico qualquer: "))
    resposta  = valor * 2
    return resposta

#Chamando a função

print(f"O dobro é {dobro()}")