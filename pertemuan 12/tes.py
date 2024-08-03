# Import library
import sys

# Data pengguna (sebagai contoh)
users = {
    "user1": "password1",
    "user2": "password2"
}

# Fungsi untuk menampilkan menu utama
def show_menu():
    print("\nMenu Utama:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Keluar")

# Fungsi untuk login
def login():
    print("Silakan login")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login berhasil!")
        return True
    else:
        print("Username atau password salah!")
        return False

# Fungsi untuk menambahkan data
def tambah_data(data_dict):
    key = input("Masukkan kunci: ")
    value = input("Masukkan nilai: ")
    data_dict[key] = value
    print("Data berhasil ditambahkan!")

# Fungsi untuk menampilkan data
def tampilkan_data(data_dict):
    if data_dict:
        print("\nData yang tersimpan:")
        for key, value in data_dict.items():
            print(f"{key}: {value}")
    else:
        print("Belum ada data yang tersimpan!")

# Program utama
def main():
    data_dict = {}
    logged_in = False

    while not logged_in:
        logged_in = login()

    while True:
        show_menu()
        choice = input("Pilih menu: ")

        if choice == "1":
            tambah_data(data_dict)
        elif choice == "2":
            tampilkan_data(data_dict)
        elif choice == "3":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
