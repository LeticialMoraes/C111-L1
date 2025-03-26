import pandas as pd

print("Exercicio 1")
seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

print()
print("Exercicio 2")
total_ano1 = seriesAno1.sum()
total_ano2 = seriesAno2.sum()

print(f"\nPorcentagem total Ano 1: {total_ano1:.2f}%")
print(f"Porcentagem total Ano 2: {total_ano2:.2f}%")

print()
print("Exercicio 3")
crescimento = ((seriesAno2 - seriesAno1) / seriesAno1 * 100)
print("\nCrescimento/Declínio por linguagem:")
for linguagem in crescimento.index:
    print(f"{linguagem}: {crescimento[linguagem]:.2f}%")

print()
print("Exercicio 4")
crescimento_positivo = crescimento[crescimento > 0]
print("\nLinguagens com crescimento:")
for linguagem in crescimento_positivo.index:
    print(f"{linguagem}: {crescimento_positivo[linguagem]:.2f}%")

print()
print("Exercicio 5")
projecao = seriesAno2 * (1 + crescimento/100) ** 2

print("\nProjeção para daqui 2 anos:")
print(projecao)
print(f"\nLinguagem mais popular será: {projecao.nlargest(1).index[0]}")

