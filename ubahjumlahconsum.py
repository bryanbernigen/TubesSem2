from read_csv import load
from add_data import *
from write_csv import save
import argparse
import os,time

from read_csv import *
data=load("csv_datas")
loaded,user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history=data

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

id_item_yang_akan_diubah=input("Masukan ID: ")
ubah_jumlah_consumable(id_item_yang_akan_diubah, consumable)