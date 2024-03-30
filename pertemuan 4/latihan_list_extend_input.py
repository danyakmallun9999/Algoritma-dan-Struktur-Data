print("-------------------------------------------------------------")
print("       Latihan LIST dengan menggunakan metode extend         ")
print("-------------------------------------------------------------")
print(" ")
a = ["Teknik","Informatika"]
b = ["Fakultas","Sains","dan","Teknologi"]
c = ["UNISNU","Jepara"]
d = input ("Masukkan List objek yang akan di Extend : ")

a.extend(b)
a.extend(c)
a.extend([d])

print("Contoh Mengextend List : ", a)