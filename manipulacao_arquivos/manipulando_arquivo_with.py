# Criando um novo arquivo

#Criando arquivo com suporte a caracteres especiais
with open("comida.txt", "w", encoding="utf-8") as comida:
    comida.write("Cachorro-Quente\n")
    comida.write("Coxão assado\n")
    comida.write("Lasanha\n")
    comida.write("Camarão Cozido\n")

#Consultando arquivo
with open("comida.txt", "r", encoding="utf-8") as comida:
    print(comida.read())
