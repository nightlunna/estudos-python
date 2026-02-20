# Uma requisição é uma troca de informações entre o código Python e um servidor (site ou API).
# A biblioteca Requests permite realizar quatro operações principais, similar ao um banco de dados:

# GET: Pegar informações de algum lugar.

# POST: Criar uma nova informação

# PATCH: Atualizar/editar uma informação existente

# DELETE: Excluir uma informação

# Para usar a biblioteca, é necessário instalá-la via terminal:

# python -m venv venv (terminal)
# pip install requests (terminal)

# E importá-la no código: 

import requests

# Exemplos:

# Método GET
# o código acessa uma API de moedas para obter cotações em tempo real.


link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
requisicao = requests.get(link)
print(requisicao.json()) # Converte a resposta para um dicionário Python

# Status Code 200: Significa que a requisição deu certo.

# Status Code 404: Significa que o link não foi encontrado.
# (você estava usando literalmente isso na API do pokemon)

# Método POST 

# O professor utiliza o Firebase (Google) como um banco de dados online para os testes. No POST, você deve enviar as
# informações que deseja criar no formato JSON.


informacoes = '{"nome": "Isabelly", "sobrenome": "Oliveira", "idade": "22"}'
requisicao = requests.post("link_do_firebase.json", data=informacoes)

# Método PATCH

# Diferente do POST, o PATCH serve para modificar uma informação específica dentro de um link que já existe.


informacoes_editadas = '{"idade": "23"}'
requisicao = requests.patch("link_do_item_especifico.json", data=informacoes_editadas)

# Método DELETE 

# Remove um item ou um conjunto de dados do link que foi informado.

requisicao = requests.delete("link_do_item_que_quero_apagar.json")

