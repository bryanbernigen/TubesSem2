#READ ME
'''
    Fungsi akan menambah data yang diinput ke list awal. 
    Untuk membuat perubahannya terlihat di file csv, silahkan panggil fungsi pada write_csv.py
    Alur yang disarankan:
        1. baca data csv dengan memanggil read_csv(nama_file) ke sebuah variabel (contoh xyz)
        2. tambah data dengan memanggil add_data(xyz)
        3. masukkan data yang akan ditambahkan
        4. perbaharui data csv dengan write(xyz, nama_file_yang_akan_diperbaharui)
            catatan: jika nama_file == nama_file_yang_akan_deperbaharui maka data di nama_file akan tertimpa oleh data baru
'''
import os
from hashing import hashing

# Fungsi akan menambah data dengan jumlah kolom yang sama dengan data acuan;
# Fungsi tidak akan memvalidasi input yang sama (Contoh: Username sama tidak apa-apa)
# Jika ingin divalidasi silahkan  edit pada bagian meminta user untuk memasukkan data
def add_data(data_yang_akan_ditambah):
    data=data_yang_akan_ditambah
    #jumlah_baris=len(data)
    jumlah_kolom=len(data[0])

    #meminta user untuk memasukkan data yang akan ditambahkan
    list_dummy=[]
    for i in range (jumlah_kolom):
        if (type(data))=='int':
            dummy=int(input("Masukkan {} :".format(data[0][i])))
            list_dummy.append(dummy)
        elif (type(data))=='float':
            dummy=float(input("Masukkan {} :".format(data[0][i])))
            list_dummy.append(dummy)
        else :
            dummy=str(input("Masukkan {} :".format(data[0][i])))
            list_dummy.append(dummy)
    #memasukkan ke data utama
    data.append(list_dummy)

