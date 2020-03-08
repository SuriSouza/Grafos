a = [5, -1, 8, -2, -3, 6]
pos = []
neg = []
for i in a:
    if(i >= 0):
        pos.append(i)
    else:
        neg.append(i)
print(pos)
print(neg)