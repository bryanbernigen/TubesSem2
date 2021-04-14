from read_csv import read_gadget
from add_data import add_data_gadget
from write_csv import save


def carirarity (gadget):
    inputRaririty= str (input(" Masukkan rarity :"))
    print('Hasil pencarian :')
    for i in range (len(gadget)):
        if (gadget[i][4]) == inputRarity :
            return (print (gadget[0] +':'+ gadget[i]))
        else :
            return (print('Data belum tersedia'))



    