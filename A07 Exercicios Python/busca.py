#Dada uma lista busca um determinado elemento
#se ele for encontrado seu indice e imprimido
#caso contrario imprime que o elemento nao foi encontrado
a = [4, 2, 5, 7, 6, 1]
n = int(input("Informe n: "))
encontrou = False
for i in range(len(a)):
    if(a[i] == n):
        print("%d no indice %d" % (n, i))
        encontrou = True
        break
if(not encontrou):
    print("%d nao encontrado!" % n)