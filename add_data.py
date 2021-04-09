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

#ID yang dimaskud adalah ID gadgetnya
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

#ID yang dimaksud adalah ID comsumablenya
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

#Masukkan ID usernya bukan usernamenya
def add_data_consumable_history(id_pengambil,consumable,consumable_history):
    data=consumable_history
    os.system("cls")
    stage=0
    list_dummy=[]
    #ID pengambilan
    while stage==0:
        stage+=1
    list_dummy.append(len(data))
    #ID pengambil
    while stage==1:
        stage+=1
    list_dummy.append(id_pengambil)
    #ID consumable
    while stage==2:
        print("ID Consumable    : ")
        print("Nama Consumable  : ")
        print("Jumlah           : ")
        print("Tanggal          : ")
        print("")
        id_consumable=input("Masukkan ID consumbale yang akan di ambil : ")
        for j in range(len(consumable)):
            if id_consumable==consumable[j][0]:
                j=len(consumable)-1 #agar langsung keluar loop for j
                os.system("cls")
                print("ID           :",consumable[j][0])
                print("Nama         :",consumable[j][1])
                print("Deskripsi    :",consumable[j][2])
                print("Jumlah       :",consumable[j][3])
                print("Rarity       :",consumable[j][4])
                print("")
                valisdasi=input("Apakah Anda akan mengambil consumable tersebut? (y/n) : ")
                if valisdasi=='y':
                    os.system("cls")
                    nomor_consumable=j
                    nama_consumable=consumable[j][1]
                    stage+=1
                else:
                    os.system("cls")
            elif(j==len(consumable)-1):
                os.system("cls")
                print("Consumable tidak terdaftar")
    list_dummy.append(id_consumable)
    #Jumlah 
    # (tidak ditambahkan ke dalam data consumable_history.csv)
    while stage==3:
        print("ID Consumable    : ",id_consumable)
        print("Nama Consumable  : ",nama_consumable)
        print("Jumlah           : ")
        print("Tanggal          : ")
        print("")
        try:
            jumlah=int(input("Masukkan jumlah consumable yang akan diambil : "))
        except ValueError:
            os.system("cls")
            print("Jumlah harus dalam bentuk bilangan bulat")
        else:
            if jumlah<0:
                os.system("cls")
                print("Jumlah harus lebih dari 0")
            elif consumable[nomor_consumable][3]-jumlah<0:
                os.system("cls")
                print("Jumlanh yang akan diambil melebihi persediaan. Jumlah penagambilan maksimal: {}".format(consumable[nomor_consumable][3]))
            else:
                print("Anda akan mengambil {} sebanyak {} buah".format(nama_consumable,jumlah))
                validasi=input("Apakah sudah benar? (y/n) : ")
                if validasi=='y':
                    os.system("cls")
                    stage+=1
                else:
                    os.system("cls")
    #tanggal
    while stage==4:
        print("ID Consumable    : ",id_consumable)
        print("Nama Consumable  : ",nama_consumable)
        print("Jumlah           : ",jumlah)
        print("Tanggal          : ")
        print("")
        tanggal=input("Masukkan tanggal pengambilan (dd/mm/yyyy) : ")
        print("Anda akan memasukkan {} sebagai tanggal pengambilan".format(tanggal))
        validasi=input("Apakah sudah benar? (y/n) : ")
        if validasi=='y':
            os.system("cls")
            stage+=1
        else:
            os.system("cls")
            print("Tanggal gagal dimasukkan")
    list_dummy.append(tanggal)

    #Verifikasi Terakhir
    print("ID pengambil     : ",id_pengambil)
    print("ID Consumable    : ",id_consumable)
    print("Nama Consumable  : ",nama_consumable)
    print("Jumlah           : ",jumlah)
    print("Tanggal          : ",tanggal)
    print("")
    print("Anda akan mengambil consumable sesuai data tersebut")
    verivikasi_akhir=input("Apakah sudah benar? (y/n) : ")
    if verivikasi_akhir=='y':
        consumable[nomor_consumable][3]=consumable[nomor_consumable][3]-jumlah
        consumable_history.append(list_dummy)
        return consumable,consumable_history
    else:
        return consumable,consumable_history

