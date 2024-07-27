print('--------------------------------------------------------------')
print('------ Contoh LIST DEL Dengan Inputan dan Perulangan ---------')
print('--------------------------------------------------------------')
print(' ')
print('Fakultas Saintek : [Teknik Informatika, Teknik Industri, Teknik Sipil, Teknik Elektro, Sistem Informasi, Desain Produk, DKV, Budidaya Perairan]')
print(' ')

Fakultas_Saintek =  ['Teknik Informatika', 'Teknik Industri', 'Teknik Sipil', 'Teknik Elektro', 'Sistem Informasi', 'Desain Produk', 'DKV', 'Budidaya Perairan']


while True:
    hapus_index = input('Masukkan Objek yang akan di hapus : ')
    if hapus_index == 'stop':
        break
    del Fakultas_Saintek[int(hapus_index)]
    print(" ")
    print("Hasil lis Fakultas setelah di edit : ", Fakultas_Saintek)
print('Selesai')
    