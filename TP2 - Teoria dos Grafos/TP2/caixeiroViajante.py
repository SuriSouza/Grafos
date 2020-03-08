from time import time
from random import choice

def nearestNeighbor(listaAdj):

    naoVisitados = [x for x in range(len(listaAdj))]
    u = 0
    S = [u]
    dist = 0
    naoVisitados.remove(u)

    while len(naoVisitados) != 0:
        aux = 9999999
        for (v, w) in listaAdj[u]:
            if v in naoVisitados and w < aux:
                aux = w
                i = v

        dist = dist + aux

        S.append(i)
        naoVisitados.remove(i)
        u = i

    for j in listaAdj[S[-1]]:
        if j[0] == S[0]:
            dist += j[1]
            break

    S.append(S[0])
    print(f'Distância NN: {dist}')
    print('\033[33m'+'Processando...'+'\033[0;0m')
    twoOpt(S, listaAdj)
    return S

def twoOpt(S, listaAdj):

    start = time()

    while time() - start < 60:
        i1 = choice(S)
        i2 = choice(S)

        if i1 != i2 and i1 != S[0] and i2 != S[0]:
            S1 = S[:]
            S1[S1.index(i1)] = i2
            S1[S1.index(i2)] = i1

            custo = avalia(S, listaAdj)
            custo1 = avalia(S1, listaAdj)

            if custo1 < custo:
                S = S1[:]
            else:
                custo1 = custo

    print(f'Distância 2opt: {custo1}')
    print(f'Rota: {S}')
    print("Tempo: %.3f" % (time()-start) + "ms")

    return S

def avalia(S, listaAdj):

    custo = 0
    for i in range(len(S)-1):
        u = S[i]
        v = S[i+1]
        for j in listaAdj[u]:
            if j[0] == v:
                custo += j[1]
                break

    return custo