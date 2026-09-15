texto = input("Informe um texto qualquer: ")
#print(len(texto))

if len(texto) > 10:
    print(texto[:10])# estou exibindo todo o texto até o 10º caracter
else:
    print(texto)