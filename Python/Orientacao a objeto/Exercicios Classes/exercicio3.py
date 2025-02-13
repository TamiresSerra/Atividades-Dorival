# Crie uma classe chamada "Retângulo" que possua atributos para armazenar a largura e a altura. Implemente
# métodos para calcular a área e o perímetro do retângulo.

"""O self é uma referência à instância atual da sua classe."""

"""Quando você chama um método em objeto, o python passa automaticamente essa instância como o
primeiro argumento."""

import math

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        """Método para calcular a área do retângulo."""
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        """Método para calcular o perímetro do retângulo."""
        return 2 * (self.largura + self.altura)
    
    def exibir_informacoes(self):
        """Método para exibir as informações do retângulo."""
        print(f"Largura: {self.largura}")
        print(f"Altura: {self.altura}")
        print(f"Área: {self.calcular_area()}")
        print(f"Perímetro: {self.calcular_perimetro()}")

# Exemplo de uso:
retangulo1 = Retangulo(5, 10)
retangulo1.exibir_informacoes()