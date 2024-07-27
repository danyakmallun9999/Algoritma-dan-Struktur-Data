from datetime import date, timedelta


daftar_buku = [
{
        'judul': 'Laskar Pelangi',
        'penulis': 'Andrea Hirata',
        'isbn': '9789793062791'
    },
    {
        'judul': 'Bumi Manusia',
        'penulis': 'Pramoedya Ananta Toer',
        'isbn': '9789799731233'
    },
    {
        'judul': 'Negeri 5 Menara',
        'penulis': 'Ahmad Fuadi',
        'isbn': '9789792258386'
    },
    {
        'judul': 'Supernova: Ksatria, Puteri, dan Bintang Jatuh',
        'penulis': 'Dewi Lestari',
        'isbn': '9789792285634'
    },
    {
        'judul': 'Tetralogi Buru: Anak Semua Bangsa',
        'penulis': 'Pramoedya Ananta Toer',
        'isbn': '9789799731240'
    },
    {
        'judul': 'Ayat-Ayat Cinta',
        'penulis': 'Habiburrahman El Shirazy',
        'isbn': '9789792731292'
    },
    {
        'judul': '5 Cm',
        'penulis': 'Donny Dhirgantoro',
        'isbn': '9789791227208'
    },
    {
        'judul': 'Rectoverso',
        'penulis': 'Dewi Lestari',
        'isbn': '9789792285641'
    },
    {
        'judul': 'Cantik Itu Luka',
        'penulis': 'Eka Kurniawan',
        'isbn': '9789793062760'
    },
    {
        'judul': 'Kambing Jantan',
        'penulis': 'Raditya Dika',
        'isbn': '9789792259079'
    }
]

daftar_anggota = [
    {
        'nama': 'Dany Akmallun Niam',
        'alamat': 'Jepara',
        'nim': '190001'
    },
    {
        'nama': 'Maudy Ayunda',
        'alamat': 'Jakarta',
        'nim': '190002'
    },
    {
        'nama': 'Dian Sastrowardoyo',
        'alamat': 'Jakarta',
        'nim': '190006'
    },
    {
        'nama': 'Afgan Syahreza',
        'alamat': 'Jakarta',
        'nim': '190007'
    },
    {
        'nama': 'Agnez Mo',
        'alamat': 'Jakarta',
        'nim': '190008'
    },
    {
        'nama': 'Reza Rahadian',
        'alamat': 'Jakarta',
        'nim': '190009'
    },
    {
        'nama': 'Cinta Laura',
        'alamat': 'Jakarta',
        'nim': '190010'
    }
]

data_peminjaman = [
    {
        'nama': 'Dany Akmallun Niam',
        'nim': '190005',
        'judul': 'Tetralogi Buru: Anak Semua Bangsa',
        'tgl_minjam': '2024-07-04',
        'tgl_pengembalian': '2024-07-12'
    },
    {
        'nama': 'Raisa Andriana',
        'nim': '190001',
        'judul': 'Laskar Pelangi',
        'tgl_minjam': '2024-07-04',
        'tgl_pengembalian': '2024-07-12'
    },
    {
        'nama': 'Maudy Ayunda',
        'nim': '190002',
        'judul': 'Bumi Manusia',
        'tgl_minjam': '2024-07-04',
        'tgl_pengembalian': '2024-07-12'
    },
    {
        'nama': 'Dian Sastrowardoyo',
        'nim': '190006',
        'judul': 'Ayat-Ayat Cinta',
        'tgl_minjam': '2024-07-04',
        'tgl_pengembalian': '2024-07-12'
    },
    {
        'nama': 'Afgan Syahreza',
        'nim': '190007',
        'judul': '5 Cm',
        'tgl_minjam': '2024-07-04',
        'tgl_pengembalian': '2024-07-12'
    },
    {
        'nama': 'Agnez Mo',
        'nim': '190008',
        'judul': 'Rectoverso',
        'tgl_minjam': '2024-07-04',
        'tgl_pengembalian': '2024-07-12'
    },
    {
        'nama': 'Reza Rahadian',
        'nim': '190009',
        'judul': 'Cantik Itu Luka',
        'tgl_minjam': '2024-07-04',
        'tgl_pengembalian': '2024-07-12'
    },
    {
        'nama': 'Cinta Laura',
        'nim': '190010',
        'judul': 'Kambing Jantan',
        'tgl_minjam': '2024-07-04',
        'tgl_pengembalian': '2024-07-12'
    }

]

