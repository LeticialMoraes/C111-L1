import numpy as np

# Exercicio 1
print("exercicio 1")
array_ones = np.ones(8, dtype=int)
array_aleatorio = np.random.randint(0, 10, 8)
array_soma = array_ones + array_aleatorio
if np.sum(array_soma) >= 40:
    matriz = array_soma.reshape(4, 2)  
else:
    matriz = array_soma.reshape(2, 4) 

print("Array 1:", array_ones)
print("Array 2:", array_aleatorio)
print("Array resultante:", array_soma)
print("Matriz final:\n", matriz)

# Exercicio 2
print()
print("Exercicio 2")
array1 = np.arange(0, 52, 2)
array2 = np.arange(100, 48, -2)
array_concatenado = np.concatenate((array1, array2))
array_ordenado = np.sort(array_concatenado)
print("Array concatenado ordenado:", array_ordenado)

# Exercicio 3
print()
print("Exercicio 3")
campo = np.zeros((2, 2), dtype=int)
linha_aleatoria = np.random.randint(0, 2)
coluna_aleatoria = np.random.randint(0, 2)
campo[linha_aleatoria, coluna_aleatoria] = 1
tentativas = 0
while tentativas < 3:
    linha = int(input("Escolha uma linha (0 ou 1): "))
    coluna = int(input("Escolha uma coluna (0 ou 1): "))
    if campo[linha, coluna] == 1:
        print("Game Over! :( Try Again!")
        break
    else:
        print("Nada encontrado! Continue tentando...")
        tentativas += 1

if tentativas == 3:
    print("Congratulations! You beat the game! :)")

