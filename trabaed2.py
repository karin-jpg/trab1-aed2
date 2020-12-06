import csv
import pandas as pd
import matplotlib.pyplot as plot
import fornecedor

def Insertionsort(quantidade, fornecedor):
    for p in range(0, len(quantidade)):
        quantidade_atual = quantidade[p]
        fornecedor_atual = fornecedor[p]

        while p > 0 and quantidade[p - 1] > quantidade_atual:
            quantidade[p] = quantidade[p - 1]
            fornecedor[p] = fornecedor[p - 1]
            p -= 1

        quantidade[p] = quantidade_atual
        fornecedor[p] = fornecedor_atual
        
def Insertionsort1(array):
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1

        array[p] = current_element

dados = pd.read_csv('distribuicao_respiradores.csv', encoding="utf-8", sep = ";")

fornecedores = []
contador = 0

#print(dados.head(3))
print(dados.iloc[1,0])


fornecedores = []
contador = 0

for index, linha in dados.iterrows():
    if linha['FORNECEDOR'] not in fornecedores:
            fornecedores.append(linha['FORNECEDOR'])
            contador+=1

quantidade_respiradores = [0]*contador

for index, linha in dados.iterrows():
    indice = fornecedores.index(linha['FORNECEDOR'])
    quantidade_respiradores[indice] += int(linha['QUANTIDADE'])

#for i in range(len(fornecedores)):
 #   print(fornecedores[i], ' = ', quantidade_respiradores[i])


for i in range(len(fornecedores)):
    print(fornecedores[i], ' = ', quantidade_respiradores[i])
Insertionsort(quantidade_respiradores, fornecedores)
print("-----------------------------------")
for i in range(len(fornecedores)):
    print(fornecedores[i], ' = ', quantidade_respiradores[i])

#plot.rcParams.update({'font.size': 5})
#plot.rcParams['xtick.labelsize'] = 5
#plot.rcParams['ytick.labelsize'] = 7
plot.barh(fornecedores, quantidade_respiradores)
plot.xlabel('quantidade respiradores')
plot.ylabel('Fornecedores')
plot.title('Fornecedores x quantidade respiradores entregues')
for i, v in enumerate(fornecedores):
    plot.text(quantidade_respiradores[i], v, str(quantidade_respiradores[i]))
plot.show()