print('Tambah / Hapus daftar sayur')
sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print('Sayur :', sayur)
while True :
    print('Menu : \nA. Tambah data sayur \nB. Hapus data sayur \nC. Tampilkan data sayur \nKeluar\n')
    menu = input('Pilih opsinya: ')
    if menu == 'A':
        tambah = input('Mau tambah sayur apa bro : ')
        print(tambah, 'telah dimasukkan ke dalam list\n')
        sayur.append(tambah)
    elif menu == 'B':
        try:
            hapus = input('Mau hapus yang mana bro/sis : ')
            print(hapus, 'sudah dihapus dari list\n')
            sayur.remove(hapus)
        except ValueError:
            print('Sayur sudah dihapus dari list\n')
    elif menu == 'C':
        print('Data sayur : ', sayur, '\n')
    elif menu == 'Keluar':
        break
