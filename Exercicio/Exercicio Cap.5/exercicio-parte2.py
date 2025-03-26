import pandas as pd
import numpy as np

print("Exercicio 6")
np.random.seed(10)
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)
media_X = df.loc[df['X'] < 30, 'X'].mean()
print(f"Média dos elementos da coluna X menores que 30: {media_X}")

print()
print("Exercicio 7")
media_D = df.loc['D'].mean()
soma_E = df.iloc[4].sum()
print(f"Média dos valores da linha D: {media_D}")
print(f"Soma dos valores da linha E: {soma_E}")

print()
print("Exercicio 8")
sub_df = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print("\nDataFrame com linhas A, C, E e colunas X, Y:")
print(sub_df)

soma_linhas = sub_df.sum(axis=1)  
soma_colunas = sub_df.sum(axis=0) 

print("\nSoma dos elementos por linha:")
print(soma_linhas)

print("\nSoma dos elementos por coluna:")
print(soma_colunas)
