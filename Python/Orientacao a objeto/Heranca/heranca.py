# Definição da classe base 'Animal'
class Animal:
    # Método que imprime um som genérico de animal
    def fazerSom(self):
        print("Som de animal")

# Definição da classe 'Cachorro' que herda de 'Animal'
class Cachorro(Animal):
    # Sobrescreve o método 'fazerSom' da classe 'Animal' com um comportamento específico para Cachorro
    def fazerSom(self):
        print("Au au!")
