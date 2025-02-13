# Implemente uma classe chamada "Produto" que possua atributos para armazenar o nome, o preço e a quantidade em estoque.
# Adicione métodos para calcular o valor total em estoque e verificar e o produto está disponível.

class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def calcular_valor_estoque(self):
        return self.preco * self.quantidade_estoque

    def disponivel(self):
        return self.quantidade_estoque > 0

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade_estoque}"


# Exemplo de uso
if __name__ == "__main__":
    produto1 = Produto("Fone sem fio", 43.80, 5)
    produto2 = Produto("Pelucia", 59.99, 7)
    print(produto1)
    print(produto2)
    print(f"Valor total em estoque: R${produto1.calcular_valor_estoque():.2f}")
    print(f"Produto está disponível? {'Sim' if produto1.disponivel() else 'Não'}")
