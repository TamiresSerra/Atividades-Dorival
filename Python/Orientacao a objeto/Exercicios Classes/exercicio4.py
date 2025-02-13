# Implemente uma classe chamada "Aluno" que possua atributos para armazenar o nome, a matrícula e as notas
# adicione métodos para calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado).

class Aluno:

    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
        """
        Inicializa a classe Aluno com os atributos:
        para nome: Nome do aluno (str)
        para matricula: Matrícula do aluno (str)
        para notas: Lista de notas do aluno (list de float)
        """

    def calcular_media(self):
        """
        Calcula a média das notas do aluno.
        return: Média das notas (float)
        """
        if len(self.notas) == 0:  # Verifica se a lista de notas está vazia
            return 0 # Retorna 0 caso não haja notas
        return sum(self.notas) / len(self.notas)  # Calcula a média somando as notas e dividindo pelo total

    def verificar_situacao(self):
        """
        Verifica a situação do aluno com base na média.
        return: 'Aprovado' se a média for >= 6.0, caso contrário 'Reprovado'.
        """
        media = self.calcular_media()
        return "Aprovado" if media >= 6.0 else "Reprovado"

    def __str__(self):
        """
        Representação em string do aluno.
        return: Detalhes do aluno.
        """
        media = self.calcular_media()
        situacao = self.verificar_situacao()
        return f"Aluno: {self.nome}\nMatrícula: {self.matricula}\nMédia: {media:.2f}\nSituação: {situacao}"

# Exemplo de uso:
aluno1 = Aluno("Tamires", "12345", [7.5, 8.0, 8.5])
print(aluno1)

aluno2 = Aluno("Luke", "67890", [5.0, 4.5, 6.0])
print(aluno2)
