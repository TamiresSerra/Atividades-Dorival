# Implemente uma classe chamada "Carro" com atributos para armazenar a marca, o modelo e a velocidade atual do carro.
# Adicione métodos para acelerar, frear e exibir a velocidade atual.


class Carro:
    def __init__(self, marca, modelo, velocidade_atual):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual

    def acelerar(self, aumento):
        # Aumenta a velocidade do carro
        self.velocidade_atual += aumento
        print(f"Carro acelerando. Velocidade atual: {self.velocidade_atual} km/h.")

    def frear(self, reducao):
        # Diminui a velocidade do carro
        if self.velocidade_atual - reducao < 0:
            self.velocidade_atual = 0
            print("Carro totalmente parado.")
        else:
            self.velocidade_atual -= reducao
            print(f"Carro freiando. Velocidade atual: {self.velocidade_atual} km/h.")

    def exibir_velocidade(self):
        print(f"A velocidade atual do carro é {self.velocidade_atual} km/h.")

# Exemplo de uso
carro = Carro("Fiat", "Toro", 50)

carro.acelerar(20)
carro.frear(10)
carro.exibir_velocidade()
