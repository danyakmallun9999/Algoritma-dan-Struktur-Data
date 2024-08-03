print('===============================================================================')
print('============ Program 1 Latihan menambahkan di dictionary di python ============')
print('===============================================================================')
print(' ')

nama            = input('Masukkan nama anda             : ')
alamat          = input('Masukkan alamat rumah anda     : ')
tempat_lahir    = input('Masukkan tempat lahir          : ')
tanggal_lahir   = input('Masukkan tanggal lahir         : ')
program_studi   = input('Masukkan program studi         : ')
nim             = input('Masukkan nim                   : ')

biodata_mahasiswa = {
    'Nama'          : nama,
    'Alamat'        : alamat,
    'Tempat Lahir'  : tempat_lahir,
    'Tanggal Lahir' : tanggal_lahir,
    'Program Studi' : tanggal_lahir,
    'Nim'           : nim
}

print(' ')
print(' ')
print('Cetak : ')
print(' ')

print('Nama             : ', biodata_mahasiswa['Nama'])
print('Alamat           : ', biodata_mahasiswa['Alamat'])
print('Tempat Lahir     : ', biodata_mahasiswa['Tempat Lahir'])
print('Tanggal Lahir    : ', biodata_mahasiswa['Tanggal Lahir'])
print('Program Studi    : ', biodata_mahasiswa['Program Studi'])
print('Nim              : ', biodata_mahasiswa['Nim'])