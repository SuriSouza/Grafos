n = int(input("Informe n: "))
soma = 0
num = 1
den = 1
for i in range(1, n + 1):
    soma = soma + (num / den)
    num = num + 1
    den = den + 2
print(soma)