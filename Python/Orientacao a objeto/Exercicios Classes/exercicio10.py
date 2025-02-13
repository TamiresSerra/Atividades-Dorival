# Implemente uma classe chamada "livro" com atributos para armazenar o título, o autor e o número de páginas do livro
# Adicione métodos para emprestar o livro, devolvê-lo e verificar se está disponível

class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.disponivel = True  # A princípio, o livro está disponível para empréstimo

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível no momento.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido e está disponível novamente.")
        else:
            print(f"O livro '{self.titulo}' já está disponível.")

    def verificar_disponibilidade(self):
        if self.disponivel:
            print(f"O livro '{self.titulo}' está disponível para empréstimo.")
        else:
            print(f"O livro '{self.titulo}' não está disponível no momento.")

# Exemplo de uso
livro = Livro("A menina que roubava livros", "Markus Zusak", 550)
# Verificando a disponibilidade e emprestando
livro.verificar_disponibilidade()
livro.emprestar()

# Tentando emprestar novamente
livro.emprestar()

# Devolvendo o livro
livro.devolver()

# Verificando novamente a disponibilidade
livro.verificar_disponibilidade()
