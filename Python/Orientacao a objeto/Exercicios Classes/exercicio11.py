# Implemente uma classe chamada "Banco" que represente uma instituição financeira
# Essa classe deve conter métodos para cadastrar cliente, abrir cotas bancárias e
# realizar operações como saques, depósitos e transferências.

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = None  # Inicialmente, o cliente não tem conta bancária

class ContaBancaria:
    def __init__(self, cliente, saldo_inicial=0):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
        else:
            print("Saldo insuficiente para o saque.")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de {valor} para a conta de {conta_destino.cliente.nome} realizada.")
        else:
            print("Saldo insuficiente para a transferência.")

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []  # Lista para armazenar os clientes do banco

    def cadastrar_cliente(self, nome, cpf):
        # Cria um cliente e adiciona à lista de clientes
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")

    def abrir_conta(self, cliente, saldo_inicial=0):
        # Cria uma conta bancária para o cliente
        conta = ContaBancaria(cliente, saldo_inicial)
        cliente.conta = conta
        print(f"Conta bancária aberta para o cliente {cliente.nome}.")

    def exibir_dados_cliente(self, cliente):
        # Exibe os dados do cliente e o saldo da conta
        if cliente.conta:
            print(f"Cliente: {cliente.nome}")
            print(f"CPF: {cliente.cpf}")
            print(f"Saldo da conta: {cliente.conta.saldo}")
        else:
            print(f"Cliente {cliente.nome} não possui conta bancária.")

# Exemplo de uso
banco = Banco("Banco Exemplo")

# Cadastrando clientes
banco.cadastrar_cliente("Amber Viollet", "123.456.789-00")
banco.cadastrar_cliente("Abner Gilbert", "987.654.321-00")

# Abrindo contas bancárias
Abner = banco.clientes[0]
Amber = banco.clientes[1]
banco.abrir_conta(Abner, 1000)
banco.abrir_conta(Amber, 500)

# Realizando operações bancárias
Abner.conta.sacar(200)
Amber.conta.depositar(300)
Abner.conta.transferir(150, Amber.conta)

# Exibindo os dados dos clientes
banco.exibir_dados_cliente(Abner)
banco.exibir_dados_cliente(Amber)
