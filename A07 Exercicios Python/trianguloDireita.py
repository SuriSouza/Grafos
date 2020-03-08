n = int(input("Informe n: "))
for i in range(n):
    str = ""
    for j in range(n - i - 1):
        str += "  "
    for j in range(n - i - 1, n):
        str += "* "
    print(str)