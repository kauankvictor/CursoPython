# > maior que
# < menor que
# >= maior ou igual 
# <= menor ou igual
# == igual
# != diferente 

vendas = 1500
meta = 1300

if vendas > meta:
    print("Vendedor ganha bonus: ")
else:
    print("vnededor não ganha bonus! ") 

#2º cenario
venda = 1500
meta1 = 1300 #ganha 10%
meta2 = 2000 #ganah 13%

if venda >= 2000:
    bonus = 0.10 * vendas
else:
    if venda >= 1300:
        bonus = 0.10 * vendas
    else:
        bonus = 0
print("Bonus: ", bonus)

#ou pode utilizar um elif, pode usar quantos elif quiser no meio do if e else

lista_produtos = ["celular" , "notebook" , "carro"]
procurar = input("qual item deseja procurar? ")
procurar = procurar.lower()

if procurar in lista_produtos: #se procurar estiver dentro de lista_produtos
    print("temos esse produto")
else:
    print("não temos esse produto")