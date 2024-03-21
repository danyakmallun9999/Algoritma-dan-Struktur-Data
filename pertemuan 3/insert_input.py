print("========================================================")
print("=============== Contoh List Insert =====================")
print("========================================================")
print(" ")

a = [1,2,3,4]
index = input('Masukkan index yang akan di insert   : ')
objek = input('Masukkan objek yang akan di input    : ')

a.insert(int(index),objek)

print(a)