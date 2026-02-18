# Um set é uma coleção não ordenada de valores únicos (não permite duplicatas)
# Eles são ideais para armazenar múltiplos itens onde a repetição não é desejada e para realizar operações matemáticas de conjuntos.

# Características Principais:
# Sintaxe: São criados utilizando chaves { }, diferentemente das listas [ ] e tuplas ( ).

# Imutabilidade dos itens: 
# o conjunto em si, você pode adicionar ou remover itens,
# os elementos colocados nele devem ser de tipos imutáveis.

# Não indexados: 
# Como não possuem uma ordem definida, você não pode acessar um elemento por uma posição específica (índice).

# Operações Básicas:

# Criação:
# Pode ser feita diretamente com {} ou através da função set(), 
# que inclusive converte outras coleções (como listas) em conjuntos,
# eliminando duplicatas automaticamente.

# Verificação e Iteração: 
# É possível usar a função len() para saber o tamanho, o operador in para verificar se
#  um item existe e laços for para percorrer os elementos .


# Adicionar e Remover:

# add(): Adiciona um novo elemento (se já existir, ele ignora).

# remove(): Remove um item, mas gera erro se o item não for encontrado.

# discard(): Remove um item e, caso ele não exista, não gera erro.

# pop(): Remove um elemento aleatório.

# clear(): Esvazia o conjunto completamente.


# Operações Matemáticas de Conjuntos:

# União (| ou union): Junta todos os elementos de dois conjuntos, removendo as repetições.

# Intersecção (& ou intersection): Retorna apenas os elementos que aparecem em ambos os conjuntos.

# Diferença (- ou difference): Retorna os elementos que estão no primeiro conjunto, mas não no segundo.

# Diferença Simétrica (^ ou symmetric_difference): Retorna elementos que estão em um dos conjuntos, mas não nos dois ao mesmo tempo.

# Disjunção (isdisjoint): Verifica se dois conjuntos não possuem nenhum elemento em comum.

#Exemplos:

class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} deu a partida: VRUM!")
        else:
            print(f"O {self.modelo} já está ligado.")

carro_do_joao = Carro("Ford", "Mustang", "Preto")
carro_da_maria = Carro("Fiat", "Uno", "Escada no teto")

carro_do_joao.ligar() 
# Saída: O Mustang deu a partida: VRUM!


# Exemplo de duplicatas em uma lista e como o set resolve:

emails_sujos = ["ana@email.com", "joao@email.com", "ana@email.com", "pedro@email.com", "joao@email.com"]

emails_unicos = set(emails_sujos)

print(emails_unicos)
# Saída: {'ana@email.com', 'joao@email.com', 'pedro@email.com'}


# Exemplo de quais produtos as duas lojas vendem e o que cada uma tem de exclusivo:

estoque_loja_A = {"Teclado", "Mouse", "Monitor", "Cadeira"}
estoque_loja_B = {"Mouse", "Monitor", "Headset", "Webcam"}

# (Intersecção)
em_comum = estoque_loja_A & estoque_loja_B
print(f"Ambas vendem: {em_comum}") # {'Mouse', 'Monitor'}

#(Diferença)
exclusivo_A = estoque_loja_A - estoque_loja_B
print(f"Só na Loja A: {exclusivo_A}") # {'Teclado', 'Cadeira'}