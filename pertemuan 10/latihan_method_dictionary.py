print('------------------------------------------------------------------')
print('------------------- LATIHAN METHOD DICTIONARY --------------------')
print('------------------------------------------------------------------')

print(' ')

merk_motor          = input('Masukkan merk motor anda        : ')
type_motor          = input('Masukkan type motor anda        : ')
warna_motor         = input('Masukkan warna motor anda       : ')
kecepatan_motor     = input('Masukkan kecepatan motor        : ')
tahun_beli_motor    = input('Masukkan tahun pembelian motor  : ')

identitas_motor = {
    'Merk Motor'        : merk_motor,
    'Type Motor'        : type_motor,
    'Warna Motor'       : warna_motor,
    'Kecepatan Motor'   : kecepatan_motor,
    'Tahun Beli Motor'  : tahun_beli_motor
}

print(' ')

while True :
    print('Macam-macam Pilihan Program : ')
    print('1. Program Method Copy')
    print('2. Program Method Fromkey')
    print('3. Program Mencari Value')
    print('4. Keluar Program')

    print(' ')

    pilihan_program = input('Masukkan Pilihan Program : ')
    if ( pilihan_program == '1' ) :
        identitas_motor_baru = identitas_motor.copy()
        print('Directory lama : ', identitas_motor)
        print('Directory baru : ', identitas_motor_baru)
        print(' ')
    elif ( pilihan_program == '2' ) :
        dict = dict.fromkeys(identitas_motor)
        print('Biodata Mahasiswa Baru ', dict)
        print(' ')

        dict = dict.fromkeys(identitas_motor,'Dany')
        print('Biodata Mahasiswa yang lebih baru : ', dict)
        print('')
    elif ( pilihan_program == '3' ) :
        values = list(identitas_motor.values())
        print('Value : ', values)
        print(' ')
    elif ( pilihan_program == '4' ) :
        exit()
    else :
        print('Pilih Sesuai dengan pilihan yang ada')