def tampilanAwal():
    print(' ')
    print('              <---- Selamat Datang ---->              ')
    print('         [    PERPUSTAKAAN UNISNU JEPARA    ]         ')
    print('------------------------------------------------------')
    print("""
        1. Buku
        2. Anggota
        3. Peminjaman
        4. Keluar
    """)

    pilihan = input("Masukkan pilihan = ")

    if pilihan == '1':
        buku()
    elif pilihan == '2':
        anggota()
    elif pilihan == '3':
        peminjaman()
    elif pilihan == '4':
        exit()
    else:
        print(' ')
        print('            !!!-  PILIHAN TIDAK ADA  -!!!         ')

def buku():

    while True:
        print(' ')
        print(' ')
        print('                <---- Sistem Buku ---->               ')
        print('-------------|------ ++++++++++++++ -----|------------')
        print("""
                1. Tambah buku
                2. Lihat daftar buku
                3. Hapus buku
                4. Kembali ke awal
        """)

        pilihan = input('Masukkan Pilihan = ')

        if pilihan == '1':
            tambahBuku()
        elif pilihan == '2':
            daftarBuku()
        elif pilihan == '3':
            hapusBuku()
        elif pilihan == '4':
            tampilanAwal()
        else:
            print(' ')
            print('            !!!-  PILIHAN TIDAK ADA  -!!!         ')

def tambahBuku():
    print(' ')
    print('                <---- Tambah Buku ---->               ')
    print('-------------|------ > -----|---- < -----|------------')
    print(' ')

    judul   = input('Masukkan judul    = ')
    penulis = input('Masukkan penulis  = ')
    isbn    = input('Masukkan isbn     = ')

    buku_baru =     {
        'judul'  : judul,
        'penulis': penulis,
        'isbn'   : isbn
    }

    daftar_buku.append(buku_baru)

    print(' ')
    print(f'{judul} [isbn:{isbn}] telah berhasil ditambahkan')
    print(' ')

def daftarBuku():
    print(' ')
    print('                <---- Daftar Buku ---->               ')
    print('-------------|------ > -----|---- < -----|------------')
    print(' ')

    print('Berikut list daftar buku = ')
    for buku in daftar_buku:
        print(f"    - {buku['judul']}")

def hapusBuku():
    print(' ')
    print('                 <---- Hapus Buku ---->               ')
    print('-------------|------ > -----|---- < -----|------------')
    print(' ')

    print('berikut list daftar buku = ')
    for buku in daftar_buku:
        print(f"    - {buku['judul']}")
    print(' ')

    hapus_buku = input('Masukkan judul buku = ')
    print(' ')

    buku_ditemukan = False
    for buku in daftar_buku:
        if buku['judul'] == hapus_buku:
            buku_ditemukan = True
            daftar_buku.remove(buku)

            print(f'         {hapus_buku} TELAH DI HAPUS DARI DAFTAR BUKU         ')
            print(' ')

            print('Daftar buku yang masih ada : ')
            for buku_terbaru in daftar_buku:
                print(f'    - {buku_terbaru['judul']}')      
            break
         
    if not buku_ditemukan:
        print('         !!!-  BUKU TIDAK DI TEMUKAN  -!!!         ')

def anggota() :
    while True:
        print(' ')
        print(' ')
        print('               <---- Sistem Anggota ---->             ')
        print('-------------|------ ++++++++++++++ -----|------------')
        print("""
                1. Tambah anggota
                2. Lihat daftar anggota
                3. Hapus anggota
                4. Kembali ke awal
        """)

        pilihan = input('masukkan pilihan = ')

        if pilihan == '1':
            tambahAnggota()
        elif pilihan == '2':
            daftarAnggota()
        elif pilihan == '3':
            hapusAnggota()
        elif pilihan == '4':
            tampilanAwal()
        else:
            print(' ')
            print('            !!!-  PILIHAN TIDAK ADA  -!!!         ')

def tambahAnggota():
    print(' ')
    print('              <---- Tambah Anggota ---->              ')
    print('-------------|------ > -----|---- < -----|------------')
    print(' ')

    nama   = input('masukkan nama     = ')
    alamat = input('masukkan alamat   = ')
    nim    = input('masukkan nim      = ')

    anggota_baru =     {
        'nama'  : nama,
        'alamat': alamat,
        'nim'   : nim
    }

    daftar_anggota.append(anggota_baru)

    print(' ')
    print(f'anggota {nama} [nim:{nim}] telah berhasil ditambahkan')
    print(' ')

def daftarAnggota():
    print(' ')
    print('               <---- Daftar Anggota ---->             ')
    print('-------------|------ > -----|---- < -----|------------')
    print(' ')

    print('berikut list daftar anggota = ')
    for anggota in daftar_anggota:
        print(f"    - {anggota['nama']}")

