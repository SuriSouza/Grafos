import caminhoMinimo

# Leitura do arquivo fonte do grafo

print("### ESCOLHA SEU GRAFO ###\n")

opc = input("1 toy.txt\n" +
            "2 rg300_4730.txt\n" +
            "3 rome99c.txt\n" +
            "4 facebook_connections.txt\n" +
            "5 USA-road-dt.DC.txt\n\n")

if opc == "1":
    fileName = "toy.txt"
elif opc == "2":
    fileName = "rg300_4730.txt"
elif opc == "3":
    fileName = "rome99c.txt"
elif opc == "4":
    fileName = "facebook_connections.txt"
elif opc == "5":
    fileName = "USA-road-dt.DC.txt"
else:
    print("Opção Inválida!")

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
    str = file.readline()       # ler linha do arquivo
    str = str.split(" ")        # criar lista separado por espaço
    origem = int(str[0])
    destino = int(str[1])
    peso = int(str[2])
    listaAdj[origem].append((destino, peso))
    matAdj[origem][destino] = peso
    arestas.append((origem, destino, peso))

'''for i in range(len(listaAdj)):
    print(listaAdj[i])'''

# Interação com o usuário

op = input("\nAlgoritmo:\n" +
"   1 Dijkstra\n" +
"   2 Bellman-Ford\n" +
"   3 Floyd-Warshall\n\n")

if op == "1":
    minimo = caminhoMinimo.dijkstra(listaAdj, 0)

elif op == "2":
    minimo = caminhoMinimo.bellmanFord(listaAdj, 0, arestas)

elif op == "3":
    minimo = caminhoMinimo.floydWarshall(matAdj)

else:
    print("Opção inválida!")