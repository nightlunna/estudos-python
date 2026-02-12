"Funções são comandos que realizam ações específicas, mas podemos criar as nossas próprias para personalizar operações"
"Para definir uma função, utiliza a palavra-chave def, seguida pelo nome da função e parênteses."
#exemplo:
def minha_funcao():
    print("Essa é minha função!")

# A FUNÇÃO SÓ EXECUTADA QUANDO VOCÊ CHAMA ELA PELO NOME

minha_funcao()
""" você literalmente chamou a sua propria função pra ser executada"""

"Um adendo importante é que existem diferenças em váriaveis colocadas dentro da sua função e fora dela, ou seja, locais e globais"
"Criadas dentro da sua função, elas só existem enquanto a função está sendo executada"
"Criadas fora da sua função, elas podem ser acessadas em qualquer lugar do código, inclusive dentro das suas funções"
"temos parâmetros e argumentos, que permitem enviar dados da função para tornar ela interativa"
"Parâmetros são os nomes definidos na criação da função"
"Argumentos são os valores reais passados ao chamar a função"

#exemplo
def somar(n1, n2):
    print(n1 + n2)

"existe um comando chamado retorno de valores que se chama RETURN"
"ele permite que a função devolva um valor para quem chamou, guardar o resultado em uma variável"

#exemplo
def somar2(n1, n2):
    resultado = n1 + n2
    return resultado

resultado_da_soma = somar(5,5)
print(resultado_da_soma)

"argumentos váriaveis são definidos em duas partes: de um e dois ateriscos sendo que um é adicionado como tupla e dois como dicionario"
#exemplo
def calcular_media(*numeros):
    qtd =len(numeros)
    soma = 0
    for numero in numero
    media = soma / qtd
    return media

resultado = calcular_media(7,2,4,9)
print(f"A media é {resultado}")