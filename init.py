import csv

cores = []
def lerCSV():
    with open('cores.csv') as ifile:
        read = csv.reader(ifile) 
        index = 1
        for row in read:
            line = str(index) + " - " + row[0]
            print (line)
            cores.append([line, row[1], row[0]])
            index += 1

def getLine(opcao):
    for line in cores:
        if opcao in line[0]: 
            return line

def init():
    print("Digite o codigo de uma das cores abaixo para selecionar a cor escolhida para monitorar")
    lerCSV()
    cor = input()
    line = getLine(cor)
    print("A opção escolhida foi " + line[0])

    return line