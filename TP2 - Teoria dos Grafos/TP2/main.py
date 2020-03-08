import caixeiroViajante

# Leitura do arquivo fonte do grafo

fileName = input("Digite o grafo: ")
file = open(fileName)
str = file.readline()
str = str.split(" ")
numVertices = int(str[0])
numArestas = int(str[1])

# Preenchimento das estruturas de dados

listaAdj = [[] for x in range(numVertices)]
matAdj = [[0 for x in range(numVertices)] for x in range(numVertices)]
vertices = [x for x in range(numVertices)]
arestas = []

for i in range(numArestas):
    str = file.readline()
    str = str.split(" ")
    origem = int(str[0])
    destino = int(str[1])
    peso = float(str[2])
    listaAdj[origem].append((destino, peso))
    matAdj[origem][destino] = peso
    arestas.append((origem, destino, peso))

print("\nGrafo: <" + fileName + ">")
S = caixeiroViajante.nearestNeighbor(listaAdj)
