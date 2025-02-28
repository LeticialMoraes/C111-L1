#Resolução exercicio 1
nome_completo = input("Digite seu nome completo: ")
print("Seu nome com todas as letras maiúsculas:", nome_completo.upper())
print("Seu nome com todas as letras minúsculas:", nome_completo.lower())
quantidade_letras = len(nome_completo.replace(" ", ""))
print("Seu nome possui", quantidade_letras, "letras")
nome_modificado = nome_completo.replace(nome_completo.split()[-1], "do Inatel")
print("Seu nome modificado:", nome_modificado)
print() 
 

#Resolução exercicio 2
print("Resolução exercicio 2")
numero = int(input("Escolha um número para ver sua tabuada: "))
inicio = int(input("Escolha o início do intervalo: "))
fim = int(input("Escolha o fim do intervalo: "))
print(f"Tabuada do {numero} de {inicio} a {fim}:")
for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")

print()
#Resolução exercicio 3
print("Resolução exercicio 3") 
sexo = input("Digite seu sexo (M para homem, F para mulher): ").upper()
while sexo != 'M' and sexo != 'F':
    print("Entrada inválida. Tente novamente.")
    sexo = input("Digite seu sexo (M para homem, F para mulher): ").upper()

if sexo == 'M':
    print("Você é homem.")
else:
    print("Você é mulher.")







