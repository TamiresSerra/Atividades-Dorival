# Definição da classe 'Gato', que herda de 'Animal'
class Gato(Animal):
    # Sobrescreve o método 'fazerSom' da classe 'Animal' com um comportamento específico para Gato
    def fazerSom(self):
        print("Miau!")  # O Gato faz "Miau!" quando o método é chamado

# Função que aceita um objeto 'animal' como parâmetro e chama o método 'fazerSom' desse objeto
def emitirSomDoAnimal(animal):
    animal.fazerSom()  # Chama o método 'fazerSom' do objeto passado como parâmetro (polimorfismo em ação)

# Criando um objeto da classe Cachorro
cachorro = Cachorro()

# Criando um objeto da classe Gato
gato = Gato()

# Chama a função 'emitirSomDoAnimal' passando o objeto 'cachorro' como argumento
emitirSomDoAnimal(cachorro)  # Saída: "Au au!" porque o método 'fazerSom' foi sobrescrito em Cachorro

# Chama a função 'emitirSomDoAnimal' passando o objeto 'gato' como argumento
emitirSomDoAnimal(gato)      # Saída: "Miau!" porque o método 'fazerSom' foi sobrescrito em Gato