def add_data_gadget_borrow_history(id_pengambil,gadget,gadget_history):
    data=gadget_history
    os.system("cls")
    stage=0
    list_dummy=[]
    #ID pengambilan
    while stage==0:
        stage+=1
    list_dummy.append(len(data))
    #ID pengambil
    while stage==1:
        stage+=1
    list_dummy.append(id_pengambil)
    #ID gadget
    while stage==2:
        print("ID gadget        : ")
        print("Nama gadget      : ")
        print("Jumlah           : ")
        print("Tanggal          : ")
        print("")
        id_gadget=input("Masukkan ID consumbale yang akan di ambil : ")
        for j in range(len(gadget)):
            if id_gadget==gadget[j][0]:
                j=len(gadget)-1 #agar langsung keluar loop for j
                os.system("cls")
                print("ID               : ",gadget[j][0])
                print("Nama             : ",gadget[j][1])
                print("Deskripsi        : ",gadget[j][2])
                print("Jumlah           : ",gadget[j][3])
                print("Rarity           : ",gadget[j][4])
                print("Tahun Ditemukan  : ",gadget[j][5])
                print("")
                valisdasi=input("Apakah Anda akan mengambil gadget tersebut? (y/n) : ")
                if valisdasi=='y':
                    os.system("cls")
                    nomor_gadget=j
                    nama_gadget=gadget[j][1]
                    stage+=1
                else:
                    os.system("cls")
            elif(j==len(gadget)-1):
                os.system("cls")
                print("gadget tidak terdaftar")
    list_dummy.append(id_gadget)
    #Jumlah 
    #ditambahkan pada kolom ke-5
    while stage==3:
        print("ID gadget        : ",id_gadget)
        print("Nama gadget      : ",nama_gadget)
        print("Jumlah           : ")
        print("Tanggal          : ")
        print("")
        try:
            jumlah=int(input("Masukkan jumlah gadget yang akan diambil : "))
        except ValueError:
            os.system("cls")
            print("Jumlah harus dalam bentuk bilangan bulat")
        else:
            if jumlah<0:
                os.system("cls")
                print("Jumlah harus lebih dari 0")
            elif gadget[nomor_gadget][3]-jumlah<0:
                os.system("cls")
                print("Jumlanh yang akan diambil melebihi persediaan. Jumlah penagambilan maksimal: {}".format(gadget[nomor_gadget][3]))
            else:
                print("Anda akan mengambil {} sebanyak {} buah".format(nama_gadget,jumlah))
                validasi=input("Apakah sudah benar? (y/n) : ")
                if validasi=='y':
                    os.system("cls")
                    stage+=1
                else:
                    os.system("cls")
    #tanggal
    while stage==4:
        print("ID gadget        : ",id_gadget)
        print("Nama gadget      : ",nama_gadget)
        print("Jumlah           : ",jumlah)
        print("Tanggal          : ")
        print("")
        tanggal=input("Masukkan tanggal pengambilan (dd/mm/yyyy) : ")
        print("Anda akan memasukkan {} sebagai tanggal pengambilan".format(tanggal))
        validasi=input("Apakah sudah benar? (y/n) : ")
        if validasi=='y':
            os.system("cls")
            stage+=1
        else:
            os.system("cls")
            print("Tanggal gagal dimasukkan")
    list_dummy.append(tanggal)
    list_dummy.append(jumlah)

    #Verifikasi Terakhir
    print("ID pengambil     : ",id_pengambil)
    print("ID gadget        : ",id_gadget)
    print("Nama gadget      : ",nama_gadget)
    print("Jumlah           : ",jumlah)
    print("Tanggal          : ",tanggal)
    print("")
    print("Anda akan mengambil gadget sesuai data tersebut")
    verivikasi_akhir=input("Apakah sudah benar? (y/n) : ")
    if verivikasi_akhir=='y':
        gadget[nomor_gadget][3]=gadget[nomor_gadget][3]-jumlah
        gadget_history.append(list_dummy)
        return gadget,gadget_history
    else:
        return gadget,gadget_history

def delete_gadget(id_gadget_yang_akan_dihapus,gadget):
    os.system("cls")
    baris_gadget=0
    for j in range(len(gadget)):
        if id_gadget_yang_akan_dihapus==gadget[j][0]:
            baris_gadget=j
    if baris_gadget==0:
        print("Tidak ada item dengan ID tersebut")
    else:
        print("ID gadget        : ",gadget[baris_gadget][0])
        print("Nama gadget      : ",gadget[baris_gadget][1])
        print("Deskripsi        : ",gadget[baris_gadget][2])
        print("Jumlah           : ",gadget[baris_gadget][3])
        print("Rarity           : ",gadget[baris_gadget][4])
        print("Tahun ditemukan  : ",gadget[baris_gadget][5])
        print("")
        validasi=input("Apakah Anda yakin akan menghapus gadget tersebut? (y/n) : ")
        if validasi=='y':
            del gadget[baris_gadget]
            return gadget
        else:
            return gadget
#Contoh Penggunaan
'''
data=read_csv("clone.csv")
add_data(data)
write_csv(data,"clone.csv")
'''