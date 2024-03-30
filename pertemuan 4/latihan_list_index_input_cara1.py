print("-------------------------------------------------------------")
print("       Latihan LIST dengan menggunakan metode index          ")
print("-------------------------------------------------------------")
print(" ")
print("a = [Teknik, Informatika, Fakultas, Sains , dan , Teknologi, UNISNU ,Jepara]")
print(" ")

a = ["Teknik","Informatika", "Fakultas","Sains","dan","Teknologi", "UNISNU","Jepara"]

informatika = input("Masukkan nama objek yang akan di tampilkan no indexnya : ")
fakultas    = input("Masukkan nama objek yang akan di tampilkan no indexnya : ")
unisnu      = input("Masukkan nama objek yang akan di tampilkan no indexnya : ")

print ("Index untuk Informatika adalah Index ke : ", a.index(informatika))
print ("Index untuk Fakultas adalah Index ke    : ", a.index(fakultas))
print ("Index untuk UNISNU adalah Index ke      : ", a.index(unisnu))