def add_data_user(user):
    data=user
    jumlah_baris=len(data)
    #jumlah_kolom=len(data[0])

    #Meminta user untuk memasukkan data yang akan ditambahkan
    #inisialisasi
    stage=0         #menandakan kolom ke-berapa yang akan diisi
    list_dummy=[]   #list kosong yang nantinya akan di append ke data utama
    #ID
    while stage==0:
        id=len(data)
        stage+=1
        os.system("cls")
        print("id berhasil dibuat")
    list_dummy.append(id)
    #username
    while stage==1:
        print("id           : ",id)
        print("username     :")
        print("nama         :")
        print("alamat       :")
        print("password     :")
        print("role         :")
        print("") 
        username=input("Masukkan Username : ")
        if len(username)>20:
            stage-=1
            j=jumlah_baris
            os.system("cls")
            print("Panjang username maksimal adalah 20 karakter")
        for j in range(jumlah_baris):
            if username==user[j][1]:
                os.system("cls")
                j=jumlah_baris-1 #agar keluar loop searching unique username"
                print("Mohon Maaf, username sudah terpakai, mohon coba lagi")
            elif j == jumlah_baris-1:
                print("Anda akan membuat {} sebagai username".format(username))
                validasi=input("Apakah sudah benar? (y/n) : ")
                if validasi=='y':
                    os.system("cls")
                    stage+=1
                    print("Username Berhasil dibuat")
                else:
                    os.system("cls")
                    print("Username gagal dibuat")
    list_dummy.append(username)
    #nama
    while stage==2:
        print("id           : ",id)
        print("username     : ",username)
        print("nama         :")
        print("alamat       :")
        print("password     :")
        print("role         :")
        print("")
        nama=input("Masukkan nama Anda : ")
        print("Anda akan membuat {} sebagai nama Anda".format(nama))
        validasi=input("Apakah sudah benar? (y/n) : ")
        if validasi=='y':
            stage+=1
            os.system("cls")
            print("nama berhasil dibuat")
        else:
            os.system("cls")
            print("nama gagal dibuat")
    list_dummy.append(nama)
    #alamat
    while stage==3:
        print("id           : ",id)
        print("username     : ",username)
        print("nama         : ",nama)
        print("alamat       :")
        print("password     :")
        print("role         :")
        print("")
        alamat=input("Masukkan alamat Anda : ")
        print('Anda akan memasukkan {} sebagai alamat Anda'.format(alamat))
        validasi=input("Apakah sudah benar? (y/n) : ")
        if validasi=='y':
            stage+=1
            os.system("cls")
            print("alamat berhasil dibuat")
        else:
            os.system("cls")
            print("Alamat gagal dimasukkan ke data")
    list_dummy.append(alamat)
    #password
    while stage==4:
        print("id           : ",id)
        print("username     : ",username)
        print("nama         : ",nama)
        print("alamat       : ",alamat)
        print("password     :")
        print("role         :")
        print("")
        password=input("Masukkan password Anda : ")
        if len(password)<12:
            print("Anda akan membuat {} sebagai passowrd Anda".format(password))
            validasi=input("Apakah sudah benar? (y/n) : ")
            if validasi=='y':
                password_hashed=hashing(password,username)
                stage+=1
                os.system("cls")
                print("password berhasil dibuat")
            else:
                os.system("cls")
                print("password gagal dibuat")
        else:
            os.system("cls")
            print("Makasimal panjang password adalah 12 karakter")
    list_dummy.append(password_hashed)
    #role
    while stage==5:
        print("id           : ",id)
        print("username     : ",username)
        print("nama         : ",nama)
        print("alamat       : ",alamat)
        print("password     : ",password)
        print("role         :")
        print("")
        role=input("Masukkan role Anda : ")
        if role!="admin" and role!="user":
            os.system("cls")
            print("role hanya ada admin atau user")
        else:
            print("Anda akan memasukkan {} sebagai role Anda".format(role)) 
            validasi=input("Apakah sudah benar? (y/n) : ")
            if validasi=='y':
                stage+=1
                os.system("cls")
            else:
                os.system("cls")
                print("role gagal dimuat")
    list_dummy.append(role)

    #Verivikasi akhir
    print("Anda akan memasukkan data berikut:")
    print("id           : ",id)
    print("username     : ",username)
    print("nama         : ",nama)
    print("alamat       : ",alamat)
    print("pasword      : ",password)
    print("role         : ",role)   
    verivikasi_akhir=(input("Apakah Anda akan menambah data tersebut? (y/n) : "))
    if verivikasi_akhir=='y':
        #memasukkan ke data utama
        data.append(list_dummy)
        print("Data Berhasil ditambah")
        return data
    else:
        print("Data tidak ditambah")
        return data

