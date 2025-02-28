# Exercicio 1
print("Resolução exercicio 1")
nomes = ['Leonardo', 'Joao', 'Pedro', 'Matheus', 'Guilherme']
print("Os 3 primeiros colocados são: ", nomes[:3])
print("Os 2 ultimos colocados são: ", nomes[-2:])
print(sorted(nomes))
if 'Barcelona' in nomes:
    print(f"Barcelona está na posição {nomes.index('Barcelona')}")
else:
    print("Barcelona não está na lista.")

print()
# Exercicio 2
print("Resolução exercicio 2")
loja1 = {'iPhone 15', 'Galaxy S24', 'iPhone 13', 'Xiaomi Mi 11'}
loja2 = {'Galaxy S24', 'iPhone 13', 'OnePlus 9', 'Moto G100'}
disponiveis = loja1 | loja2
print(disponiveis)
comuns = loja1 & loja2
print(comuns)
print()


# Exercicio 3
print("Resolução exercicio 3")
aluno = {}
aluno['nome'] = input("Digite o nome do aluno: ")
aluno['media'] = float(input("Digite a média do aluno: "))
aluno['situacao'] = 'AP' if aluno['media'] >= 50 else 'RP'
print("\nDados do aluno: ", aluno)
