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
from login import login
from caritahun import cari_tahun
from see_history import see_gadget_return_history,see_consumable_history,see_gadget_borrow_history
from interface import *
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
valid=False
while not valid:
    valid,curret_id,curret_role=login(user)

while valid:
    pilihan=input("Masukkan Pilihan Menu: ")

    #Masukkan Fungsi-Fungsi Yang Sudah dibuat disini (F01-F17)
    #F01 - Register
    if pilihan=='register':
        if curret_role=='admin':
            add_data_user(user)
        else:
            print("Fungsi Hanya diperbolehkan untuk Admin")
    #F02 - Login
        #Sudah di atas
    #F03 - Pencarian Gadget Berdasarkan Rarity
    if pilihan == "carirarity":
        rarity=input("Masukkan rarity yang akan dicari: ")
        if rarity=='S' or rarity=='A' or rarity=='B' or rarity=='C':
            found=False
            for j in range(len(gadget)):
                if rarity==gadget[j][4]:
                    found=True
                    print("Nama Gadget      : ",gadget[j][1])
                    print("Deskripsi        : ",gadget[j][2])
                    print("Jumlah           : ",gadget[j][3])
                    print("Rarity           : ",gadget[j][4])
                    print("Tahun Ditemukan  : ",gadget[j][5])
                    print("")
            if not found:
                print("Tidak ada gadget dengan rarity tersebut")
        else:
            print("Rarity tidak valid")
    #F04 - Pencarian Gadget Berdasarkan Tahun
    if pilihan=='caritahun':
        cari_tahun(gadget)
    #F05 - Menambah Item
    if pilihan == "tambahitem":
        if curret_role=='admin':
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
                    if consumable[i][0] == id_item:
                        cek += 1
                if cek > 0:
                    print("Gagal menambahkan item karena ID sudah ada.")
                else: #cek == 0 atau id_item belum ada
                    add_data_consumable(id_item,consumable)

            else:
                print("Gagal menambahkan item karena ID tidak valid")
        else:
            print("Fungsi Hanya diperbolehkan untuk Admin")
    #F06 - Menghapus Item
    if pilihan=='hapusitem':
        if curret_role=='admin':
            id_item_yang_akan_dihapus=input("Masukkan ID item yang akan dihapus : ")
            if id_item_yang_akan_dihapus[0]=='G':
                delete_gadget(id_item_yang_akan_dihapus,gadget)
            elif id_item_yang_akan_dihapus[0]=='C':
                delete_consumable(id_item_yang_akan_dihapus,consumable)
            else:
                print("ID tidak cocok")
        else:
            print("Fungsi Hanya diperbolehkan untuk Admin")
    #F07 - Mengubah jumlah pada inventory
    if pilihan == "ubahjumlah":
        if curret_role=='admin':
            id_item_yang_akan_diubah = input("Masukan ID: ")
            if id_item_yang_akan_diubah[0]=='G':
                ubah_jumlah_gadget(id_item_yang_akan_diubah, gadget)
            elif id_item_yang_akan_diubah[0]=='C':
                ubah_jumlah_consumable(id_item_yang_akan_diubah, consumable)
            else:
                print("Tidak ada item dengan ID tersebut!")
        else:
            print("Fungsi Hanya diperbolehkan untuk Admin")
    #F08 - Meminjam Gadget
    if pilihan=='pinjam':
        if curret_role=='user':
            add_data_gadget_borrow_history(curret_id,gadget,gadget_borrow_history)
        else:
            print("Fungsi Hanya diperbolehkan untuk User")
    #F09 - Mengembalikan Gadget
    if pilihan=='kembalikan':
        if curret_role=='user':
            add_data_gadget_return_history(curret_id,gadget,gadget_borrow_history,gadget_return_history)
        else:
            print("Fungsi Hanya diperbolehkan untuk User")
    #F10 - Meminta Consumable
    if pilihan=='minta':
        if curret_role=='user':
            add_data_consumable_history(curret_id,consumable,consumable_history)
        else:
            print("Fungsi Hanya diperbolehkan untuk user")
    #F11 - Melihat Riwayat Peminjaman Gadget
    if pilihan=='riwayatpinjam':
        if curret_role=='admin':
            see_gadget_borrow_history(user,gadget,gadget_borrow_history)
    #F12 - Melihat Riwayat Pengembalian Gadget
    if pilihan=='riwayatkembali':
        if curret_role=='admin':
            see_gadget_return_history(user,gadget,gadget_return_history)
        else:
            print("Fungsi Hanya diperbolehkan untuk Admin")
    #F13 - Melihat Riwayat Pengambilan Consumable
    if pilihan=='riwayatambil':
        if curret_role=='admin':
            see_consumable_history(user,consumable,consumable_history)
        else:
            print("Fungsi Hanya diperbolehkan untuk Admin")
    #F14 - Load Data
        #Sudah pada baigan awal bersama dengan argparse
    #F15 - Save Data
    if pilihan=='save':
        os.system("cls")
        path=input("Masukkan Folder tempat file akan di save: ")
        save(path,user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history)
        r=50
        for i in range (r):
            progressBar(i, r)
            time.sleep(.02)
        time.sleep(1.5)
        data=load(path)
        loaded,user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history=data
    #F16 - Help
    if pilihan == 'help':
        print("================== HELP =================="
              "\nregister              - untuk melakukan registrasi user baru"
              "\nlogin                 - untuk melakukan login ke dalam sistem"
              "\ncarirarity            - untuk mencari gadget dengan rarity tertentu"
              "\ncaritahun             - untuk mencari gadget berdasarkan tahun ditemukan"
              )
        if curret_role=='admin':
            print("tambahitem          - untuk menambahkan item ke dalam inventori"
                  "\nhapusitem         - untuk menghapus suatu item pada database"
                  "\nubahjumlah        - untuk mengubah jumlah gadget dan consumable dalam sistem"
                  "\nriwayatkembali    - untuk melihat riwayat pengembalian gadget"
                  "\nriwayatambil      - untuk melihat riwayat pengambilan consumable"
                    )
        else:#curret_role=='user'
            print("pinjam               - untuk melakukan peminjaman gadget"
                  "\nkembalikan          - untuk mengembalikan gadget"
                  "\nminta               - untuk meminta consumable yang tersedia"
                    )
        print("save                   - untuk melakukan penyimpanan data"
              "\nhelp                  - untuk panduan penggunaan penggunaan sistem"
              "\nexit                  - untuk keluar dari aplikasi"
                )

    #F17 - Exit
    if pilihan == 'exit':
        pil = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        if pil == "y" or pil == "Y":
            path = input("Masukkan Folder tempat file akan di save: ")
            save(path, user, gadget, consumable, consumable_history, gadget_borrow_history, gadget_return_history)
        break
    #FB01 - Hashing
        #Done pada hashing.py
    #FB02 - Mengembalikan Gadget Secara Parsial
        #Done
    #FB03 - Gacha
    if pilihan=='gacha':
        #Validasi User
        #Sementara id digenerate otomatis. Nantinya current id
        id=1
        gacha(id,consumable,consumable_history)