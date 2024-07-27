# Soal UTS Algoritma dan Struktur Data 
# NIM : 231240001460 (Genap)
# 3 Soal dalam 1 file

# 1 B
print("----------------------------------------------------------------")
print("       Soal 1 B, Gunakan Rumus : List, Raw_input, Append        ")
print("----------------------------------------------------------------")
print("                    Form Pembelian Motor Honda                  ")
print(" ")

biodata_pembeli     = []
motor_yang_dibeli   = []


nama_pembeli            = input("masukkan nama pembeli            : ")
biodata_pembeli.append(nama_pembeli)
alamat_pembeli          = input("masukkan alamat pembeli          : ")
biodata_pembeli.append(alamat_pembeli)
tempat_lahir_pembeli    = input("masukkan tempat lahir            : ")
biodata_pembeli.append(tempat_lahir_pembeli)
tanggal_lahir_pembeli   = input("masukkan tanggal lahir           : ")
biodata_pembeli.append(tanggal_lahir_pembeli)

print(" ")
print(" ")

type_motor  = input("masukkan nama type motor         : ")
motor_yang_dibeli.append(type_motor)
harga_motor = input("masukkan harga motor             : ")
motor_yang_dibeli.append(harga_motor)
warna_motor = input("masukkan warna motor             : ")
motor_yang_dibeli.append(warna_motor)

print(" ")
print(" ")

print("Biodata Pembeli          : ", biodata_pembeli)
print("Motor yang dibeli        : ", motor_yang_dibeli)
print(" ")
print(" ")

# 2B
print("----------------------------------------------------------------")
print("      Soal 2B, Rumus : List, while, Raw_input, Break, Del       ")
print("----------------------------------------------------------------")
print(" ")

bilangan_genap = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]

print("Daftar bilangan genap = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]")
print(" ")

while True : 
    hapus_indeks = input("Masukkan indeks bilangan genap yang akan di hapus : ")
    if hapus_indeks == "stop" :
        break
    del bilangan_genap[int(hapus_indeks)]
    print("Hasil List bilangan genap setelah di edit : ", bilangan_genap)
    print(" ")
print("selesai")
print(" ")
print(" ")


# 3
print("----------------------------------------------------------------")
print("           Program Fungsi Len, Max dan Min pada Tuple           ")
print("----------------------------------------------------------------")
print(" ")

A = ("Program", "Studi", "Teknik", "Informatika", "Fakultas", "Saintek", "Unisnu")
B = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500)

print("Variable Tuple : ")
print("A = (Program, Studi, Teknik, Informatika, Fakultas, Saintek, Unisnu)")
print("B = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500)")
print(" ")

print("Tampilkan : ")
print("Menentukan nilai len dari elemen A adalah                   : ", len(A))
print("Menentukan nilai len dari elemen B adalah                   : ", len(B))
print("")

print("Menentukan nilai maximum atau terbesar dari elemen A adalah : ", max(A))
print("Menentukan nilai minimum atau terkceil dari elemen A adalah : ", min(A))
print(" ")

print("Menentukan nilai maximum atau terbesar dari elemen B adalah : ", max(B))
print("Menentukan nilai minimum atau terkecil dari elemen B adalah : ", min(B))