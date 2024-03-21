print("========================================================")
print("=============== Contoh List Insert =====================")
print("========================================================")
print(" ")

nama = ['Mochammad','Haji']
alamat = ['Jl','Taman','Pekeng','Tahunan','Jepara']

index = input('Masukkan index nama yang akan di insert   : ')
objek = input('Masukkan objek nama yang akan di input    : ')

index1 = input('Masukkan index alamat yang akan di insert   : ')
objek1 = input('Masukkan objek alamat yang akan di input    : ')

nama.insert(int(index),objek)
alamat.insert(int(index1),objek1)

print('Nama setelah di insert', nama)
print('Alamat setelah di insert', alamat)