urutAngka = []
bil = int ( input ('Masukkan bilangan yang akan diurutkan : '))
while(len(urutAngka) < bil):
    angka = int ( input ("Masukkan angka : "))
    urutAngka.append(angka)
urutAngka.sort(reverse = True)
print ("Urutan dari angka besar ke kecil dari bilangan yang sudah dimasukkan adalah\n",urutAngka)
