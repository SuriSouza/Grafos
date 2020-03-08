n = int(input("Informe n: "))
div = 2
primo = True
while(div < n):
    if(n % div == 0):
        print("Nao primo")
        primo = False
        break
    div = div + 1
if(primo == True):
    print("Primo")