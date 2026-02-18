# O Python utiliza a indentação (o recuo do código,"Tab") para saber quais comandos pertencem a uma condição.

# if (se): Executa um bloco de código se a condição for verdadeira.

# else (caso contrário): Executa se a condição do if for falsa.

# elif (senão se): Testa múltiplas condições em sequência.

# Comparações e Operadores:

# ==: Verifica se dois valores são iguais.

# !=: Verifica se são diferentes.

# > / <: Maior que / Menor que.

# and: As duas condições precisam ser verdadeiras.

# or: Pelo menos uma condição precisa ser verdadeira.

# Exemplo 1:
# O programa pede o nome de um produto e verifica se ele já existe em uma lista. Se não existir, ele cadastra o item.

produtos = ["iphone", "ipad", "airpod"]
novo_produto = input("Digite o produto: ")

if novo_produto in produtos:
    print("Produto já existente.")
else:
    produtos.append(novo_produto)
    print(f"{novo_produto} cadastrado com sucesso!")


# Exemplo 2: 
# Cálculo de Bônus com Faixas (Usando elif)

# Vendas >= 15.000: Bônus de 500.
# Vendas entre 5.000 e 15.000: Bônus de 100.
# Vendas < 5.000: Bônus zero.

vendas = 11000

if vendas >= 15000:
    bonus = 500
elif vendas >= 5000:
    bonus = 100
else:
    bonus = 0

print(f"Bônus: {bonus}")


#Exemplo 3: 
# Condições Compostas (and)
# O bônus só é pago se o funcionário atingir sua meta e a empresa também bater a meta global (ex: 100.000)

vendas_func = 16000
vendas_empresa = 200000
meta_empresa = 100000

if vendas_func >= 15000 and vendas_empresa >= meta_empresa:
    bonus = 500
elif vendas_func >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 100
else:
    bonus = 0