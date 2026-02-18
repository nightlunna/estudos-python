# O maior cuidado ao usar while é garantir que a condição em algum momento se torne falsa.
# Se a variável de controle não for atualizada (incrementada ou decrementada), o programa entrará em um loop infinito.

# Exemplos: Contador Simples
# O loop executa enquanto a variável a for menor ou igual ao limite definido.

a = 1
while a <= 15:
    print(f"Número: {a}")
    a += 1  # para evitar loop infinito

    
# Somatória com Ponto de Parada (Break)
# o programa continua pedindo números ao usuário e somando até que o número 0 seja digitado.

# break: Comando para "quebrar" e sair do loop imediatamente.
# !=: Operador que significa "diferente de".

soma = 0
while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    soma += num
print(f"A soma total é: {soma}")


#Limite de Valor Acumulado
# O loop continua enquanto o valor total da soma for inferior a um limite (ex: 100). 
# Assim que ultrapassa, o programa para e exibe o total.

total = 0
while total <= 100:
    num = int(input("Adicione um número à soma: "))
    total += num
print(f"O total ultrapassou o limite: {total}")


# No final, onde usa o while?
# nas estruturas de repetição sempre que você perceber que está copiando e colando trechos de código idênticos.
# O while é a ferramenta certa quando o encerramento da tarefa depende de uma ação externa (como um input do usuário)
# ou de um cálculo dinâmico.