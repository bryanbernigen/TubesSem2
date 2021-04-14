#README
'''
buka file dengan cara mengetikan:
    python main.py "folder_yang_berisi_data_csv"
selama fungsi login belum jadi, cara keluar program adalah control + "c"
'''

#import modul yang dibuat
from read_csv import load
from add_data import *
from write_csv import save
import argparse
import os,time

#inisialisasi Data (Loading Data dari CSV)
parser = argparse.ArgumentParser()
parser.add_argument("folder_location", help="Location of the folder that contains all the data.",nargs='?', const='')
args = parser.parse_args()
if args.folder_location is None:
    print("Tidak ada folder yang dimasukkan")
    exit()
current_path=os.getcwd()
new_path=os.path.join(current_path,args.folder_location)
if os.path.exists(new_path):
    data=load(args.folder_location)
else:
    print("Folder tidak ada")
    exit()
loaded,user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history=data

#Algoritma Program
#User diminta untuk login
current_user=input("Masukkan Username :")
current_password=input("Masukkan Password: ")

#Masukkan Fungsi Login disini
    #Fungsi Login harus bisa mengembalikan current_id (id dari user saat ini di user.csv) 
    #Fungsi Login harus bisa mengembalikan current_role (role dari user saat ini di user.csv) 
    #Fungsi Login Harus bisa mengembalikan login=True atau False (jika sudah hapusa baris dibawah comment ini (yang login=True))
login=True


#Fungsi Total
while login==True:
    os.system("cls")
    pilihan=input("Masukkan Pilihan Menu: ")

    #Masukkan Fungsi-Fungsi Yang Sudah dibuat disini (F01-F17)
    #F01 - Register
    if pilihan=='register':
        #validasi admin
        add_data_user(user)
    #F02 - Login
    #F03 - Pencarian Gadget Berdasarkan Rarity
    if pilihan == "carirarity"

    #F04 - Pencarian Gadget Berdasarkan Tahun

    #F05 - Menambah Item
    if pilihan == "tambahitem":
        #Validasi Admin
        cek = 0 #untuk mengecek apakah id_item sudah ada
        id_item = input("Masukkan ID: ")

        if id_item[0] == 'G':
            for i in range(1,len(gadget)):
                if gadget[i][0] == id_item:
                    cek += 1
            if cek > 0:
                print("Gagal menambahkan item karena ID sudah ada.")
            else: #cek == 0 atau id_item belum ada
                add_data_gadget(id_item,gadget)

        elif id_item[0] == 'C':
            for i in range(1,len(consumable)):
                if gadget[i][0] == id_item:
                    cek += 1
            if cek > 0:
                print("Gagal menambahkan item karena ID sudah ada.")
            else: #cek == 0 atau id_item belum ada
                add_data_consumable(id_item,consumable)

        else:
            print("Gagal menambahkan item karena ID tidak valid")
    #F06 - Menghapus Item
    if pilihan=='hapusitem':
        #Validasi Admin
        id_item_yang_akan_dihapus=input("Masukkan ID item yang akan dihapus : ")
        if id_item_yang_akan_dihapus[0]=='G':
            delete_gadget(id_item_yang_akan_dihapus,gadget)
        elif id_item_yang_akan_dihapus[0]=='C':
            delete_consumable(id_item_yang_akan_dihapus,consumable)
        else:
            print("ID tidak cocok")
    #F07 - Mengubah jumlah pada inventory
    if pilihan == "ubahjumlah":
        #Validasi Admin
        id_item_yang_akan_diubah = input("Masukan ID: ")
        if id_item_yang_akan_diubah[0]=='G':
            ubah_jumlah_gadget(id_item_yang_akan_diubah, gadget)
        elif id_item_yang_akan_diubah[0]=='C':
            ubah_jumlah_consumable(id_item_yang_akan_diubah, consumable)
        else:
            print("Tidak ada item dengan ID tersebut!")
    #F08 - Meminjam Gadget
    if pilihan=='pinjam':
        #Validasi User
        #sementera ID digenerate. Nantinya id merupakan current_id
        id=1
        #tulisan pada fungsi dibawah ini ada yang salah (yang dipinjam gadget yang ditulis malah consumable)
        add_data_gadget_borrow_history(id,gadget,gadget_borrow_history)
    #F09 - Mengembalikan Gadget
    if pilihan=='kembalikan':
        #Validasi User
        #Sementara ID digenerate otomatis. Nantinya merupakan curret_id
        id=1
        add_data_gadget_return_history(id,gadget,gadget_borrow_history,gadget_return_history)
    #F10 - Meminta Consumable
    if pilihan=='minta':
        #Validasi user
        #sementara id digenerate. Nantinya merupakan current_user
        id=1
        add_data_consumable_history(id,consumable,consumable_history)
    #F11 - Melihat Riwayat Peminjaman Gadget
    #F12 - Melihat Riwayat Penembalian Gadget
    #F13 - Melihat Riwayat Pengambilan Consumable
    #F14 - Load Data
    #F15 - Save Data
    if pilihan=='save':
        os.system("cls")
        path=input("Masukkan Folder tempat file akan di save: ")
        print("Saving....")
        save(path,user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history)
        time.sleep(3)
        print("Saved")
        time.sleep(1)
    #F16 - Help
    #F17 - Exit