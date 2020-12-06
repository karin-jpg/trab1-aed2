import csv
import pandas
def Insertionsort(array):
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1

        array[p] = current_element


with open('distribuicao_respiradores.csv', encoding="utf8") as csv_file:

    dados = csv.reader(csv_file, delimiter=';')
    dados.__next__()

    arquivo = open('dados.txt', 'a', encoding="utf8")
    fornecedores = []
    contador = 0
    for row in dados:
        if row[1] not in fornecedores:
            fornecedores.append(row[1])
            contador+=1

    quantidade_aparelhos = [0]*contador
    print(quantidade_aparelhos)
    print(fornecedores)

def Insertionsorts(array):
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1

        array[p] = current_element


with open('distribuicao_respiradores.csv', encoding="utf8") as csv_file:

    dados = csv.reader(csv_file, delimiter=';')
    #dados.__next__()

    fornecedores = []
    contador = 0
    for row in dados:
        if row[1] not in fornecedores:
            fornecedores.append(row[1])
            contador+=1
    print(fornecedores)
    quantidade_respiradores = [0]*contador
    
