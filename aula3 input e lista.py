#inputs
email = input("digite seu email: ")
celular = int(input("digite seu numero de celular: "))

print(f"seu telefone é {celular}, verifique seu email {email}, mandamos um codigo lá")
#listas
vendas = [50,100,200,40]

total_vendas = sum(vendas) #sum é somar
print(total_vendas)

tamanho_lista = len(vendas) #len mostra o tamanho da lista

print(max(vendas)) #maior valor da lista
print(min(vendas)) #menor valor da lista

print(vendas[0]) #pegar posição


#procurar produto na lista
lista_prod = ["banana" , "maça", "kauan"]

esc = input("qual produto deseja procurar? ")
esc = esc.lower() #vai deixar tudo em letra miniscula para dapara pesquisar

print(f"{esc}" in lista_prod) 
#adicionar produto na lista
add = input("o que voce pretende adicionar? ")
lista_prod.append(add)
print(lista_prod)

#remover produto
lista_prod.remove("kauan")
print(lista_prod) 


lista_prod.pop(0) #remove de acordo com a posição
print(lista_prod)

#editar um item
preco = ["1000" , "2000" , "3000"]
preco[0] = int(input("digite o novo valor: "))
print(preco)

#contar quantas vezes um item aparece na lista
print(lista_prod.count("maça"))

#ordenar um lista
lista_prod.sort() #ordena em ordem alfabetica
print(lista_prod)