def add_data_gadget(id,gadget):
        os.system("cls")
        stage=0
        list_dummy=[]
        #ID
        while stage==0:
            stage+=1
            os.system("cls")
            print("ID berhasil dibuat")
        list_dummy.append(id)
        #Nama
        while stage==1:
            print("ID               : ",id)
            print("Nama             : ")
            print("Deskripsi        : ")
            print("Jumlah           : ")
            print("Rarity           : ")
            print("Tahun Ditemukan  : ")
            print("")
            nama=input("Masukkan nama barang : ")
            print("Anda akan memasukkan {} sebagai nama barang".format(nama))
            validasi=input("Apakah sudah benar? (y/n) : ")
            if validasi=='y':
                os.system("cls")
                stage+=1
                print("Nama barang berhasil dimasukkan")
            else:
                os.system("cls")
                print("Nama barang gagal dimasukkan")
        list_dummy.append(nama)
        #Deskripsi
        while stage==2:
            print("ID               : ",id)
            print("Nama             : ",nama)
            print("Deskripsi        : ")
            print("Jumlah           : ")
            print("Rarity           : ")
            print("Tahun Ditemukan  : ")
            print("")
            deskripsi=input("Masukkan Deskripsi Benda : ")
            print("Anda akan memasukkan {} ke deskripsi benda".format(deskripsi))
            validasi=input("Apakah sudah benar? (y/n) : ")
            if validasi=='y':
                os.system("cls")
                stage+=1
                print("Deskripsi benda berhasil ditambahkan")
            else:
                os.system("cls")
                print("Deskripsi benda gagal ditambahkan")
        list_dummy.append(deskripsi)
        #Jumlah
        while stage==3:
            print("ID               : ",id)
            print("Nama             : ",nama)
            print("Deskripsi        : ",deskripsi)
            print("Jumlah           : ")
            print("Rarity           : ")
            print("Tahun Ditemukan  : ")
            print("")
            try:
                jumlah=int(input("Masukkan jumlah benda : "))
            except ValueError:
                os.system("cls")
                print("Jumlah benda harus dalam bentuk integer")
            else:
                jumlah=int(jumlah)
                if jumlah<0:
                    os.system("cls")
                    print("Mohon maaf tahun tidak valid")
                else:
                    print("Anda akan memasukkan {} ke jumlah".format(jumlah))
                    validasi=input("Apakah sudah benar? (y/n) : ")
                    if validasi=='y':
                        os.system("cls")
                        stage+=1
                        print("Jumlah berhasil dimasukkan")
                    else:
                        os.system("cls")
                        print("jumlah gagal dimasukkan")
        list_dummy.append(jumlah)
        #Rarity
        while stage==4:
            print("ID               : ",id)
            print("Nama             : ",nama)
            print("Deskripsi        : ",deskripsi)
            print("Jumlah           : ",jumlah)
            print("Rarity           : ")
            print("Tahun Ditemukan  : ")
            print("")
            rarity=input("Masukkan rarity : ")
            if rarity!="C" and rarity!="B" and rarity!="A" and rarity!="S":
                os.system("cls")
                print("Rarity harus berupa 'C','B','A','S'")
            else:
                print("Anda akan memasukkan {} ke rarity".format(rarity))
                validasi=input("Apakah sudah benar? (y/n) : ")
                if validasi=='y':
                    os.system("cls")
                    stage+=1
                    print("rarity berhasil ditambahkan")
                else:
                    os.system("cls")
                    print("rarity gagal dimasukkan")
        list_dummy.append(rarity)
        #Tahun
        while stage==5:
            print("ID               : ",id)
            print("Nama             : ",nama)
            print("Deskripsi        : ",deskripsi)
            print("Jumlah           : ",jumlah)
            print("Rarity           : ",rarity)
            print("Tahun Ditemukan  : ")
            print("")
            try:
                tahun=int(input("Masukkan tahun benda ditemukkan : "))
            except ValueError:
                os.system("cls")
                print("Jumlah benda harus dalam bentuk integer")
            else:
                if tahun<0:
                    os.system("cls")
                    print("Mohon maaf tahun tidak valid")
                else:
                    print("Anda akan memasukkan {} ke tahun ditemukan".format(tahun))
                    validasi=input("Apakah sudah benar? (y/n) : ")
                    if validasi=='y':
                        os.system("cls")
                        stage+=1
                        print("Tahun ditemukan berhasil dimasukkan")
                    else:
                        os.system("cls")
                        print("Tahun ditemukan gagal dimasukkan")
        list_dummy.append(tahun)

        #Validasi terakhir
        os.system("cls")
        print("Anda akan menambahkan data berikut:")
        print("ID               : ",id)
        print("Nama             : ",nama)
        print("Deskripsi        : ",deskripsi)
        print("Jumlah           : ",jumlah)
        print("Rarity           : ",rarity)
        print("Tahun Ditemukan  : ",tahun)
        verivikasi_akhir=(input("Apakah Anda akan menambah data tersebut? (y/n) : "))
        if verivikasi_akhir=='y':
            gadget.append(list_dummy)
            return gadget
        else:
            return gadget

