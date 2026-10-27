"""
chave : valor -> dicionário

valor -> lista
"""
contatos = {"joão": 123, "maria":456, "josé":789} # dict()

print(type(contatos))

print(contatos)

#ADICIONAR ITENS AO DICIONÁRIO
#FORMA 1
contatos["marcia"] = 140

print(contatos)

#FORMA2
contatos.update({"arnaldo":894})# adicionando novo item
print(contatos)

contatos.update({"marcia":190})# atualizando um valor existente
print(contatos)


#EXCLUINDO DADOS DO DICIONÁRIO
#FORMA1
contatos.pop("joão")
print(contatos)

#FORMA2
del contatos["maria"]
print(contatos)

#EXCLUSÃO TOTAL DO DICIONÁRIO
contatos.clear()
print(contatos)
