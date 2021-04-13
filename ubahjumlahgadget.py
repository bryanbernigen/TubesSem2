from read_csv import load
from add_data import *
from write_csv import save
import argparse
import os,time

from read_csv import *
data=load("csv_datas")
loaded,user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history=data

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

id_item_yang_akan_diubah=input("Masukan ID: ")
ubah_jumlah_gadget(id_item_yang_akan_diubah, gadget)