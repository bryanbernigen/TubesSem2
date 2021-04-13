#README
'''
buka file dengan cara mengetikan:
    python main.py "folder_yang_berisi_data_csv"
selama fungsi login belum jadi, cara keluar program adalah control + "c"
'''

#import modul yang dibuat
from read_csv import load
from add_data import add_data_user,add_data_gadget,add_data_consumable
import argparse
import os

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
    pilihan=input("Masukkan Pilihan Menu: ")

    #Masukkan Fungsi-Fungsi Yang Sudah dibuat disini (F01-F17)
    #F01 - Register
    if pilihan=='register':
        add_data_user(user)
    #F02 - Login
    #F03 - Pencarian Gadget Berdasarkan Rarity
    #F04 - Pencarian Gadget Berdasarkan Tahun
    #F05 - Menambah Item
    ''' 
    if pilihan=='tambahitem':
        if current_role=='admin':
            id_item=input("Masukkan ID: ")
            if id_item[0]=='C':
                add_data_consumable(id_item,consumable)
            elif id_item[0]=='G':
                add_data_gadget(id_item,gadget)
    '''
    #F06 - Menghapus Item
    #F07 - Mengubah jumlah pada inventory
    #F08 - Meminjam Gadget
    #F09 - Menegmbalikan Gadget
    #F10 - Meminta Consumable
    #F11 - Melihat Riwayat Peminjaman Gadget
    #F12 - Melihat Riwayat Penembalian Gadget
    #F13 - Melihat Riwayat Pengambilan Consumable
    #F14 - Load Data
    #F15 - Save Data
    #F16 - Help
    #F17 - Exit