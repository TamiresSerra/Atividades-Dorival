# Crie uma classe chamada "Triângulo" como atributos para armazenar os três lados do triângulo.
# Implemente métodos para verificar se é um triângulo válido e calcular sua área.

import math

class Triangulo:
    def __init__(self, a, b, c):
        # Atributos dos lados do triângulo
        self.a = a
        self.b = b
        self.c = c

    def valido(self):
        # Verifica se a soma de dois lados é maior que o terceiro
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def calcular_area(self):
        # Se o triângulo for válido, calcula a área usando a fórmula de Herão
        if self.valido():
            s = (self.a + self.b + self.c) / 2  # Semi-perímetro
            area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            return area
        else:
            return "Triângulo inválido"

# Exemplo de uso
triangulo = Triangulo(3, 4, 5)

if triangulo.valido():
    print("Área do triângulo:", triangulo.calcular_area())
else:
    print("Os lados fornecidos não formam um triângulo válido.")
