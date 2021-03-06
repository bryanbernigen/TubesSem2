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
import time
from hashing import hashing

# Fungsi akan menambah data dengan jumlah kolom yang sama dengan data acuan;
# Fungsi tidak akan memvalidasi input yang sama (Contoh: Username sama tidak apa-apa)
# Jika ingin divalidasi silahkan  edit pada bagian meminta user untuk memasukkan data
def validasi_tanggal(tanggal):
    tanggal=str(tanggal)
    if len(tanggal)!=10:
        return False
    if tanggal[2]!='/' or tanggal[5]!='/':
        return False
    hari=tanggal[0]+tanggal[1]
    bulan=tanggal[3]+tanggal[4]
    tahun=tanggal[6]+tanggal[7]+tanggal[8]+tanggal[9]
    hari=int(hari)
    bulan=int(bulan)
    tahun=int(tahun)
    if hari>31: return False
    if bulan>12: return False
    if tahun<0: return False
    if tahun%400==0: #kabisat
        if bulan==2:
            if hari<=28:
                return True
        elif bulan==1 or bulan==3 or bulan==5 or bulan==7 or bulan==8 or bulan==10 or bulan==12:
            if hari<=31:
                return True
        else:
            if hari<=30:
                return True
    elif tahun%100==0: #bukan kabisat
        if bulan==2:
            if hari<=29:
                return True
        elif bulan==1 or bulan==3 or bulan==5 or bulan==7 or bulan==8 or bulan==10 or bulan==12:
            if hari<=31:
                return True
        else:
            if hari<=30:
                return True        
    elif tahun%4==0: #kabisat
        if bulan==2:
            if hari<=28:
                return True
        elif bulan==1 or bulan==3 or bulan==5 or bulan==7 or bulan==8 or bulan==10 or bulan==12:
            if hari<=31:
                return True
        else:
            if hari<=30:
                return True
    else: #bukan kabisat
        if bulan==2:
            if hari<=29:
                return True
        elif bulan==1 or bulan==3 or bulan==5 or bulan==7 or bulan==8 or bulan==10 or bulan==12:
            if hari<=31:
                return True
        else:
            if hari<=30:
                return True         

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
        role="user"
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
                tahun=int(input("Masukkan tahun benda ditemukan : "))
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
                nomor_consumable=j
                j=len(consumable)-1 #agar langsung keluar loop for j
                os.system("cls")
                print("ID           :",consumable[nomor_consumable][0])
                print("Nama         :",consumable[nomor_consumable][1])
                print("Deskripsi    :",consumable[nomor_consumable][2])
                print("Jumlah       :",consumable[nomor_consumable][3])
                print("Rarity       :",consumable[nomor_consumable][4])
                print("")
                validasi=input("Apakah Anda akan mengambil consumable tersebut? (y/n) : ")
                if validasi=='y':
                    os.system("cls")
                    nama_consumable=consumable[nomor_consumable][1]
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
        if validasi_tanggal(tanggal):
            print("Anda akan memasukkan {} sebagai tanggal pengambilan".format(tanggal))
            validasi=input("Apakah sudah benar? (y/n) : ")
            if validasi=='y':
                os.system("cls")
                stage+=1
            else:
                os.system("cls")
                print("Tanggal gagal dimasukkan")
        else:
            os.system("cls")
            print("Tanggal tidak Valid")
    list_dummy.append(tanggal)
    list_dummy.append(jumlah)

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
        id_gadget=input("Masukkan ID gadget yang akan di ambil : ")
        for j in range(len(gadget)):
            if id_gadget==gadget[j][0]:
                nomor_gadget=j
                j=len(gadget)-1 #agar langsung keluar loop for j
                os.system("cls")
                print("ID               : ",gadget[nomor_gadget][0])
                print("Nama             : ",gadget[nomor_gadget][1])
                print("Deskripsi        : ",gadget[nomor_gadget][2])
                print("Jumlah           : ",gadget[nomor_gadget][3])
                print("Rarity           : ",gadget[nomor_gadget][4])
                print("Tahun Ditemukan  : ",gadget[nomor_gadget][5])
                print("")
                valisdasi=input("Apakah Anda akan mengambil gadget tersebut? (y/n) : ")
                if valisdasi=='y':
                    os.system("cls")
                    nama_gadget=gadget[nomor_gadget][1]
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
                print("Jumlah yang akan diambil melebihi persediaan. Jumlah pengambilan maksimal: {}".format(gadget[nomor_gadget][3]))
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
        if validasi_tanggal(tanggal):
            print("Anda akan memasukkan {} sebagai tanggal pengambilan".format(tanggal))
            validasi=input("Apakah sudah benar? (y/n) : ")
            if validasi=='y':
                os.system("cls")
                stage+=1
            else:
                os.system("cls")
                print("Tanggal gagal dimasukkan")
        else:
            os.system("cls")
            print("Tanggal tidak valid")
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

