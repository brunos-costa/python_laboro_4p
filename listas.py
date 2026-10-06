mercearia = ["Frutas", "Verduras", "Bebidas", "Carnes", "Água Sanitária"]

print(type(mercearia))
print(mercearia)

mercearia[4] = "Feijão"
print(mercearia)

#Exibindo a lista completa
for item in mercearia:
    print(item)

# Inserindo item no final da lista
mercearia.append("Batata")
print(mercearia)

# Inserindo item em qualquer lugar da lista
mercearia.insert(2,"Açúcar Mascavo")
print(mercearia)

#removendo o último item da lista
mercearia.pop()
print(mercearia)

#removendo qualquer item da lista
mercearia.pop(4)# remove o item de acordo com o índice.
print(mercearia)

mercearia.remove("Bebidas")
print(mercearia)
