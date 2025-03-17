import numpy as np


dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Questão 1
print("Questão 1")
print("País | Região | População | Área")
print("-" * 50)
for linha in dataset:
    print(f"{linha[0]} | {linha[1]} | {linha[2]} | {linha[3]}")

#Questão 2
print()
print("Questão 2")
regioes_unicas = np.unique(dataset[:, 1])
print("Regiões do planeta:")
for regiao in regioes_unicas:
    print(f"- {regiao}")

#Questão 3
print()
print("Questão 3")
taxas_alfabetizacao = dataset[:, 4].astype(float)  
media_alfabetizacao = np.mean(taxas_alfabetizacao)
print(f"A taxa média de alfabetização do planeta é: {media_alfabetizacao:.2f}%")

#Questão 4
print()
print("Questão 4")
paises_america_norte = dataset[np.char.strip(dataset[:, 1]) == 'NORTHERN AMERICA']
quantidade_paises = len(paises_america_norte)
print(f"Quantidade de países na América do Norte: {quantidade_paises}")

#Questão 5
print()
print("Questão 5")
paises_america_sul = dataset[np.char.strip(dataset[:, 1]) == 'LATIN AMER. & CARIB']
gdp_per_capita = paises_america_sul[:, 5].astype(float)  
indice_maior_gdp = np.argmax(gdp_per_capita)
pais_maior_gdp = paises_america_sul[indice_maior_gdp]
print(f"País com maior renda per capita na América do Sul e Caribe: {pais_maior_gdp[0]}")
print(f"GDP per capita: ${pais_maior_gdp[5]}")