def hapusAnggota():
    print(' ')
    print('               <---- Hapus Anggota ---->              ')
    print('-------------|------ > -----|---- < -----|------------')
    print(' ')

    print('Pilih anggota yang akan dihapus : ')
    for anggota in daftar_anggota:
        print(f"    - {anggota['nama']}")
    print(' ')

    hapus_anggota = input('Masukkan nama anggota = ')
    print(' ')

    anggota_ditemukan = False
    for anggota in daftar_anggota:
        if anggota['nama'] == hapus_anggota:

            anggota_ditemukan = True
            daftar_anggota.remove(anggota)

            print(f'         {hapus_anggota} TELAH DI HAPUS DARI ANGGOTA         ')
            print(' ')

            print('Nama yang masih sebagai anggota : ')
            for anggota_terbaru in daftar_anggota:
                print(f'    - {anggota_terbaru['nama']}')   

            break

    if not anggota_ditemukan :
        print('         !!!-  ANGGOTA TIDAK DI TEMUKAN  -!!!         ')

def peminjaman ( ) :
    while True :
        print(' ')
        print(' ')
        print('           <---- Sistem Peminjaman Buku ---->         ')
        print('-------------|------ ++++++++++++++ -----|------------')
        print("""
                1. Pinjam Buku
                2. Daftar Anggota Peminjam Buku
                3. Data Detail Anggota Peminjam Buku
                4. Kembali Ke Awal
        """)

        pilihan = input('Masukkan Pilihan = ')
        print(' ')

        if pilihan == '1' :
            pinjamBuku()
        elif pilihan == '2' :
            daftarPeminjam()
        elif pilihan == '3' :
            dataDetailPeminjam()
        elif pilihan == '4' :
            tampilanAwal()
        else :
            print(' ')
            print('            !!!-  PILIHAN TIDAK ADA  -!!!         ')

def pinjamBuku ( ) :
    print(' ')
    print('                <---- Pinjam Buku ---->               ')
    print('-------------|------ > -----|---- < -----|------------')
    print(' ')

    print('Daftar buku yang tersedia = ')
    for judul_tersedia in daftar_buku:
        print(f"    - {judul_tersedia['judul']}")

    print(' ')


    nama             = input('Masukkan Nama  = ')
    nim              = input('Masukkan Nim   = ')
    judul            = input('Masukkan Judul = ')
    tgl_minjam       = date.today()
    tgl_pengembalian = tgl_minjam + timedelta(days=7)

    data_peminjaman_baru = {
        'nama' : nama,
        'nim'  : nim,
        'judul': judul,
        'tgl_minjam' : tgl_minjam,
        'tgl_pengembalian' : tgl_pengembalian
    }

    data_peminjaman.append(data_peminjaman_baru)

    print(' ')
    print(f'{nama} meminjam buku {judul}, waktu pengembalian : {tgl_pengembalian}')
    print(' ')

def daftarPeminjam():
    print(' ')
    print('          <---- Daftar Peminjaman Buku ---->          ')
    print('-------------|------ > -----|---- < -----|------------')
    print(' ')

    print('Daftar nama yang meminjam buku : ')
    for nama_peminjam in data_peminjaman:
        print(f"    - {nama_peminjam['nama']}")
    
def dataDetailPeminjam():
    print(' ')
    print('         <---- Data Detail Peminjam Buku ---->        ')
    print('-------------|------ > -----|---- < -----|------------')
    print(' ')

    print('Cari berdasarkan nama')
    print(' ')
    print('---------------------------------------------------------')
    nama = input('Masukkan nama = ')

    print(' ')

    data_ditemukan = False

    for detail_peminjam in data_peminjaman:
        if detail_peminjam['nama'] == nama:
            data_ditemukan = True
            
            print(f'Nama peminjam         = {detail_peminjam["nama"]}')
            print(f'Nim peminjam          = {detail_peminjam["nim"]}')
            print(f'Buku yang di pinjam   = {detail_peminjam["judul"]}')
            print(f'Tanggal peminjaman    = {detail_peminjam["tgl_minjam"]}')
            print(f'Tanggal pengembalian  = {detail_peminjam["tgl_pengembalian"]}')

            break

    if not data_ditemukan:
            print('ANGGOTA TIDAK TERDAFTAR DALAM PEMINJAMAN BUKU')





print(' ')
print('                 <------------------->                ')
print('-------------|------ LOGIN PROGRAM -----|-------------')
print('                 <------------------->                ')
print(' ')

while True:
    username = input('Username = ')
    password = input('Password = ')

    print(' ')

    if username == 'dany' and password == 'root':
        while True:
            tampilanAwal()
    else:
        print('       !!!-  USERNAME ATAU PASSWORD SALAH  -!!!       ')
        print(' ')


