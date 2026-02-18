# Classe é um modelo ou molde para criar objetos.
# Objeto é uma instância concreta de uma classe,
# como um “exemplar” criado a partir do molde.
# Usar classes ajuda a organizar o código de forma modular e reutilizável

# Exemplo:
# Uma classe Carro pode definir atributos como cor e modelo e métodos 
# como acelerar() ou frear(); 
# cada carro criado é um objeto dessa classe.

# Sempre que usamos classes, obrigatoriamente ela será acompanhada de dois
# DEF (definição) definir a função da classe.
# comandos: O INIT e o SELF
#__init__ é um método que é chamado automaticamente quando um objeto é criado.
# É usado para inicializar atributos do objeto com valores específicos.

# Exemplo:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Aqui, ao criar p = Pessoa("Ana", 20), 
# os atributos do objeto são definidos já na criação.

# self representa a instância atual do objeto dentro da classe, ou seja
# o que ele irá fazer na classe.
# Ele permite acessar os atributos e métodos desse objeto.
# Sem self, métodos dentro da classe não 
# conseguem acessar ou modificar os dados daquele objeto.

# Um resumo bem simples: Classes são para moldes de objetos
# Objetos são instâncias concretas criadas a partir de classes
# __init__ inicializa os atributos doobjeto quando ele é criado. 
# self literal o próprio objeto.

# Exemplo:

class ContaBancaria:

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = salado_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor 
            print(f"Deposito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor invalido para deposito.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor invalido para saque.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor 
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")

    conta1 = ContaBancaria("Isabelly, 1000")

    conta1.exibir_saldo()
    conta1.depositar(500)
    conta1.sacar(300)
    conta1.exibir_saldo()


    