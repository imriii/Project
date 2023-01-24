import os
import platform
import random
import time
import sys

#DEF
def clearTerminal():
	#Untuk sistem Windows
	if( platform.system() == "Windows"):
		os.system('cls')
def list_menu():
    print("=" * 36)
    print("Aplikasi Pesan Hotel Surabaya")
    print("-" * 36)
    print("1","Pilih Hotel Anda")
    print("2","Tentang Aplikasi")
    print("3","Keluar Aplikasi")
    print("-" * 36)
def list_hotel():
    print("=" * 36)
    print("Daftar Hotel yang Tersedia")
    print("-" * 36)
    print("1","Horison Plaza Surabaya")
    print("2","Alexander Hotel Surabaya")
    print("3","Karlita Hotel Surabaya")
    print("-" * 36)
def kamar():
    print("=" * 36)
    print("Pilih Kamar")
    print("-" * 36)
    print("1","Standart Room")
    print("2","Deluxe Room")
    print("-" * 36)
def pemesanan():
    #Header
    print("=" * 36)
    print("Mengisi Data Diri")
    print("-" * 36)
    #Input Biodata
    clearTerminal()
    print("=" * 36)
    print("Pembayaran")
    print("-" * 36)
    nama = input("Masukan Nama Anda      : ")
    no_hp = input("Masukan Nomor HP Anda    : ")
    email = input("Masukan Email Anda       : ")
    lama_menginap = int(input("Berapa lama menginap    : "))
    harga_total= harga_kamar * lama_menginap
    print("Harga Sewa Hotel       :",harga_total)

    #PROSES NOTA
    print("-" * 36)
    print("Sedang Memproses NOTA. . .")
    time.sleep(3)
    while True:
        #Output Nota
        clearTerminal()
        print("=" * 36)
        print("Bukti Pembayaran")
        print("-" * 36)
        print("Nomer Kamar Hotel        : ",random.randint(1,100))
        print("Nama Hotel               : ",nama_hotel)
        print("Jenis kamar              : ",jenis_kamar)
        print("Nama Pemesan             : ",nama)
        print("No HandPhone             : ",no_hp)
        print("Alamat Email             : ",email)
        print("Lama Menginap            : ",lama_menginap , "hari")
        print("Total Harga              : ",harga_total)
        print("-" * 36)
        exit=input("Enter Untuk Keluar . . .")
        if exit == "":
            clearTerminal()
            print("Terimakasih Sudah Menggunakan Aplikasi Kami :)\n")
            sys.exit()
clearTerminal()
print("=" * 36)
print("Aplikasi Pesan Hotel Surabaya")
print("-" * 36)
print("1","Pilih Hotel Anda")
print("2","Tentang Aplikasi")
print("3","Keluar Aplikasi")
print("-" * 36)
input_menu = int(input("Masukan Pilihan Anda : "))
print("-" * 36)

#Jika Input Menu Memilih Nomer 1
if(input_menu == 1):
    clearTerminal()
    list_hotel()
    input_hotel = int(input("Masukan Hotel Pilihan Anda : "))

#Horison Plaza
    if (input_hotel == 1):
        nama_hotel = "Horison Plaza Tegal"
        clearTerminal()
        kamar()
        input_kamar = input("Masukan Pilihan kamar Anda : ")
        if (input_kamar == "1"):
            jenis_kamar = "Standart Room"
            harga_kamar = 200000 
            pemesanan() 
        elif(input_kamar == "2"):
            jenis_kamar = "Deluxe Room"
            harga_kamar = 350000
            pemesanan()
        else:
            print("Anda Salah Memasukan Kode")
#Alexander Hotel
    elif (input_hotel == 2):
        nama_hotel = "Alexander Hotel Tegal"
        clearTerminal()
        kamar()
        input_kamar = input("Masukan Pilihan kamar Anda : ")
        if (input_kamar == "1"):
            jenis_kamar = "Standart Room"
            harga_kamar = 300000
            pemesanan() 
        elif(input_kamar == "2"):
            jenis_kamar = "Deluxe Room"
            harga_kamar = 450000
            pemesanan()
        else:
            print("Anda Salah Memasukan Kode")
#Karlita Hotel
    elif (input_hotel == 3):
        nama_hotel = "Karlita Hotel Tegal"
        clearTerminal()
        kamar()
        input_kamar = input("Masukan Pilihan kamar Anda : ")
        if (input_kamar == "1"):
            jenis_kamar = "Standart Room"
            harga_kamar = 250000
            pemesanan()        
        elif(input_kamar == "2"):
            jenis_kamar = "Deluxe Room"
            harga_kamar = 325000
            pemesanan()
        else:
            print("Anda Salah Memasukan Kode")
    else:
        print("\n")
        print("Input Salah !! \n")
#Jika Input Menu Memilih Nomer 2
elif(input_menu == 2):
    clearTerminal()
    print("=" * 47)
    print("Aplkasi Sewa Hotel Sederhana Yang dibuat oleh")
    print("-" * 47)
    print("1","Arie Firmansyah ")
    print("2","Je'izza Alya Nabila")
    print("-" * 47)
    exit=input("Enter Untuk Keluar . . .")
    if exit == "":
        clearTerminal()
        sys.exit()
#Jika Input Menu Memilih Nomer 3
elif(input_menu == 3):
    clearTerminal()
    print("Terima kasih,telah menggunakan aplikasi kami :) \n")
    exit()

else:
    print("Anda Salah Memasukan Kode \n")