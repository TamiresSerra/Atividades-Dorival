# Implemente uma classe chamada "Agenda" que represente uma agenda telefônica. Essa classe deve permitir adicionar
# adicionar, editar e remover contatos, além de buscar por contatos a partir de um nome ou número de telefone

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        # Retorna uma string formatada para exibir o nome e telefone do contato
        return f"{self.nome} - {self.telefone}"

class Agenda:
    def __init__(self):
        # Inicializa a agenda com uma lista vazia de contatos
        self.contatos = []  # Lista para armazenar os contatos

    def adicionar_contato(self, nome, telefone):
        # Adiciona um novo contato à agenda
        contato = Contato(nome, telefone)  # Cria o contato com nome e telefone
        self.contatos.append(contato)  # Adiciona o contato à lista de contatos
        print(f"Contato {nome} adicionado com sucesso.")

    def editar_contato(self, nome, novo_nome=None, novo_telefone=None):
        # Encontra o contato pelo nome e atualiza as informações
        for contato in self.contatos:
            if contato.nome == nome:
                # Se um novo nome for fornecido, atualiza o nome do contato
                if novo_nome:
                    contato.nome = novo_nome
                # Se um novo telefone for fornecido, atualiza o telefone do contato
                if novo_telefone:
                    contato.telefone = novo_telefone
                print(f"Contato {nome} atualizado com sucesso.")  # Exibe mensagem de sucesso
                return  # Finaliza a função, já que o contato foi encontrado e atualizado
        print(f"Contato {nome} não encontrado.")  # Caso o contato não seja encontrado

    def remover_contato(self, nome):
        # Remove um contato da agenda pelo nome
        for contato in self.contatos:
            if contato.nome == nome:
                # Se encontrar o contato, o remove da lista
                self.contatos.remove(contato)
                print(f"Contato {nome} removido com sucesso.")  # Exibe mensagem de sucesso
                return  # Finaliza a função após a remoção
        print(f"Contato {nome} não encontrado.")  # Caso o contato não seja encontrado

    def buscar_contato_por_nome(self, nome):
        # Busca um contato pelo nome
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():  # A busca não diferencia maiúsculas de minúsculas
                print(f"Contato encontrado: {contato}")  # Exibe o contato encontrado
                return  # Finaliza a função, já que o contato foi encontrado
        print(f"Contato {nome} não encontrado.")  # Caso o contato não seja encontrado

    def buscar_contato_por_telefone(self, telefone):
        # Busca um contato pelo número de telefone
        for contato in self.contatos:
            if contato.telefone == telefone:  # Compara os telefones
                print(f"Contato encontrado: {contato}")  # Exibe o contato encontrado
                return  # Finaliza a função, já que o contato foi encontrado
        print(f"Contato com telefone {telefone} não encontrado.")  # Caso o contato não seja encontrado

    def exibir_contatos(self):
        # Exibe todos os contatos na agenda
        if self.contatos:  # Verifica se há contatos na lista
            print("Contatos na agenda:")
            for contato in self.contatos:
                print(contato)  # Exibe cada contato
        else:
            print("A agenda está vazia.")  # Exibe mensagem se a agenda estiver vazia

# Exemplo de uso
agenda = Agenda()

# Adicionando contatos
agenda.adicionar_contato("Abner Gilbert", "1234-5678")  # Adiciona o contato "Abner Gilbert"
agenda.adicionar_contato("Amber Viollet", "9876-5432")  # Adiciona o contato "Amber Viollet"
agenda.adicionar_contato("Tamires Oliveira", "5555-1234")  # Adiciona o contato "Tamires Oliveira"

# Exibindo os contatos
agenda.exibir_contatos()  # Exibe todos os contatos na agenda

# Buscando contatos
agenda.buscar_contato_por_nome("Abner Gilbert")  # Busca pelo nome "Abner Gilbet"
agenda.buscar_contato_por_telefone("9876-5432")  # Busca pelo telefone "9876-5432"

# Editando um contato
agenda.editar_contato("Abner Gilbert", novo_nome="Abner", novo_telefone="1234-0000")  # Edita o nome e telefone de "Abner"

# Removendo um contato
agenda.remover_contato("Tamires Oliveira")  # Remove o contato "Tamires Oliveira"

# Exibindo os contatos após edições e remoções
agenda.exibir_contatos()  # Exibe os contatos restantes na agenda