def add_data_gadget_return_history(id_pengembali,gadget,gadget_borrow_history,gadget_return_history):
    #membuat list gadget apa saja yang pernah dipinjam user
    os.system("cls")
    list_gadget_user_all=[]
    for j in range(len(gadget_borrow_history)):
        list_dummy=[]
        if gadget_borrow_history[j][1]==id_pengembali:
            added=False
            for i in range(len(list_gadget_user_all)):
                if gadget_borrow_history[j][2]==list_gadget_user_all[i][0]:
                    list_gadget_user_all[i][2]+=gadget_borrow_history[j][4]
                    added=True
            if not added:
                list_dummy.append(gadget_borrow_history[j][2])
                #Tambah Nama Gadget
                found=False
                for jj in range(len(gadget)):
                    if gadget[jj][0]==gadget_borrow_history[j][2]:
                        list_dummy.append(gadget[jj][1])
                        found=True
                        break
                if not found:
                    for jj in range(len(gadget_return_history)):
                        if gadget_return_history[jj][2]==gadget_borrow_history[j][2]:
                            list_dummy.append(gadget_return_history[jj][5])
                            break
                list_dummy.append(gadget_borrow_history[j][4])
                list_gadget_user_all.append(list_dummy)

    #Jika User belum pernah meminjam apapun
    if list_gadget_user_all==[]:
        print("Tidak ada gadget yang dapat dikembalikan")
        return

    #Mengecek Gadget Apa saja yang sudah dikembalikan
    for j in range(len(gadget_return_history)):
        if gadget_return_history[j][1]==id_pengembali:
            for jj in range(len(list_gadget_user_all)):
                if gadget_return_history[j][2]==list_gadget_user_all[jj][0]:
                    list_gadget_user_all[jj][2]-=gadget_return_history[j][4]

    #Menghapus Gadget yang sudah dikembalikan sepenuhnya

    n=0
    for j in range(len(list_gadget_user_all)):
       i=j-n
       if list_gadget_user_all[i][2]==0:
           del list_gadget_user_all[i]
           n+=1

    #Mencetak Gadget apa saja yang masih dipinjam user tersebut
    print(f"{'NO':<5} {'ID':<5} {'Nama Gadget':<30} {'Jumlah':<10}")
    for j in range(len(list_gadget_user_all)):
        print("{:<5} {:<5} {:<30} {:<10}".format(j+1,list_gadget_user_all[j][0],list_gadget_user_all[j][1],list_gadget_user_all[j][2]))
    print("")
    #Menanyakan User Gadget mana yang akan dikembalikan
    id_gadget_yang_akan_dikembalikan=input("Masukkan ID Gadget yang akan dikembalikan : ")
    found=False
    for j in range(len(list_gadget_user_all)):
        if id_gadget_yang_akan_dikembalikan==list_gadget_user_all[j][0]:
            jumlah_yang_akan_dikembalikan=int(input("Masukkan Banyak Gadget yang akan dikembalikan : "))
            if jumlah_yang_akan_dikembalikan>list_gadget_user_all[j][2]:
                print("Jumlah Gadget yang akan dikembalikan melebihi jumlah gadget yang dipinjam")
            else:
                nama_gadget_yang_akan_dikembalikan=list_gadget_user_all[j][1]
                tanggal=input("Masukkan tanggal pengembalian : ")
                while not validasi_tanggal(tanggal):
                    os.system("cls")
                    print("Tanggal tidak valid")
                    tanggal=input("Masukkan tanggal pengembalian : ")
                found=True
    
    #Jika Input ID salah
    if not found:
        return
    os.system("cls")
    #Validasi Pengembalian
    print("ID Gadget            : ",id_gadget_yang_akan_dikembalikan)
    print("Nama Gadget          : ",nama_gadget_yang_akan_dikembalikan)
    print("Jumlah               : ",jumlah_yang_akan_dikembalikan)
    print("Tanggal Pengembalian : ",tanggal)
    print("Anda akan mengembalikan Gagdet sesuai data tersebut")
    verivikasi_akhir=input("Apakah sudah benar? (y/n) : ")
    if verivikasi_akhir=='y':
        #menambah jumlah gadget di csv gadget
        new_gadget=True
        for j in range(len(gadget)): #jika gadget sudah ada, tinggal mengubah jumlah
            if gadget[j][0]==id_gadget_yang_akan_dikembalikan:
                gadget[j][3]+=jumlah_yang_akan_dikembalikan
                new_gadget=False
        if new_gadget: #kalau gadget baru, maka akan dibuat baris gadget baru
            list_dummy=[]
            list_dummy.append(id_gadget_yang_akan_dikembalikan)
            list_dummy.append(nama_gadget_yang_akan_dikembalikan)
            list_dummy.append("dikembalikan setelah dihapus admin")
            list_dummy.append(jumlah_yang_akan_dikembalikan)
            list_dummy.append("S")
            list_dummy.append(0)
            gadget.append(list_dummy)
        #menambah return history
        list_dummy=[]
        list_dummy.append(len(gadget_return_history))
        list_dummy.append(id_pengembali)
        list_dummy.append(id_gadget_yang_akan_dikembalikan)
        list_dummy.append(tanggal)
        list_dummy.append(jumlah_yang_akan_dikembalikan)
        list_dummy.append(nama_gadget_yang_akan_dikembalikan)
        gadget_return_history.append(list_dummy)
        os.system("cls")

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

