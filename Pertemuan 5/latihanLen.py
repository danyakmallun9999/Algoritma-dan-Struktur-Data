print("-----------------------------------------------------------------------------------------")
print("     Program Menghitung Jumlah Mahasiswa di dalam suatu kelas menggunakan fungsi len    ")
print("----------------------------------------------------------------------------------------")
print("KELAS A : [PRASETYO, RIFQI, ARIF, WULAN, GERAL, NISA,LITA,AJI,BAMBANG,ABTHOL,LUTFI,YONGKI]")
print("KELAS B : [YOGA, IQBAL, HIRMANTO, CHACHA, IRWAN, ALFIANTO]")
print("KELAS C : [ARIFI, DODI, ANGGARA, FIKIH, RESTU, SUFYAN,BAMBANG,VITA,VIKI,MEIRINA]")

kelasA = ['PRASETYO', 'RIFQI', 'ARIF', 'WULAN', 'GERAL', 'NISA','LITA','AJI','BAMBANG','ABTHOL','LUTFI','YONGKI']
kelasB = ['YOGA', 'IQBAL', 'HIRMANTO', 'CHACHA', 'IRWAN', 'ALFIANTO']
kelasC = ['ARIFI', 'DODI', 'ANGGARA', 'FIKIH', 'RESTU', 'SUFYAN','BAMBANG','VITA','VIKI','MEIRINA']

while True :
    tanya = input ('Masukkan nama kelas yang akan dihitung jumlah mahasiwanya pada kelas :')
    if tanya == 'A':
        tanya = kelasA
    else:
        if tanya == 'B':
            tanya = kelasB
        else:
            if tanya == 'C':
                tanya = kelasC
            else:
                if tanya == 'stop':
                    break
    print('--------------------> Jumlah mahasiswa pada kelas tersebut adalah : ', len(tanya))
    print(' ')
print(" ")
print('Selesai')
