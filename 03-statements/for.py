# O for serve para percorrer itens de uma coleção (como uma lista ou um dicionário) e realizar a mesma ação para cada um desses itens

# Estrutura: for item in lista:

# Indentação: 
# Assim como no if, tudo o que deve ser repetido precisa estar com um recuo (Tab) para dentro do for.

# Formas de usar o For:
# For com range()
# Usado quando você quer repetir algo por uma quantidade específica de vezes.


for i in range(10):
    print("Se inscreve no canal") # Vai imprimir 10 vezes

#Exemplo:
# For para Percorrer Listas (Mais comum)
# Neste formato, atribui o valor de cada item da lista a uma variável temporária a cada repetição.


vendas = [1000, 500, 800, 1500]

for venda in vendas:
    print(venda) # Imprime cada valor da lista individualmente


# Exemplo: Cálculo de Bônus Automático
# calcular o bônus de 10% para uma lista de funcionários, mas apenas para aqueles que bateram uma meta de 1.200.

#Criamos a lógica para um item: Primeiro, definimos como calcular o bônus de uma única venda.
#Colocamos dentro do For: essa lógica no loop para que ela rode para a lista toda.

vendas = [1000, 500, 800, 1500, 2000, 2300]
meta = 1200
percentual_bonus = 0.10

for venda in vendas:
    if venda >= meta:
        bonus = venda * percentual_bonus
    else:
        bonus = 0
    print(f"Bônus calculado: {bonus}")

# essa estrutura permite processar dados de 1.500 funcionários tão rápido quanto de apenas 5,
# assim os dados que estejam em uma lista ou venham de um banco de dados.