def delete_consumable(id_consumable_yang_akan_dihapus,consumable):
    os.system("cls")
    baris_consumable=0
    for j in range(len(consumable)):
        if id_consumable_yang_akan_dihapus==consumable[j][0]:
            baris_consumable=j
    if baris_consumable==0:
        print("Tidak ada item dengan ID tersebut")
    else:
        print("ID Consumable    : ",consumable[baris_consumable][0])
        print("Nama Consumable  : ",consumable[baris_consumable][1])
        print("Deskripsi        : ",consumable[baris_consumable][2])
        print("Jumlah           : ",consumable[baris_consumable][3])
        print("Rarity           : ",consumable[baris_consumable][4])
        print("")
        validasi=input("Apakah Anda yakin akan menghapus consumable tersebut? (y/n) : ")
        if validasi=='y':
            del consumable[baris_consumable]
            return consumable
        else:
            return consumable

def ubah_jumlah_gadget(id_item_yang_akan_diubah,gadget):
    os.system("cls")
    baris_gadget=0
    for j in range(len(gadget)):
        if id_item_yang_akan_diubah==gadget[j][0]:
            baris_gadget=j
    if baris_gadget==0:
        print("Tidak ada item dengan ID tersebut!")
    else:
        jumlah = int(input("Masukkan Jumlah: "))
        if jumlah < 0:
            if (jumlah * (-1)) > gadget[baris_gadget][3]:
                print(jumlah, gadget[baris_gadget][1], "gagal dibuang karena stok kurang. Stok sekarang:", gadget[baris_gadget][3], "(<",jumlah,")")
            else:
                gadget[baris_gadget][3] = gadget[baris_gadget][3] + jumlah
                print(jumlah, gadget[baris_gadget][1], "berhasil dibuang. Stok sekarang:", gadget[baris_gadget][3])
        else:
            gadget[baris_gadget][3] = gadget[baris_gadget][3] + jumlah
            print(jumlah, gadget[baris_gadget][1], "berhasil ditambahkan. Stok sekarang:", gadget[baris_gadget][3])

