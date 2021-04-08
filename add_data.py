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

def add_data_user(data_yang_akan_ditambah):
    data=data_yang_akan_ditambah
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
            if username==data_yang_akan_ditambah[j][1]:
                os.system("cls")
                j=jumlah_baris-1 #agar keluar loop searching unique username"
                stage-=1 #stage dikurang 1 agar tidak keluar loop while
                print("Mohon Maaf, username sudah terpakai, mohon coba lagi")
            elif j == jumlah_baris-1:
                print("Anda akan membuat {} sebagai username".format(username))
                validasi=input("Apakah sudah benar? (y/n) : ")
                if validasi=='y':
                    os.system("cls")
                    print("Username Berhasil dibuat")
                else:
                    os.system("cls")
                    stage-=1
        stage+=1
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
    verivikasi_akhir=str(input("Apakah Anda akan menambah data tersebut? (y/n) : "))
    if verivikasi_akhir=='y':
        #memasukkan ke data utama
        data.append(list_dummy)
        print("Data Berhasil ditambah")
        return data
    else:
        print("Data tidak ditambah")
        return data

#Contoh Penggunaan
'''
data=read_csv("clone.csv")
add_data(data)
write_csv(data,"clone.csv")
'''