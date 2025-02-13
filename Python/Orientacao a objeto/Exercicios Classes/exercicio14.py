# Crie uma classe chamada "MáquinaDeVendas" que simule uma máquina de venda de produtos
# Essa classe deve permitir cadastrar produtos, selecionar um produto para compra, inserir dinheiro, retornar troco e exibir estoque disponivel

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        # Retorna uma string formatada para exibir o nome, preço e quantidade do produto
        return f"{self.nome} - R${self.preco:.2f} - {self.quantidade} disponível(s)"

class MaquinaDeVendas:
    def __init__(self):
        self.produtos = []  # Lista para armazenar os produtos
        self.saldo = 0  # Saldo de dinheiro inserido

    def cadastrar_produto(self, nome, preco, quantidade):
        # Cadastra um novo produto na máquina de vendas
        produto = Produto(nome, preco, quantidade)  # Cria um objeto Produto com as informações fornecidas
        self.produtos.append(produto)  # Adiciona o produto à lista de produtos
        print(f"Produto {nome} cadastrado com sucesso.")  # Exibe uma mensagem de confirmação

    def exibir_estoque(self):
        # Exibe todos os produtos cadastrados e suas quantidades
        print("Estoque disponível:")
        for produto in self.produtos:
            print(produto)  # Para cada produto, imprime as informações formatadas do produto

    def selecionar_produto(self, nome_produto):
        # Seleciona um produto para compra baseado no nome
        for produto in self.produtos:
            if produto.nome.lower() == nome_produto.lower():  # Compara o nome do produto (não diferencia maiúsculas/minúsculas)
                if produto.quantidade > 0:  # Verifica se o produto está em estoque (quantidade > 0)
                    print(f"Produto {produto.nome} selecionado. Preço: R${produto.preco:.2f}")
                    return produto  # Retorna o produto selecionado para a compra
                else:
                    print(f"Produto {produto.nome} está fora de estoque.")  # Caso o produto não tenha estoque
                    return None  # Retorna None, indicando que o produto não está disponível
        print(f"Produto {nome_produto} não encontrado.")  # Caso o produto não seja encontrado
        return None  # Retorna None caso o produto não exista na lista

    def inserir_dinheiro(self, valor):
        # Insere um valor em dinheiro na máquina
        if valor <= 0:  # Verifica se o valor inserido é positivo
            print("Valor inserido deve ser positivo.")  # Se o valor for negativo ou zero, exibe uma mensagem de erro
            return
        self.saldo += valor  # Soma o valor inserido ao saldo atual
        print(f"R${valor:.2f} inseridos. Saldo atual: R${self.saldo:.2f}")  # Exibe o valor inserido e o saldo atual

    def comprar_produto(self, produto_selecionado):
        # Realiza a compra do produto, verificando se o saldo é suficiente
        if produto_selecionado and self.saldo >= produto_selecionado.preco:  # Verifica se o produto foi selecionado e se o saldo é suficiente
            self.saldo -= produto_selecionado.preco  # Subtrai o preço do produto do saldo
            produto_selecionado.quantidade -= 1  # Decrementa a quantidade do produto no estoque
            print(f"Compra realizada com sucesso! Troco: R${self.saldo:.2f}")  # Exibe mensagem de sucesso e o valor do troco
            self.saldo = 0  # Zera o saldo após a compra
        elif produto_selecionado:  # Caso o produto tenha sido selecionado
            print(f"Saldo insuficiente para comprar {produto_selecionado.nome}.")  # Exibe mensagem de erro se o saldo for insuficiente
        else:
            print("Nenhum produto selecionado para compra.")  # Exibe mensagem de erro se não houver produto selecionado

    def retornar_troco(self):
        # Retorna o troco do valor inserido
        if self.saldo > 0:  # Verifica se há saldo a ser devolvido
            print(f"TROCO: R${self.saldo:.2f}")  # Exibe o valor do troco
            self.saldo = 0  # Zera o saldo após retornar o troco
        else:
            print("Não há troco a ser retornado.")  # Caso não haja saldo (se o valor já tiver sido utilizado para a compra)

# Exemplo de uso
maquina = MaquinaDeVendas()  # Cria uma instância da máquina de vendas

# Cadastrando produtos
maquina.cadastrar_produto("Coca-Cola", 4.50, 10)  # Cadastra o produto "Coca-Cola" com preço e quantidade
maquina.cadastrar_produto("Pão da Fazenda", 3.00, 5)  # Cadastra o produto "pão da fazenda" com preço e quantidade
maquina.cadastrar_produto("Água", 2.00, 20)  # Cadastra o produto "Água" com preço e quantidade

# Exibindo o estoque disponível
maquina.exibir_estoque()  # Exibe todos os produtos cadastrados e suas quantidades

# Selecionando um produto para compra
produto_selecionado = maquina.selecionar_produto("Coca-Cola")  # Seleciona o produto "Coca-Cola"

# Inserindo dinheiro
maquina.inserir_dinheiro(5.00)  # Insere R$5,00 na máquina

# Realizando a compra
maquina.comprar_produto(produto_selecionado)  # Realiza a compra do produto selecionado

# Exibindo o estoque após a compra
maquina.exibir_estoque()  # Exibe os produtos restantes no estoque após a compra

# Retornando o troco
maquina.retornar_troco()  # Retorna o troco se houver saldo após a compra

