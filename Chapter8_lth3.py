print('Program Hitung Jumlah karakter dalam Nama Mahasiswa')
status = True
i = []
while status == True:
    nama = input('Masukkan nama mahasiswa : ',)
    i.append(nama)
    i.sort()
    adalagigacuk = input('Lagi? (y/n) : ')
    if adalagigacuk != 'y':
        print()
        for data in i:
            print(data, '(', len(data), 'karakter', ')')
            status = False
