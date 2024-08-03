# contoh 2 fungsi - parameter fngsi
print("-------------------------------------------------------")
print("              Contoh 2 - Parameter Fungsi              ")
print("-------------------------------------------------------")
print(" ")

def judul(prodi) :
    print('Program Studi', prodi)

def cetak_maksimal(a,b):
    if a > b:
        print("merupakan nilai maksimal", a)
    elif a == b:
        print("sama dengan",(a,b))
    else:
        print("merupakan nilai maksimal", b)

# memanggil fungsi judul dengan argumen "Teknik Informatika"
judul("Teknik Informatika")

print(" ")

# memanggil fungsi judul dengan argumen "Budidaya Perairan"
judul("Budidaya Perairan")

print(" ")

cetak_maksimal(10,100)
cetak_maksimal(1,9)
cetak_maksimal(100,800)
cetak_maksimal(1,90)
cetak_maksimal(1000,2345)