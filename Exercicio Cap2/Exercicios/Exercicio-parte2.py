# Exercício 4
print("Resolução exercicio 4")
distancia = float(input("Digite a distância da viagem em Km: "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O preço da passagem é: R${preco:.2f}")

# Exercício 5
print()
print("Resolução exercicio 5")
numero = int(input("Digite um número entre 1000 e 9999: "))
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000
print(f"Número da unidade: {unidade}")
print(f"Número da dezena: {dezena}")
print(f"Número da centena: {centena}")
print(f"Número do milhar: {milhar}")

