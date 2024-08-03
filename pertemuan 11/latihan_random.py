# latihan library standart
print("------------------------------------------------------- ")
print("------------------ Contoh modul random ---------------- ")
print("------------------------------------------------------- ")

import random

nama_buah = ['Apel','Pisang','Nanas','Mangga','Semangka','Melon','Sirsat']
jumlah_index = len(nama_buah)

angka_random = random.randint(1,jumlah_index - 1)

hasil_buah = ''

if angka_random == 1 :
    hasil_buah = nama_buah[1]
elif angka_random == 2 :
    hasil_buah = nama_buah[2]
elif angka_random == 3 :
    hasil_buah = nama_buah[3]
elif angka_random == 4 :
    hasil_buah = nama_buah[4]
elif angka_random == 5 :
    hasil_buah = nama_buah[5]
elif angka_random == 6 :
    hasil_buah = nama_buah[6]
elif angka_random == 7 :
    hasil_buah = nama_buah[7]
elif angka_random == 8 :
    hasil_buah = nama_buah[8]

print ("Buah yang kepilih : ", hasil_buah)

# print("bilangan random antara 0 <= n < 1.0 : ", random.random())
# print("bilangan random antara 0 <= n < 1.0 : ", random.random())
# print("bilangan random antara 0 <= n < 1.0 : ", random.random())

# print(" ")

# # random integer
# print("bilangan random antara 1 <= n <= 1000    : ", random.randint(1, 1000))
# print("bilangan random antara 1 <= n <= 100     : ", random.randint(1, 100))
# print("bilangan random antara 1 <= n <= 10      : ", random.randint(1, 10))

# print(" ")
# print("nama buah acak adalah:",random.choice(nama_buah))






























