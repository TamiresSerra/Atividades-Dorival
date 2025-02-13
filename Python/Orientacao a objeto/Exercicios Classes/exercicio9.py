# Crie uma classe chamada "Paciente" que possua atributos para armazenar o nome, a idade e o historico de consultas do paciente
# Implemente métodos para adicionar uma nova consulta ao histórico e exibir as consultas realizadas


class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_consultas = []  # Lista para armazenar as consultas realizadas

    def adicionar_consulta(self, consulta):
        self.historico_consultas.append(consulta)
        print(f"Consulta adicionada para o paciente {self.nome}.")

    def exibir_consultas(self):
        if self.historico_consultas:
            print(f"Consultas realizadas por {self.nome}:")
            for consulta in self.historico_consultas:
                print(f"- {consulta}")
        else:
            print(f"O paciente {self.nome} não tem consultas registradas.")

# Exemplo de uso
paciente = Paciente("Tamires", 17)

# Adicionando consultas ao histórico
paciente.adicionar_consulta("Consulta 01 - 24/01/2025")
paciente.adicionar_consulta("Consulta 02 - 30/02/2025")

# Exibindo as consultas
paciente.exibir_consultas()

