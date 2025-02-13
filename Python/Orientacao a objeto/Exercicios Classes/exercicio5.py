# Crie uma classe chamada "Funcionário" com atributos para armazenar o nome, o salário e o cargo do funcionário.
# Implemente métodos para calcular o salário líquido, considerando descontos de imposto e benefícios.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome  # Armazena o nome do funcionário
        self.salario = salario  # Armazena o salário bruto do funcionário
        self.cargo = cargo  # Armazena o cargo do funcionário

    def calcular_salario_liquido(salario_bruto, beneficios=0, outros_descontos=0):
        """
        Calcula o salário líquido de forma simplificada.

        :param salario_bruto: Salário bruto do funcionário (float)
        :param beneficios: Total de benefícios recebidos (float, opcional)
        :param outros_descontos: Total de descontos (float, opcional)
        :return: Salário líquido (float)
        """
        # Tabelas simplificadas para INSS e IRRF
        inss = min(salario_bruto * 0.14, 7507.49 * 0.14)  # Calcula 14% do salário bruto ou aplica o teto do INSS
        irrf = max(0, (salario_bruto - inss) * 0.15 - 354.80)  # Calcula 15% sobre o salário base menos INSS, aplicando dedução

        # Salário líquido
        return salario_bruto - (inss + irrf + outros_descontos) + beneficios  # Subtrai INSS, IRRF e outros descontos e adiciona benefícios


# Exemplo de uso
salario_bruto = 5000.00
beneficios = 800.00
outros_descontos = 200.00

salario_liquido = Funcionario.calcular_salario_liquido(salario_bruto, beneficios, outros_descontos)
print(f"Salário líquido: R$ {salario_liquido:.2f}")