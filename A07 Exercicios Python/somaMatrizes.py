def somaMatrizes(a, b):
    c = a.copy()
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]
    return c

a = [[1, 2], [3, 4]]
b = [[4, 3], [2, 1]]
c = somaMatrizes(a, b)
print(c)