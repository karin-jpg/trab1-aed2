import csv
import pandas as pd
import matplotlib.pyplot as plot


def countingSort(quantidade, fornecedores, exp): 
  
    n = len(quantidade) 
  
    output = [0] * (n) 
    output2 = [0] * (n) 
    count = [0] * (10) 

    for i in range(0, n): 
        index = (quantidade[i] / exp) 
        count[int(index % 10)] += 1

    for i in range(1, 10): 
        count[i] += count[i - 1] 
  
    i = n - 1
    while i >= 0: 
        index = (quantidade[i] / exp) 
        output[count[int(index % 10)] - 1] = quantidade[i]
        output2[count[int(index % 10)] - 1] = fornecedores[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(quantidade)): 
        quantidade[i] = output[i]
        fornecedores[i] = output2[i]
  

def radixSort(quantidade, fornecedores):   
    max1 = max(quantidade) 

    exp = 1
    while max1 / exp > 0: 
        countingSort(quantidade, fornecedores, exp) 
        exp *= 10


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

def shellSort(quantidade, fornecedores, n):
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            aux1 = quantidade[i]
            aux2 = fornecedores[i]
            j = i
            while j >= intervalo and quantidade[j - intervalo] > aux1:
                quantidade[j] = quantidade[j - intervalo]
                fornecedores[j] = fornecedores[j - intervalo]
                j -= intervalo

            quantidade[j] = aux1
            fornecedores[j] = aux2
        intervalo //= 2




dados = pd.read_csv('distribuicao_respiradores.csv', encoding="utf-8", sep = ";")

datas = []
contador = 0

for index, linha in dados.iterrows():
    if linha['ESTADO/MUNICIPIO'] == 'ESTADO':
        if linha['DATA DE ENTREGA'] not in datas:
            datas.append(linha['DATA DE ENTREGA'])
            contador+=1

quantidade_respiradores = [0]*contador

for index, linha in dados.iterrows():
    if linha['ESTADO/MUNICIPIO'] == 'ESTADO':
        indice = datas.index(linha['DATA DE ENTREGA'])
        quantidade_respiradores[indice] += int(linha['QUANTIDADE'])



#Insertionsort(quantidade_respiradores, datas)
#shellSort(quantidade_respiradores, datas, len(quantidade_respiradores))
radixSort(quantidade_respiradores, datas)
quantidade = []
data = []
for i in range(50):
    quantidade.append(quantidade_respiradores[i])
    data.append(datas[i])

plot.barh(data, quantidade)
plot.xlabel('Quantidade respiradores')
plot.ylabel('Estado')
plot.title('Quantidade de respiradores entregues por Estado')
for i, v in enumerate(data):
    plot.text(quantidade_respiradores[i], v, str(quantidade_respiradores[i]))
plot.show()