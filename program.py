import os

# Struktur database
TEMPLATE = {
    "nama": 20*" ",
    "kamar": 20*" ",
    "lama_menginap": 20*" ",
    "tagihan": 20*" ",
}

# Fungsi untuk melihat list kamar
def daftar_kamar():
    os.system("cls")
    print("="*33)
    print("No |   Jenis Kamar  | Harga Kamar")
    print("="*33)
    with open("room.txt", "r") as file:
        data = file.readlines()

        for index,content in enumerate(data):
            content = content.split(",")
            kamar = content[0]
            harga = content[1]
            print(f"{index+1:2} | {kamar} | {harga}")

    print("="*33)

    input_data()
    
# Fungsi untuk menginput data dari user    
def input_data():
    no = int(input("Masukkan Nomor Kamar : "))
    os.system("cls")
    lama_menginap = int(input("Masukkan Lama Menginap : "))
    nama = input("Masukkan Nama Anda : ")

    with open("room.txt", "r") as file:
        content = file.readlines()

        for index,data in enumerate(content):
            data = data.split(",")
            kamar = data[0]
            harga_kamar = int(data[1])
            if index == no - 1:
                break
        
    tagihan = harga_kamar * lama_menginap
    tagihan = str(tagihan)
    lama_menginap = str(lama_menginap)

    database = TEMPLATE.copy()
    
    database["nama"] = nama + TEMPLATE["nama"][len(nama):]
    database["kamar"] = kamar  + TEMPLATE["kamar"][len(kamar):]
    database["lama_menginap"] = lama_menginap  + TEMPLATE["lama_menginap"][len(lama_menginap):]
    database["tagihan"] = tagihan  + TEMPLATE["tagihan"][len(tagihan):]

    data_str = f"{database['nama']},{database['kamar']},{database['lama_menginap']},{database['tagihan']}\n"

    with open("data.txt","a") as file:
        file.write(data_str)

    hasil_belanja(nama, kamar, lama_menginap, tagihan)

def hasil_belanja(nama, kamar, lama_menginap, tagihan):
    os.system("cls")
    print("="*50)
    print("Silahkan Cek Data Anda".center(50))
    print("="*50)
    print(f"Nama                : {nama}")
    print(f"Kamar Yang Di Pesan : {kamar}")
    print(f"Lama Menginap       : {lama_menginap}")
    print(f"Total Tagihan       : {tagihan}")
    print("="*50)
    x = input("")

# Fungsi manmpilkan menu admin
def menu_admin():
    os.system("cls")
    print("Selamat Datang Di Program".center(60))
    print("Booking Hotel".center(59) + "\n")
    print("1. Read Data")
    print("2. Sort Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit\n")     

# Fungsi untuk membaca database
def baca_data():
    os.system("cls")
    print("="*81)
    print("No |         Nama        |         Kamar        | Lama Menginap |     Tagihan   |")
    print("="*81)

    with open("data.txt","r") as file:
        content = file.readlines()

        for no,data in enumerate(content):
            data = data.split(",")
            nama = data[0]
            kamar = data[1]
            lama_menginap = data[2] 
            tagihan = data[3].replace("\n", "")

            print(f"{no+1:2} | {nama} | {kamar} | {lama_menginap:.10}hari| Rp.{tagihan:.10}|")

    print("="*81)
    x = input("")

# Fungsi untuk sorting
def sorting():
    os.system("cls")
    print("="*81)
    print("No |         Nama        |         Kamar        | Lama Menginap |     Tagihan   |")
    print("="*81)

    with open("data.txt","r") as file:
        content = file.readlines()
        data_tuple = [tuple(line.strip().split(',')) for line in content]
        data_sort = sorted(data_tuple, key=lambda x:x[0])
        for no,data in enumerate(data_sort):
            nama = data[0]
            kamar = data[1]
            lama_menginap = data[2] 
            tagihan = data[3].replace("\n", "")

            print(f"{no+1:2} | {nama} | {kamar} | {lama_menginap:.10}hari| Rp.{tagihan:.10}|")

    print("="*81)
    x = input("")

# Fungsi untuk update data
def update():
    baca_data()
    no = int(input("Masukkan Nomor : "))

    with open("data.txt","r") as file:
        content = file.readlines() 
        
        for index,data in enumerate(content):
            if index == no - 1:
                data = data.split(",")
                nama = data[0].strip()
                kamar = data[1].strip()
                lama_menginap = data[2].strip() 
                tagihan = data[3].replace("\n", "")
                break
        
    hasil_belanja(nama, kamar, lama_menginap, tagihan)
    nama = input("Masukkan Nama Baru : ")

    database = TEMPLATE.copy()
    
    database["nama"] = nama + TEMPLATE["nama"][len(nama):]
    database["kamar"] = kamar  + TEMPLATE["kamar"][len(kamar):]
    database["lama_menginap"] = lama_menginap  + TEMPLATE["lama_menginap"][len(lama_menginap):]
    database["tagihan"] = tagihan  + TEMPLATE["tagihan"][len(tagihan):]

    data_str = f"{database['nama']},{database['kamar']},{database['lama_menginap']},{database['tagihan']}\n"

    with open("data.txt","r+") as file:
        file.seek(len(data_str) * (no - 1))
        file.write(data_str)

    hasil_belanja(nama, kamar, lama_menginap, tagihan)

# FUngsi untuk delete data
def hapus_data():
    baca_data()
    no = int(input("Masukkan Nomor : "))

    with open("data.txt","r") as file :
        content = file.readlines()

        for index,data in enumerate(content):
            if index == no - 1:
                data = data.split(",")
                nama = data[0].strip()
                kamar = data[1].strip()
                lama_menginap = data[2].strip() 
                tagihan = data[3].replace("\n", "")
                break
        
        hasil_belanja(nama, kamar, lama_menginap, tagihan)

        opsi = input("Yakin Ingin dihapus (y/t) : ")
        if opsi == "y" or opsi == "Y":
            with open("data.txt","w") as file:
                    for index,data in enumerate(content):
                        if index != no -1 :
                            file.write(data)

# program dimulai
while True:
    os.system("cls")
    print("Selamat Datang Di Program".center(60))
    print("Booking Hotel".center(59) + "\n")
    print("1. Menu User\n2. Menu Admin")
    opsi = input("Masukkan Nomor : ")
    if opsi == "1":
        while True:
            daftar_kamar()
            opsi = input("Apakah Selesai (y/n): ")
            if opsi == "y":
                break
    else:
        while True:
            menu_admin()
            opsi = input("Masukkan Nomor : ")
            match opsi:
                case "1": baca_data()
                case "2": sorting()
                case "3": update()
                case "4": hapus_data()
                case "5": break