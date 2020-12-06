buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
status = True
print('Total Harga Buah')
print('Daftar harga buah per/kg : ')
print(buah)
while status == True:
    print('Menu :')
    print('A. Tambah data buah \nB. Beli buah \nKeluar')
    menu = input('\nPilihan menu : ')
    total = []
    if menu == 'A':
        i = True
        while i == True:
            dataBaru = input('Masukkan nama buah : ')
            if dataBaru not in buah:
                harganya = int(input('Masukkan harga per/kg : '))
                buah[dataBaru] = harganya
                print('Daftar Harga Barunya')
                for data in buah:
                    print (data, '( Harga Rp', buah.get(data),')')
                    i = False
                print()
            
    elif menu == 'B':
        while True:
            beli = input('Nama buah yang ingin dibeli : ')
            if beli in buah:
                kg = int(input('Berapa Kg             : '))
                harga = kg * buah[beli]
                total.append(harga)
                lagi = input('Masih Kurang (y/n)? ')
                if lagi != 'y':
                    print('Total harga           : ', sum(total))
                    print()
                    break
    elif menu == 'Keluar':
        break
