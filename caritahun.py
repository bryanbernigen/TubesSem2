import os

def cari_tahun(gadget):
        os.system("cls")
        tahun=int(input("Masukkan Tahun      : "))
        kategori=input("Masukkan Kategori   : ")
        found=False
        if kategori=='>':
            for j in range(1,len(gadget)):
                if tahun<gadget[j][5]:
                    found=True
                    print("Nama Gadget      : ",gadget[j][1])
                    print("Deskripsi        : ",gadget[j][2])
                    print("Jumlah           : ",gadget[j][3])
                    print("Rarity           : ",gadget[j][4])
                    print("Tahun Ditemukan  : ",gadget[j][5])
                    print("")
        elif kategori=='>=':
            for j in range(1,len(gadget)):
                if tahun <= gadget[j][5]:
                    found=True
                    print("Nama Gadget      : ",gadget[j][1])
                    print("Deskripsi        : ",gadget[j][2])
                    print("Jumlah           : ",gadget[j][3])
                    print("Rarity           : ",gadget[j][4])
                    print("Tahun Ditemukan  : ",gadget[j][5])
                    print("")
        elif kategori=='=':
            for j in range(1,len(gadget)):
                if tahun == gadget[j][5]:
                    found=True
                    print("Nama Gadget      : ",gadget[j][1])
                    print("Deskripsi        : ",gadget[j][2])
                    print("Jumlah           : ",gadget[j][3])
                    print("Rarity           : ",gadget[j][4])
                    print("Tahun Ditemukan  : ",gadget[j][5])
                    print("")
        elif kategori=='<':
            for j in range(1,len(gadget)):
                if tahun > gadget[j][5]:
                    found=True
                    print("Nama Gadget      : ",gadget[j][1])
                    print("Deskripsi        : ",gadget[j][2])
                    print("Jumlah           : ",gadget[j][3])
                    print("Rarity           : ",gadget[j][4])
                    print("Tahun Ditemukan  : ",gadget[j][5])
                    print("")
        elif kategori=='<=':
            for j in range(1,len(gadget)):
                if tahun >= gadget[j][5]:
                    found=True
                    print("Nama Gadget      : ",gadget[j][1])
                    print("Deskripsi        : ",gadget[j][2])
                    print("Jumlah           : ",gadget[j][3])
                    print("Rarity           : ",gadget[j][4])
                    print("Tahun Ditemukan  : ",gadget[j][5])
                    print("")
        else:
            print("Kategori tidak Valid")
        
        if not found:
            print("Tidak ada gadget yang sesuai")