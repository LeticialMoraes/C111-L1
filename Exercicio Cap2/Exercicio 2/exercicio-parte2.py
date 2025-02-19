# Exercicio 4
print("Resolução exercicio 4")
nome1 = input("Digite o nome da 1ª pessoa: ")
peso1 = float(input(f"Digite o peso da 1ª pessoa (kg): "))
nome2 = input("Digite o nome da 2ª pessoa: ")
peso2 = float(input(f"Digite o peso da 2ª pessoa (kg): "))
nome3 = input("Digite o nome da 3ª pessoa: ")
peso3 = float(input(f"Digite o peso da 3ª pessoa (kg): "))
if peso1 > peso2 and peso1 > peso3:
    mais_pesado = nome1
elif peso2 > peso1 and peso2 > peso3:
    mais_pesado = nome2
else:
    mais_pesado = nome3

if peso1 < peso2 and peso1 < peso3:
    mais_leve = nome1
elif peso2 < peso1 and peso2 < peso3:
    mais_leve = nome2
else:
    mais_leve = nome3
print(f"\nA pessoa mais pesada é {mais_pesado}.")
print(f"A pessoa mais leve é {mais_leve}.")


print()
# Exercicio 5
print("Resolução exercicio 5")
n = int(input("Quantas pessoas deseja cadastrar? "))
soma_idades = 0
mulheres_menos_20 = 0
for i in range(n):
    nome = input(f"\nDigite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    sexo = input(f"Digite o sexo de {nome} (M/F): ").strip().upper()
    soma_idades += idade
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idades / n
print(f"\nA média de idade do grupo é: ", media_idade)
print(f"Quantidade de mulheres com menos de 20 anos: ",mulheres_menos_20)