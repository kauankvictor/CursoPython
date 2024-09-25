dic_produtos = {"s24 ultra": 7000 , "buds fe": 134 , "s22 ultra": 4700}

#pegar um elemento
print(dic_produtos["s24 ultra"])

#editar um elemento
dic_produtos["s24 ultra"] = 2000

#quqantidad de itens
print(len(dic_produtos))

#retirar um item
dic_produtos.pop("s24 ultra")
print(dic_produtos)

#adicionar um item no dicionario
dic_produtos["a71"] = 1900
print(dic_produtos)

#verificar se um item existe no dicionario
item = input("Qual item deseja procurar? ")
item = item.lower()
if item in dic_produtos:
    print("existe produto")
else:
    print("não existe") 

#exercicio
dic_prod = {"macarrao" : 4 , "arroz" : 7}

nome_prod = input("Nome do produto: ")
preco_prod = float(input("Preço do produto: "))
nome_prod = nome_prod.lower()

dic_prod[nome_prod] = preco_prod
print(dic_prod)

for produto in dic_prod:
    novo_preco = dic_prod[produto] * 1.1
    dic_prod[produto] = novo_preco
    print(dic_prod)