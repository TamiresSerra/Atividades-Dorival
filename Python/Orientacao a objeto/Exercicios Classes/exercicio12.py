# Crie uma classe chamada "Loja Virtual" que represente uma plataforma de vendas online
# Essa classe deve ter funcionalidades para cadrastrar produtos, gerar carrinho de compras
# aplicar descontos e calcular o valor total da compra

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        # Retorna uma representação em string do produto para exibição
        return f"{self.nome} - R${self.preco:.2f}"

class Carrinho:
    def __init__(self):
        # Inicializa o carrinho com uma lista vazia de produtos e sem desconto
        self.produtos = []  # Lista para armazenar os produtos no carrinho
        self.desconto = 0  # Desconto aplicado (em percentual)

    def adicionar_produto(self, produto):
        # Adiciona um produto ao carrinho
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado ao carrinho.")

    def aplicar_desconto(self, percentual):
        # Aplica o desconto no carrinho de compras
        self.desconto = percentual
        print(f"Desconto de {percentual}% aplicado.")

    def calcular_total(self):
        # Calcula o valor total da compra com o desconto aplicado
        total = sum(produto.preco for produto in self.produtos)  # Soma os preços dos produtos no carrinho
        total_com_desconto = total * (1 - self.desconto / 100)  # Aplica o desconto no total
        return total_com_desconto  # Retorna o valor total com o desconto aplicado

class LojaVirtual:
    def __init__(self, nome):
        # Inicializa a loja com nome e uma lista de produtos
        self.nome = nome
        self.produtos = []  # Lista de produtos cadastrados na loja

    def cadastrar_produto(self, nome, preco):
        # Cria um novo produto e o adiciona à lista de produtos da loja
        produto = Produto(nome, preco)
        self.produtos.append(produto)
        print(f"Produto {nome} cadastrado com sucesso.")

    def exibir_produtos(self):
        # Exibe os produtos disponíveis na loja
        print("Produtos disponíveis na loja:")
        for produto in self.produtos:
            print(produto)  # Exibe a representação de cada produto

# Exemplo de uso
loja = LojaVirtual("Loja Exemplo")

# Cadastrando produtos
loja.cadastrar_produto("Livro mangá", 59.90)
loja.cadastrar_produto("Cosplay anime", 189.90)
loja.cadastrar_produto("Pc gamer", 7129.90)

# Exibindo os produtos cadastrados
loja.exibir_produtos()

# Criando o carrinho de compras e adicionando produtos
carrinho = Carrinho()
carrinho.adicionar_produto(loja.produtos[0])  # Livro mangá
carrinho.adicionar_produto(loja.produtos[1])  # Calça Cosplay anime

# Aplicando desconto e calculando o total
carrinho.aplicar_desconto(10)  # 10% de desconto
total = carrinho.calcular_total()  # Calcula o total com o desconto
print(f"Total com desconto: R${total:.2f}")  # Exibe o total final da compra com desconto
