import sqlite3

# Criar conexão com banco de dados
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

# Criar tabela de livros
cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    ano INTEGER NOT NULL)''')
conexao.commit()

# Função para adicionar um livro
def adicionar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    ano = input("Ano de publicação: ")
    cursor.execute("INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)", (titulo, autor, ano))
    conexao.commit()
    print("Livro adicionado com sucesso!")

# Função para visualizar livros cadastrados
def visualizar_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    if livros:
        print("\nLista de livros:")
        for livro in livros:
            print(f"{livro[0]} - {livro[1]} | {livro[2]} | {livro[3]}")
    else:
        print("Nenhum livro cadastrado.")

# Função para atualizar um livro
def atualizar_livro():
    visualizar_livros()
    id_livro = input("\nDigite o ID do livro que deseja atualizar: ")
    novo_titulo = input("Novo título: ")
    novo_autor = input("Novo autor: ")
    novo_ano = input("Novo ano de publicação: ")
    cursor.execute("UPDATE livros SET titulo=?, autor=?, ano=? WHERE id=?", (novo_titulo, novo_autor, novo_ano, id_livro))
    conexao.commit()
    print("Livro atualizado com sucesso!")

# Função para remover um livro
def remover_livro():
    visualizar_livros()
    id_livro = input("\nDigite o ID do livro que deseja remover: ")
    cursor.execute("DELETE FROM livros WHERE id=?", (id_livro,))
    conexao.commit()
    print("Livro removido com sucesso!")

# Menu principal
def menu():
    while True:
        print("\n### Biblioteca da Bosch ###")
        print("1. Cadastrar novo livro")
        print("2. Visualizar livros")
        print("3. Atualizar livro")
        print("4. Remover livro")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            visualizar_livros()
        elif opcao == "3":
            atualizar_livro()
        elif opcao == "4":
            remover_livro()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

menu()
conexao.close()
