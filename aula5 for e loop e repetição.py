num = int(input("quantas vezes se repete esse codigo:"))

for i in range(num): #menos usado
    o = input("digite seu nome")

#mais usada
lista_vendas = [1000 , 500 , 800, 1500, 2000, 2300]
meta = 1200
percentual_bonus = 0.1

for item in lista_vendas: #para cada item dentro da sua lista
    print(item) 

for venda in lista_vendas:
    if venda >= meta:
        bonus = venda * percentual_bonus
    else:
        bonus = 0
    print(f"O bonus do usuario é de {bonus}")