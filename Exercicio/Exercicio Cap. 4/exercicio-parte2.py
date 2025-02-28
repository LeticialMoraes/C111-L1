# Exercicio 4
print("Exercicio 4")
import numpy as np
matriz = np.random.randint(1, 10, (5, 5))
linhas, colunas = matriz.shape
total_elementos = linhas * colunas
par_ou_impar = "par" if total_elementos % 2 == 0 else "ímpar"
print("Matriz:\n", matriz)
print(f"Número de linhas: {linhas}")
print(f"Número de colunas: {colunas}")
print(f"Total de elementos: {total_elementos}")
print(f"O vetor unidimensional teria um número {par_ou_impar} de elementos.")


# Exercicio 5
print()
print("Exercicio 5")
np.random.seed(10)
matriz = np.random.randint(1, 51, (4, 4))
medias_linhas = np.mean(matriz, axis=1)
medias_colunas = np.mean(matriz, axis=0)
print("Matriz:\n", matriz)
print("Média de cada linha:", medias_linhas)
print("Média de cada coluna:", medias_colunas)
