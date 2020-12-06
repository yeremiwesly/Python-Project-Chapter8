print('Total Harga Buah')
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Daftar harga buah per/kg : ')
print(buah)
total = []
while True:
    beli = input('Nama buah yang dibeli : ')
    if beli in buah:
        kg = int(input('Berapa Kg             : '))
        harga = kg * buah[beli]
        total.append(harga)
        lagi = input('Masih kurang (y/n)? ')
        if lagi != 'y':
            print('------------------------------')
            print('Total harga           : ', sum(total))
            break
