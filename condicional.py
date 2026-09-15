nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

#print("A média é: ", media)
"""
Comentário de 
mais de 1 linha
"""

if media >= 7:
    print(f"Sua média é {media:.2}, você passou")
elif media == 7:# elif é o mesmo que else if
    print(f"Sua média é {media:.2}, você passou arrastado")
else:
    print(f"Sua média é {media:.2}, você NÃO passou")
