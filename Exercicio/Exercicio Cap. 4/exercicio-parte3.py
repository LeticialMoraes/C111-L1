import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype = 'str', encoding='utf-8')
print(dataset)
missoes = len(dataset)
missoes_sucesso = np.sum(dataset[:, -1] == 'Success')
porcentagem_sucesso = (missoes_sucesso / missoes) * 100
print("porcentagem de missoes que deram certo: ", porcentagem_sucesso, "%")

missoes_eua = np.sum(np.char.find(dataset[:, 2], 'USA') >= 0)
print("numero de missoes da USA: ", missoes_eua)

spacex_missoes = dataset[dataset[:, 1] == 'SpaceX']  
spacex_missoes = np.array([m for m in spacex_missoes if m[-2].strip()])  
missao_mais_cara = max(spacex_missoes, key=lambda x: float(x[-2]))  
print("missao mais cara: ", missao_mais_cara)

empresas, contagem = np.unique(dataset[:, 1], return_counts=True)  
empresas_missoes = dict(zip(empresas, contagem))
print("empresas e quantidade de missoes: ", empresas_missoes)
