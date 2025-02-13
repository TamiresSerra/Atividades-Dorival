# Crie uma classe chamada "Círculo" que possua um atributo para armazenar o raio e métodos para calcular a área e o perímetro do círculo.


""" 
Minha explicação:

Relembrando o que são classes -> uma classe é um modelo que define a estrutura de um objeto. Ela contém:

Atributos: Variáveis que armazenam características do objeto.
Métodos: Funções que definem o comportamento do objeto.

Já o objeto é uma (instância) dessa classe. Cada objeto criado a partir de uma classe herda os atributos e métodos definidos por ela, mas
pode ter valores e estados específicos.

Explicando de uma maneira mais clara: resumidamente imagina que você está criando um modelo ou plano para um objeto. Esse modelo
vai definir como o objeto vai ser e como ele vai se comportar. Esse (plano) é a classe.

Hmm, outro exemplo, se quisermos criar um modelo de (carro), a classe pode definir algumas características do carro (atributos) e o que 
ele pode fazer (métodos).


O que são atributos ???

Os atributos são as 'características' do objeto. No caso de uma (Carro), pode se falar que os atributos são:

1. cor
2. marca
3. modelo
4. ano


O que são métodos ???

Os métodos são as 'ações' ou 'comportamentos' que o objeto pode ter. No caso do (Carro), pode se falar que os métodos são:

1. andar
2. frear
3. buzinar


E o que é um objeto ???

Quando você cria algo a partir de uma classe, você automaticamente está criando um objeto. Cada objeto é uma instância daquela
classe. isso significa que, a partir da classe (Carro), você pode criar vários carros diferentes, com carcterísticas próprias,
mas todos vão compartilhar a mes estrutura definida pela classe.

"""

# Voltando ao exercício, # Crie uma classe chamada "Círculo" que possua um atributo para armazenar o raio e métodos para calcular a área e o perímetro do círculo.

import math # calcular o valor de pi ou outras diversas contas em python

class Circulo:
    def __init__(self, raio):  # Método especial que inicializa o círculo
        self.raio = raio  # Atribui o valor do raio

    def calcular_area(self):  # Método para calcular a área
        return math.pi * self.raio ** 2  # Fórmula da área

    def calcular_perimetro(self):  # Método para calcular o perímetro
        return 2 * math.pi * self.raio  # Fórmula do perímetro
    
    
# Criando um círculo com raio 5
meu_circulo = Circulo(5)

# Calculando e mostrando a área
print("Área do círculo:", meu_circulo.calcular_area())

# Calculando e mostrando o perímetro
print("Perímetro do círculo:", meu_circulo.calcular_perimetro())