def add_data_consumable(id,consumable):
        os.system("cls")
        stage=0
        list_dummy=[]
        #ID
        while stage==0:
            stage+=1
            os.system("cls")
            print("ID berhasil dibuat")
        list_dummy.append(id)
        #Nama
        while stage==1:
            print("ID               : ",id)
            print("Nama             : ")
            print("Deskripsi        : ")
            print("Jumlah           : ")
            print("Rarity           : ")
            print("")
            nama=input("Masukkan nama barang : ")
            print("Anda akan memasukkan {} sebagai nama barang".format(nama))
            validasi=input("Apakah sudah benar? (y/n) : ")
            if validasi=='y':
                os.system("cls")
                stage+=1
                print("Nama barang berhasil dimasukkan")
            else:
                os.system("cls")
                print("Nama barang gagal dimasukkan")
        list_dummy.append(nama)
        #Deskripsi
        while stage==2:
            print("ID               : ",id)
            print("Nama             : ",nama)
            print("Deskripsi        : ")
            print("Jumlah           : ")
            print("Rarity           : ")
            print("")
            deskripsi=input("Masukkan Deskripsi Benda : ")
            print("Anda akan memasukkan {} ke deskripsi benda".format(deskripsi))
            validasi=input("Apakah sudah benar? (y/n) : ")
            if validasi=='y':
                os.system("cls")
                stage+=1
                print("Deskripsi benda berhasil ditambahkan")
            else:
                os.system("cls")
                print("Deskripsi benda gagal ditambahkan")
        list_dummy.append(deskripsi)
        #Jumlah
        while stage==3:
            print("ID               : ",id)
            print("Nama             : ",nama)
            print("Deskripsi        : ",deskripsi)
            print("Jumlah           : ")
            print("Rarity           : ")
            print("")
            try:
                jumlah=int(input("Masukkan jumlah benda : "))
            except ValueError:
                os.system("cls")
                print("Jumlah benda harus dalam bentuk integer")
            else:
                jumlah=int(jumlah)
                if jumlah<0:
                    os.system("cls")
                    print("Mohon maaf tahun tidak valid")
                else:
                    print("Anda akan memasukkan {} ke jumlah".format(jumlah))
                    validasi=input("Apakah sudah benar? (y/n) : ")
                    if validasi=='y':
                        os.system("cls")
                        stage+=1
                        print("Jumlah berhasil dimasukkan")
                    else:
                        os.system("cls")
                        print("jumlah gagal dimasukkan")
        list_dummy.append(jumlah)
        #Rarity
        while stage==4:
            print("ID               : ",id)
            print("Nama             : ",nama)
            print("Deskripsi        : ",deskripsi)
            print("Jumlah           : ",jumlah)
            print("Rarity           : ")
            print("")
            rarity=input("Masukkan rarity : ")
            if rarity!="C" and rarity!="B" and rarity!="A" and rarity!="S":
                os.system("cls")
                print("Rarity harus berupa 'C','B','A','S'")
            else:
                print("Anda akan memasukkan {} ke rarity".format(rarity))
                validasi=input("Apakah sudah benar? (y/n) : ")
                if validasi=='y':
                    os.system("cls")
                    stage+=1
                    print("rarity berhasil ditambahkan")
                else:
                    os.system("cls")
                    print("rarity gagal dimasukkan")
        list_dummy.append(rarity)

        #Validasi terakhir
        os.system("cls")
        print("Anda akan menambahkan data berikut:")
        print("ID               : ",id)
        print("Nama             : ",nama)
        print("Deskripsi        : ",deskripsi)
        print("Jumlah           : ",jumlah)
        print("Rarity           : ",rarity)
        verivikasi_akhir=(input("Apakah Anda akan menambah data tersebut? (y/n) : "))
        if verivikasi_akhir=='y':
            consumable.append(list_dummy)
            return consumable
        else:
            return consumable


#Contoh Penggunaan
'''
data=read_csv("clone.csv")
add_data(data)
write_csv(data,"clone.csv")
'''