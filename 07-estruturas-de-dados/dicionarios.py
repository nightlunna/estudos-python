# Diferente de uma lista, onde você acessa os itens pela posição (índice 0, 1, 2...), no dicionário você utiliza um rótulo (chave) 
# para encontrar um valor.

# Sintaxe: 
# Usa chaves {} e os pares são separados por dois pontos :

# Exemplo:

precos = {"iPad": 1000, "iPhone": 2000, "Notebook": 5000}

#Para pegar uma informação, você informa o nome do dicionário e a chave desejada entre [].

# Exemplo:

# Pegando o e-mail do gerente da loja Iguatemi
email = email_gerentes["Iguatemi"] 

# Adicionar ou Modificar Itens:
# A lógica é a mesma para os dois, se a chave já existe, ele substitui o valor, se não existe, ele adiciona um novo par.

# Exemplo:

# Adicionando a loja Lisa
email_gerentes["Lisa"] = "lisa@gmail.com"


# Métodos Úteis: Keys e Values
# Pode isolar apenas os rótulos ou apenas os dados:

# .keys(): Retorna todas as chaves (ex: todos os nomes das lojas).

# .values(): Retorna todos os valores (ex: todos os e-mails dos gerentes).

# Loops
# Usando um for diretamente no dicionário, ele percorre as chaves por padrão.

# Exemplo:

for shopping in email_gerentes:
    print(shopping) 
    print(email_gerentes[shopping]) 

# Remover Itens
#Para deletar uma entrada, usa o método .pop() passando a chave do item que deseja excluir.
# Se tentar remover uma chave que não existe, ele vai retornar um erro.

# Verificar se uma chave existe
# usa o operador in para checar se uma chave está presente antes de tentar acessar ou remover esse item.

# Exemplo:

if "Iguatemi" in email_gerentes:
    print("Loja encontrada!")