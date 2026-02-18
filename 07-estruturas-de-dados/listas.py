# O comando input() permite que o programa peça uma informação ao usuário.

# Armazenamento: 
# O resultado tem que ser guardado em uma variável.
# Tudo o que vem do input() é tratado como texto (string). Se você quiser fazer cálculos, 
# precisa converter para número usando int() ou float().

# Exemplo:

nome = input("Digite seu nome: ")
faturamento = float(input("Digite o faturamento: "))
imposto = faturamento * 0.1
print(f"{nome}, o imposto calculado é {imposto}")


# Listas são basicamente conjuntos de informações armazenados em uma única variável, definidos por [] .

# Funções de Análise:

# sum(lista): Soma todos os valores.

# len(lista): Retorna a quantidade de itens (tamanho).

# max(lista) e min(lista): Encontram o maior e o menor valor.



# Manipulação de Itens:

# Acesso por Índice: O Python começa a contar do 0, o índice -1 acessa o último item.

# Verificação (in): Checa se um item existe na lista (retorna True ou False).

# Adicionar (append): Insere um item ao final da lista.

# Remover: remove("nome") exclui pelo nome do item, pop(0) exclui pela posição.

# Contar (count): Diz quantas vezes um item aparece na lista.

# Ordenar (sort): Coloca a lista em ordem crescente ou alfabética. Use reverse=True para ordem decrescente.


# Exemplo:

produtos = ["iphone", "ipad", "macbook"]
vendas = [5000, 3000, 10000]

# Adicionando um novo produto
produtos.append("apple watch")

# Verificando se um produto existe (tratando letras maiúsculas/minúsculas)
busca = input("O que deseja pesquisar? ").lower()
print(busca in produtos)

# Ordenando as vendas do maior para o menor
vendas.sort(reverse=True)
print(vendas)

# A combinação de input() com métodos de texto (como .lower()) 
# e listas permite criar sistemas que entendem o que o usuário digita, independentemente de ele usar letras maiúsculas ou minúsculas.