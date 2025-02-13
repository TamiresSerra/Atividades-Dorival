'''
def merge_sort(arr):
    # Passo 1: Verificar se o array tem mais de 1 elemento
    if len(arr) > 1:
        # Encontrar o ponto médio para dividir o array
        mid = len(arr) // 2  # Divide o array ao meio
        left_half = arr[:mid]  # Metade esquerda
        right_half = arr[mid:]  # Metade direita

        # Passo 2: Recursivamente ordenar as metades
        merge_sort(left_half)  # Ordena a metade esquerda
        merge_sort(right_half)  # Ordena a metade direita

        # Passo 3: Mesclar as duas metades ordenadas
        i = j = k = 0  # Índices para as metades e o array principal

        # Comparar os elementos de left_half e right_half e inseri-los em ordem
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:  # Escolhe o menor valor
                arr[k] = left_half[i]  # Coloca no array principal
                i += 1  # Avança o índice da metade esquerda
            else:
                arr[k] = right_half[j]  # Coloca no array principal
                j += 1  # Avança o índice da metade direita
            k += 1  # Avança o índice do array principal

        # Adiciona os elementos restantes da metade esquerda (se houver)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes da metade direita (se houver)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Exemplo de uso
array = [38, 27, 43, 3, 9, 82, 10]
print("Array original:", array)
merge_sort(array)
print("Array ordenado:", array)
'''

# Array para ordenar
arr = [38, 27, 43, 3, 9, 82, 10]

# Tamanho do array
n = len(arr)

# Implementação do Merge Sort
# Passo 1: Dividir o array em partes
tamanho = 1  # Começamos com subarrays de tamanho 1
while tamanho < n:  # Continuamos até que o tamanho seja maior ou igual ao array completo
    for inicio in range(0, n, 2 * tamanho):  # Iterar em blocos de tamanho duplo
        meio = min(inicio + tamanho, n)  # Meio do bloco
        fim = min(inicio + 2 * tamanho, n)  # Fim do bloco

        # Criar os subarrays temporários
        left_half = arr[inicio:meio]
        right_half = arr[meio:fim]

        # Índices para mesclar
        i = 0  # Índice para o subarray esquerdo
        j = 0  # Índice para o subarray direito
        k = inicio  # Índice para o array principal

        # Mesclar os dois subarrays no array principal
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Adicionar os elementos restantes do subarray esquerdo
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Adicionar os elementos restantes do subarray direito
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    # Duplicar o tamanho do subarray a ser mesclado
    tamanho *= 2

# Exibir o array ordenado
print("Array ordenado:", arr)
