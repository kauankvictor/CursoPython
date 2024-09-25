faturamento = 1000
custo = 700
lucro = faturamento-custo

print(f"faturamento da empresa: {faturamento}, custo: {custo}, lucro: {lucro} ")

# Deixar todas as letras maiusculas
email_cliente = "kauanvictor184@gmail.com"
email_cliente = email_cliente.upper()
print(email_cliente)

#deixar todas as letras minusculas
email_cliente = "kauanvictor184@gmail.com"
email_cliente = email_cliente.lower()
print(email_cliente)

#procurar algum elemento dentro do seu texto (dará a posição)
print(email_cliente.find("@")) # -1 quando não for encontrado

# tamanho do texto
print(len(email_cliente))

#pegar um caracterer do texto
print(email_cliente[4]) #o numero é a posição do caracter no texto

#pegar um pedaço do texto
print(email_cliente[:4]) #ira exibir ate o caracter 4
print(email_cliente[1:4]) #começa de um caracter e vai ate o outro
#lembrando que sempre começa do indice 0, no caso o nome kauan, o K vai ser 0, o A 1, o U 2 e assim por 

#trocar um pedaço do texto
novo_email = email_cliente.replace("gmail.com", "hotmail.com") #qual parte do texto voce quer trocar, e depois por qual quer substituir
print(novo_email)

#trabalhar com nomes
nome = "kauan victor"
print(nome.capitalize()) #deixa a primeira letra do texto maiuscula
print(nome.title()) #deixa todas as primeiras letras das palavras maiusculas

#exercicio
posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)

#exibir primeiro e segundo nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
print(primeiro_nome)

sobrenome = nome[posicao_espaco:]
print(sobrenome)

print("miau")
