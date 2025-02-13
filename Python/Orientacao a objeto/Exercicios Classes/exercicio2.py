# Implemente uma classe chamada "ContaBancária" que possua atributos para armazenar o número 
#da conta, nome do titular e saldo. Adicione métodos para realizar depósitos e saques.

"""
Qual a diferença entre o def e o def __init__ ??

O def é usado para definir funções que é a palavra chave que você usa quado quer criar uma função que mais tarde pode
ser chamada no seu código. Quando você usa o (def) basicamente você está criando uma função que pode fazer alguma ação 
no seu código ou retornar algum valor.

o __init__ é um método especial chamado de contrustor, ele é chamado automaticamente quando você cria um novo objeto a 
partir de uma classe. Então resumindo o __init__ tem o objetivo de inicializar o objeto com alguns valores ou configurar
o estado inicial dele.

"""


class ContaBancária:
    def __init__(self, numero_conta, titular, saldo_inicial=0):
        """Inicializa a conta bancária com número, titular e saldo inicial."""
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        """Método para realizar um depósito na conta."""
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.") #.2f formata o número para ter 2 casa decimais.
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """Método para realizar um saque da conta."""
        if valor > 0: # Verifica se o valor do saque é positivo
            if valor <= self.saldo: # Verifica se o saldo é suficiente 
                self.saldo -= valor # Realiza o saque subtraindo o valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.") #.2f formata o número para ter 2 casa decimais.
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")
    
    def exibir_informacoes(self):
        """Método para exibir as informações da conta."""
        print(f"Conta: {self.numero_conta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")



#Exemplo de uso:
conta1 = ContaBancária(12345, "Tamires", 500.00)
conta1.exibir_informacoes()

conta1.depositar(200)
conta1.sacar(100)
conta1.exibir_informacoes()

conta1.sacar(700)  # Tentativa de saque acima do saldo