from time import time

def dijkstra(listaAdj, s):
    dist = []
    pred = []

    d = int(input("Vértice destino: "))
    start = time()

    for v in range(len(listaAdj)):
        dist.append(999999)
        pred.append(None)

    dist[s] = 0
    Q = []

    for i in range(len(listaAdj)):
        Q.append(i)

    while len(Q) != 0:
        aux = 100000000
        for i in Q:
            if dist[i] < aux:
                aux = dist[i]
                u = i
        Q.remove(u)

        for v in listaAdj[u]:
            if dist[v[0]] > dist[u] + v[1]:
                dist[v[0]] = dist[u] + v[1]
                pred[v[0]] = u

    caminho = rec_caminho(s, d, pred)
    caminho.reverse()
    tempo = time() - start
    print("\nOrigem: %d" % s + "\nDestino: %d" % d + "\nCaminho: " + str(caminho) +
          "\nCusto: " + str(dist[d]) + "\nTempo: %f" % tempo)


def bellmanFord(listaAdj, s, arestas):
    dist = []
    pred = []

    d = int(input("Vértice destino: "))
    start = time()

    for v in range(len(listaAdj)):
        dist.append(999999)
        pred.append(None)

    dist[s] = 0

    for i in range(len(listaAdj)):
        for e in arestas:
            if dist[e[1]] > dist[e[0]] + e[2]:
                dist[e[1]] = dist[e[0]] + e[2]
                pred[e[1]] = e[0]

    caminho = rec_caminho(s, d, pred)
    caminho.reverse()
    tempo = time() - start
    print("\nOrigem: %d" % s + "\nDestino: %d" % d + "\nCaminho: " + str(caminho) +
          "\nCusto: " + str(dist[d]) + "\nTempo: %f" % tempo)

    for e in arestas:
        if dist[e[1]] > dist[e[0]] + e[2]:
            return False
    return True

def floydWarshall(matAdj):
    dist = [[0 for y in range(len(matAdj))] for x in range(len(matAdj))]
    pred = [[None for y in range(len(matAdj))] for x in range(len(matAdj))]

    origem = int(input("Vértice origem: "))
    destino = int(input("Vértice destino: "))
    start = time()

    for i in range(len(matAdj)):
        for j in range(len(matAdj[i])):
            if i == j:
                dist[i][j] = 0
            elif matAdj[i][j] != 0:
                dist[i][j] = matAdj[i][j]
                pred[i][j] = i
            else:
                dist[i][j] = 9999999
                pred[i][j] = None

    for k in range(len(matAdj)):
        for i in range(len(matAdj)):
            for j in range(len(matAdj[i])):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    caminho = [destino]
    aux = destino
    while aux != origem:
        caminho.append(pred[origem][aux])
        aux = pred[origem][aux]

    caminho.reverse()

    tempo = time() - start
    print("\nOrigem: %d" % origem + "\nDestino: %d" % destino + "\nCaminho: " + str(caminho) +
          "\nCusto: " + str(dist[origem][destino]) + "\nTempo: %f" % tempo)

def rec_caminho(s, d, pred):
    C = [d]
    aux = d

    while aux != s:
        aux = pred[aux]
        C.append(aux)

    return C
