def dataStatik(x):
    i = []
    for data in x:
        a = sum(x) / len(x)
        b = max(x)
        c = min(x)
    i.append(a)
    i.append(b)
    i.append(c)
    print(i)
    
x = [35, 95, 4, 65, 3, 2, 0, 5 ]
dataStatik(x)
