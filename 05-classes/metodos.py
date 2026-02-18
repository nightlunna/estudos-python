# Métodos: São as funções internas que definem o que a instância pode fazer (ex: ligar(), desligar()). 
# Têm de receber sempre o self como primeiro parâmetro para interagirem com os dados do próprio objeto.

# Exemplo
 
# O instrutor desenha a classe Computador:
# Estado: Define dinamicamente propriedades como marca, memoria ram e placa de video passando-as como argumentos.
# Comportamento: Implementa métodos para simular ações como ligar(), desligar() e exibir_informacoes().
# Execução: Instancia o computador e chama os seus métodos para verificar a lógica.
# Teoria sem execução é inútil, e a inicialização dinâmica juntamente com o uso do self costumam gerar vícios e erros lógicos no início.

class ContaBancaria:
    def init(self, titular, saldo_inicial):
 
        self.titular = titular
        self.saldo = saldo_inicial
        self.bloqueada = False 

    def exibir_extrato(self):
        print(f"Titular: {self.titular} | Saldo Atual: R${self.saldo}")

    def sacar(self, valor):
    
        if self.bloqueada:
            print("Erro: Conta bloqueada. Operação negada.")
            return False

        if valor > self.saldo:
            print("Erro: Saldo insuficiente.")
            return False

             self.saldo -= valor
        print(f"Sucesso: Saque de R${valor} realizado.")
        return True

    def bloquear_conta(self):
        self.bloqueada = True
        print("Aviso: Conta foi bloqueada por segurança.")