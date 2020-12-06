def pengkuadratan(bilangan):
    hasilnya = []
    for data in bilangan:
        data = data**2
        hasilnya.append(data)
    print(hasilnya)

bilangan = [2, 4, 5, 6]  
hasilnya = pengkuadratan(bilangan)
