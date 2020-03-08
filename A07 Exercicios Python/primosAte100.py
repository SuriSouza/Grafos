for n in range(2, 101):
    div = 2
    primo = True
    while(div < n):
        if(n % div == 0):
            primo = False
            break
        div += 1
    if(primo):
        print(n)