def ubah_jumlah_consumable(id_item_yang_akan_diubah,consumable):
    os.system("cls")
    baris_consumable=0
    for j in range(len(consumable)):
        if id_item_yang_akan_diubah==consumable[j][0]:
            baris_consumable=j
    if baris_consumable==0:
        print("Tidak ada item dengan ID tersebut!")
    else:
        jumlah = int(input("Masukkan Jumlah: "))
        if jumlah < 0:
            if (jumlah * (-1)) > consumable[baris_consumable][3]:
                print(jumlah, consumable[baris_consumable][1], "gagal dibuang karena stok kurang. Stok sekarang:", consumable[baris_consumable][3], "(<",jumlah,")")
            else:
                consumable[baris_consumable][3] = consumable[baris_consumable][3] + jumlah
                print(jumlah, consumable[baris_consumable][1], "berhasil dibuang. Stok sekarang:", consumable[baris_consumable][3])
        else:
            consumable[baris_consumable][3] = consumable[baris_consumable][3] + jumlah
            print(jumlah, consumable[baris_consumable][1], "berhasil ditambahkan. Stok sekarang:", consumable[baris_consumable][3])

def gacha(id_user,consumable,consumable_history):
    #Membuat list apa saja yang pernah di ambil user
    list_consumable_user_all=[]
    for j in range(len(consumable_history)):
        list_dummy=[]
        if consumable_history[j][1]==id_user:
            added=False
            for i in range(len(list_consumable_user_all)):
                if consumable_history[j][2]==list_consumable_user_all[i][0]:
                    list_consumable_user_all[i][2]+=consumable_history[j][4]
                    added=True
            if not added:
                list_dummy.append(consumable_history[j][2])
                for jj in range(len(consumable)):
                    if consumable[jj][0]==consumable_history[j][2]:
                        list_dummy.append(consumable[jj][1])
                        baris_benda=jj
                list_dummy.append(consumable_history[j][4])
                list_dummy.append(consumable[baris_benda][4])
                list_consumable_user_all.append(list_dummy)


    #Menanyakan apa saja yang mau digunakan untuk gacha
    list_gacha=[]
    list_sementara=[]
    list_dummy=[]
    lagi=True
    while lagi:
        #Mencetak Consumable apa saja yang diambil user tersebut
        print(f"{'NO':<5} {'ID':<5} {'Nama Consumable':<30} {'Jumlah':<10} {'Rarity':<10}")
        for j in range(len(list_consumable_user_all)):
            print("{:<5} {:<5} {:<30} {:<10} {:<10}".format(j+1,list_consumable_user_all[j][0],list_consumable_user_all[j][1],list_consumable_user_all[j][2],list_consumable_user_all[j][3]))
        id_consumable_yang_akan_digacha=input("Masukkan ID Consumable yang akan digacha : ")
        found=False
        for j in range(len(list_consumable_user_all)):
            if id_consumable_yang_akan_digacha==list_consumable_user_all[j][0]:
                found=True
                jumlah_yang_akan_digacha=int(input("Masukkan Banyak consumable yang akan digacha : "))
                if jumlah_yang_akan_digacha>list_consumable_user_all[j][2]:
                    print("Jumlah consumable yang akan digacha melebihi jumlah consumable yang dimiliki")
                else:
                    list_consumable_user_all[j][2]-=jumlah_yang_akan_digacha
                    nama_consumable_yang_akan_digacha=list_consumable_user_all[j][1]
                    rarity=list_consumable_user_all[j][3]
                    tanggal="gacha"
                    list_dummy.append(id_consumable_yang_akan_digacha)
                    list_dummy.append(nama_consumable_yang_akan_digacha)
                    list_dummy.append(jumlah_yang_akan_digacha)
                    list_dummy.append(rarity)
                    list_gacha.append(list_dummy)
                    list_dummy=[]
                    list_dummy.append(len(consumable_history))
                    list_dummy.append(id_user)
                    list_dummy.append(id_consumable_yang_akan_digacha)
                    list_dummy.append(tanggal)
                    list_dummy.append(jumlah_yang_akan_digacha*-1)
                    list_sementara.append(list_dummy)
                    list_dummy=[]
        if not found:
            again=input("Consumabale tidak terdaftar, apakah anda ingin coba lagi? (y/n) : ")
            if again!='y':
                os.system("cls")
                lagi=False
            else:
                os.system("cls")
        else:
            again=input("Apakah Anda akan menambahkan consumable lain? (y/n) : ")
            if again!='y':
                os.system("cls")
                lagi=False
            else:
                os.system("cls")
    if list_gacha==[]:
        print("Tidak ada consumable yang akan di gacha")
        time.sleep(1)
        return
    else:
        print(f"{'NO':<5} {'ID':<5} {'Nama Consumable':<30} {'Jumlah':<10} {'Rarity':<10}")
        for j in range(len(list_gacha)):
            print("{:<5} {:<5} {:<30} {:<10} {:<10}".format(j+1,list_gacha[j][0],list_gacha[j][1],list_gacha[j][2],list_gacha[j][3]))
        validasi=input("Apakah Anda akan menggacha consumable tersebut? (y/n) : " )
        if validasi=='y':
            #Proses Gacha
            print("Sedang Menggacha")
            time.sleep(3)
            os.system("cls")
            
            #Mengenerate sebuah angka dari jumlah dan rarity yang digacha
            total=0
            total_item=0
            for j in range(len(list_gacha)):
                if list_gacha[j][3]=='C':
                    total+=list_gacha[j][2]*1
                    total_item+=list_gacha[j][2]
                elif list_gacha[j][3]=='B':
                    total+=list_gacha[j][2]*2
                    total_item+=list_gacha[j][2]
                elif list_gacha[j][3]=='A':
                    total+=list_gacha[j][2]*3
                    total_item+=list_gacha[j][2]
                else:
                    total+=list_gacha[j][2]*4
                    total_item+=list_gacha[j][2]
            #Rata-rata rarity
            angka_rarity=round(total/total_item)

            #Kesempatan menaikan rarity
            chance=time.time()
            if chance%100<70:
                chance=0
            elif chance%100<90:
                chance=1
            elif chance%100<99:
                chance=2
            else:
                chance=3
            
            #hasil rarity
            angka_rarity+=chance
            if angka_rarity==1:
                rarity='C'
            elif angka_rarity==2:
                rarity='B'
            elif angka_rarity==3:
                rarity='A'
            else:
                rarity='S'
            #Jumlah Item
            jumlah_item=round(total_item/len(list_gacha))
            if jumlah_item<=0:
                jumlah_item=1
            
            #list item yang dapat digacha
            list_gachaable=[]
            list_dummy=[]
            for j in range(len(consumable)):
                if consumable[j][4]==rarity:
                    list_dummy.append(consumable[j][0])
                    list_dummy.append(consumable[j][1])
                    list_gachaable.append(list_dummy)
                    list_dummy=[]
            
            #hasil gachanya
            angka_gacha=total%len(list_gachaable)
            list_dummy=[]
            list_dummy.append(len(consumable_history))
            list_dummy.append(id_user)
            list_dummy.append(list_gachaable[angka_gacha][0])
            list_dummy.append('gacha')
            list_dummy.append(jumlah_item)

            #memperbaharui consumable history
            for j in range(len(list_sementara)):
                consumable_history.append(list_sementara[j])
            consumable_history.append(list_dummy)
            print("Selamat, Anda Mendapatkan {} {} dengan rarity {}".format(jumlah_item,list_gachaable[angka_gacha][1],rarity))
            time.sleep(3)
        else:
            return
        

#Contoh Penggunaan
'''
data=read_csv("clone.csv")
add_data(data)
write_csv(data,"clone.csv")
'''