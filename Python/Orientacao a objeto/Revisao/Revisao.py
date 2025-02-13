# Desenvolvimento de Sistemas
# Aula com o Dorival Revisão

# Data da aula dia 20/01/2025 






# Estruturas de dados e tipos básicos: int, float, str, list, dict

# Exercicio 1: faça um programa que leia 2 numeros e exiba a soma deles.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

resultado = num1 + num2

print("A soma dos dois números é:", resultado)
print(resultado)



# Exercicio 2: faça um programa que leia o ANO de nascimento do usuário, o NOME e diga ao usuário qual a idade dele em 2025

ano = int(input("Qual o seu ano de nascimento?: "))
nome = input("Qual o seu nome?: ")

idade_atual = 2025 - ano

print("Olá", nome, "sua idade em 2025 é", idade_atual)





# Controle de fluxo - Condicionais: if, else, elif

# Exercicio 1: faça um programa que verifique se o número é impar ou par

numero = int(input("Digite um número inteiro: "))

# Ele verifica se o número é divisível por 2 (numero % 2 == 0).
#Se for divisível por 2, o número é par.
#Caso contrário, o número é ímpar.

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")



# Exercicio 2: faça um programa que receba 5 notas de alunos e verifique 
# Se a média é maior ou igual a 5 -> Aprovado
# Se a média for entre 2.5 e 5 -> Recuperação
# Se a média for menor que 2.5 -> Reprovado

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
nota4 = float(input("Digite a 4ª nota: "))
nota5 = float(input("Digite a 5ª nota: "))

# Calculando a média
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# Verificando a situação do aluno
if media >= 5:
    print(f"Média: {media:.2f} - Situação: Aprovado")
elif media >= 2.5:
    print(f"Média: {media:.2f} - Situação: Recuperação")
else:
    print(f"Média: {media:.2f} - Situação: Reprovado")


# Exibição formatada:
# Quando usamos {media:.2f}, o valor da média calculada é exibido com 2 casas decimais. Por exemplo:

# Se media = 4.666666, será exibido 4.67.
# Se media = 5, será exibido 5.00.

#o papel do {media:.2f} é apenas formatar o número calculado





# Controle de fluxo: laços de repetição

# Exercicio 1: faça um programa que receba um número intero positivo e exibe uma contagem de 0 até o número lido.

numero = int(input("Digite um número inteiro positivo: "))

# Verificando se o número é positivo
if numero >= 0:
    # Exibindo a contagem de 0 até o número
    for i in range(numero + 1):
        print(i)
else:
    print("Por favor, digite um número inteiro positivo.")



# Exercicio 2: faça um programa que solicite números até usuario digitar um número negativo, e verifique qual dos números digitados é o maior.

maior_numero = None # começa como None, pois ainda não foi atribuído nenhum valor.

while True:
    numero = int(input("Digite um número (ou um número negativo para sair): "))
    
    # Se o número for negativo, encerra o loop
    if numero < 0:
        break
    
    # Verificando se é o maior número digitado
    if maior_numero is None or numero > maior_numero: # O operador is verifica se dois objetos referenciam o mesmo local de memória, ou seja, se são o mesmo objeto. 
        maior_numero = numero

if maior_numero is not None: # O operador is not verifica se dois objetos não são o mesmo objeto na memória.
    print(f"O maior número digitado foi: {maior_numero}")
else:
    print("Nenhum número válido foi digitado.")




# Funções: def

# Exercicio 1: Crie uma função inverter_string(s) que inverte a string s sem usar a técnica de slicing (sem usar [::-1]). Use um laço de repetição para resolver

def inverter_string(s):
    string_invertida = ''
    for i in range(len(s) - 1, -1, -1):  # Vai do último índice até o primeiro
        string_invertida += s[i]
    return string_invertida

print(inverter_string("Tamires"))  



# Exercicio 2: Crie uma função contar_caracteres(s) que recebe uma string e retorna um dicionario com a contagem de cada caractere que aparece na string. 
# Exemplo: conta_caracteres("banana") deve retornar {'b': 1, 'a': 3, 'n': 2}.

def contar_caracteres(s):
    contagem = {}  # Dicionário vazio para armazenar as contagens
    for char in s:
        if char in contagem:
            contagem[char] += 1  # Se o caractere já foi contado, incrementa a contagem
        else:
            contagem[char] = 1  # Se for a primeira vez que o caractere aparece, inicializa a contagem
    return contagem

print(contar_caracteres("banana")) 
