# latihan library standard
print("--------------------------------------------------------")
print("---------------- contoh modul datetime -----------------")
print("--------------------------------------------------------")

import datetime
import time

waktu_sekarang = datetime.datetime.now()
tanggal = waktu_sekarang.date()
waktu = waktu_sekarang.time()

print("Hari ini adalah : ")
print("Tanggal  : ", datetime.datetime.now().day)
print("Bulan    : ", datetime.datetime.now().month)
print("Tahun    : ", tanggal.year)

print("Tanggal / Bulan / Waktu : ", tanggal.day, '/', tanggal.month, '/', tanggal.year)
print(" ")

print("Tanggal  : ", datetime.datetime.now().date())
print("Waktu    : ", datetime.datetime.now().time())

print(" ")
print("Jam      : ", waktu.hour)
print("Minute   : ", waktu.minute)
print("Second   : ", waktu.second)

time.sleep(10)

waktu_sekarang_2 = datetime.datetime.now()
delta = waktu_sekarang_2 - waktu_sekarang

print(" ")
print("Selisih detik : ", delta.total_seconds())

print(" ")