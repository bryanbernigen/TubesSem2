#READ ME
'''
Jika data pada kolom terakhir mengandung "," maka ubahlah inisialisasi jumlah data pada Menghitung Jumlah Baris menjadi 0
Untuk mengubah bentuk data dalam sebuah kolom (string -> integer) silahkan edit pada bagian Konversi Bentuk dalam array
'''

import os

'''
def read_csv(nama_file):
    #Membuka File CSV
    f = open("csv_datas/{}".format(nama_file),"r")
    raw_lines = f.readlines()
    raw_lines_2=[raw_line.replace("\n","") for raw_line in raw_lines]
    lines=[raw_line.replace("\n","") for raw_line in raw_lines_2]
    lines_all_koma=[raw_line.replace("\n",",") for raw_line in raw_lines]
    f.close()


    #Menghitung Jumlah Kolom
    jumlah_kolom=0
    for i in range (len(lines_all_koma[0])):
        if lines_all_koma[0][i]==',':
            jumlah_kolom += 1 


    #Menghitung Jumlah Baris
    jumlah_data = 1 #Mulai dari 1 karena data kolom terakhir baris terakhir tidak ada ,
    for j in range(len(lines_all_koma)):
        for i in range (len(lines_all_koma[j])):
            if lines_all_koma[j][i]==',':
                jumlah_data += 1 
    jumlah_baris=jumlah_data // jumlah_kolom


    #Membuat List dari CSV
    list_panjang = [] #list semua data yang hanya ke kanan saja (1 Dimensi)
    for j in range (len(lines)):
        word=''
        for i in range (len(lines[j])):
            if lines[j][i] == ',' and word != '':
                list_panjang.append(word)
                word = ''
            else:
                word += lines[j][i]
        if word != '':
            list_panjang.append(word)


    #Menginisialisasi Array untuk Matriks
    list_dummy=[]
    data_csv=[]
    for i in range (jumlah_data):
        list_dummy.append(list_panjang[i])
        if (i+1)%jumlah_kolom == 0:
            data_csv.append(list_dummy)
            list_dummy=[]

    #Mengubah Array menjadi Integer(0)
    def conv_to_int (data_csv,baris_ke):
        for j in range (1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=int(data_csv[j][i])

    #Mengubah Array menjadi Bilangan Real (0.0)
    def conv_to_float (data_csv,baris_ke):
        for j in range(1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=float(data_csv[j][i])




    #Konversi Bentuk dalam Array
    #conv_to_int(data_csv,0)


    #HASIL
    return data_csv
'''
def read_user(nama_file,path_ralatif_terhadap_sekarang):
    #Membuka File CSV
    f = open("{}/{}".format(path_ralatif_terhadap_sekarang,nama_file),"r")
    raw_lines = f.readlines()
    raw_lines_2=[raw_line.replace("\n","") for raw_line in raw_lines]
    lines=[raw_line.replace("\n","") for raw_line in raw_lines_2]
    lines_all_koma=[raw_line.replace("\n",",") for raw_line in raw_lines]
    f.close()


    #Menghitung Jumlah Kolom
    jumlah_kolom=0
    for i in range (len(lines_all_koma[0])):
        if lines_all_koma[0][i]==',':
            jumlah_kolom += 1 


    #Menghitung Jumlah Baris
    jumlah_data = 1 #Mulai dari 1 karena data kolom terakhir baris terakhir tidak ada ,
    for j in range(len(lines_all_koma)):
        for i in range (len(lines_all_koma[j])):
            if lines_all_koma[j][i]==',':
                jumlah_data += 1 
    jumlah_baris=jumlah_data // jumlah_kolom


    #Membuat List dari CSV
    list_panjang = [] #list semua data yang hanya ke kanan saja (1 Dimensi)
    for j in range (len(lines)):
        word=''
        for i in range (len(lines[j])):
            if lines[j][i] == ',' and word != '':
                list_panjang.append(word)
                word = ''
            else:
                word += lines[j][i]
        if word != '':
            list_panjang.append(word)


    #Menginisialisasi Array untuk Matriks
    list_dummy=[]
    data_csv=[]
    for i in range (jumlah_data):
        list_dummy.append(list_panjang[i])
        if (i+1)%jumlah_kolom == 0:
            data_csv.append(list_dummy)
            list_dummy=[]

    #Mengubah Array menjadi Integer(0)
    def conv_to_int (data_csv,baris_ke):
        for j in range (1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=int(data_csv[j][i])

    #Mengubah Array menjadi Bilangan Real (0.0)
    '''
    def conv_to_float (data_csv,baris_ke):
        for j in range(1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=float(data_csv[j][i])
    '''



    #Konversi Bentuk dalam Array
    conv_to_int(data_csv,0)
    #conv_to_float(data_csv,2)



    #HASIL
    return data_csv

def read_gadget(nama_file,path_ralatif_terhadap_sekarang):
    #Membuka File CSV
    f = open("{}/{}".format(path_ralatif_terhadap_sekarang,nama_file),"r")
    raw_lines = f.readlines()
    raw_lines_2=[raw_line.replace("\n","") for raw_line in raw_lines]
    lines=[raw_line.replace("\n","") for raw_line in raw_lines_2]
    lines_all_koma=[raw_line.replace("\n",",") for raw_line in raw_lines]
    f.close()


    #Menghitung Jumlah Kolom
    jumlah_kolom=0
    for i in range (len(lines_all_koma[0])):
        if lines_all_koma[0][i]==',':
            jumlah_kolom += 1 


    #Menghitung Jumlah Baris
    jumlah_data = 1 #Mulai dari 1 karena data kolom terakhir baris terakhir tidak ada ,
    for j in range(len(lines_all_koma)):
        for i in range (len(lines_all_koma[j])):
            if lines_all_koma[j][i]==',':
                jumlah_data += 1 
    jumlah_baris=jumlah_data // jumlah_kolom


    #Membuat List dari CSV
    list_panjang = [] #list semua data yang hanya ke kanan saja (1 Dimensi)
    for j in range (len(lines)):
        word=''
        for i in range (len(lines[j])):
            if lines[j][i] == ',' and word != '':
                list_panjang.append(word)
                word = ''
            else:
                word += lines[j][i]
        if word != '':
            list_panjang.append(word)


    #Menginisialisasi Array untuk Matriks
    list_dummy=[]
    data_csv=[]
    for i in range (jumlah_data):
        list_dummy.append(list_panjang[i])
        if (i+1)%jumlah_kolom == 0:
            data_csv.append(list_dummy)
            list_dummy=[]

    #Mengubah Array menjadi Integer(0)
    def conv_to_int (data_csv,baris_ke):
        for j in range (1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=int(data_csv[j][i])

    #Mengubah Array menjadi Bilangan Real (0.0)
    '''
    def conv_to_float (data_csv,baris_ke):
        for j in range(1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=float(data_csv[j][i])
    '''



    #Konversi Bentuk dalam Array
    conv_to_int(data_csv,3)
    conv_to_int(data_csv,5)



    #HASIL
    return data_csv

def read_consumable(nama_file,path_ralatif_terhadap_sekarang):
    #Membuka File CSV
    f = open("{}/{}".format(path_ralatif_terhadap_sekarang,nama_file),"r")
    raw_lines = f.readlines()
    raw_lines_2=[raw_line.replace("\n","") for raw_line in raw_lines]
    lines=[raw_line.replace("\n","") for raw_line in raw_lines_2]
    lines_all_koma=[raw_line.replace("\n",",") for raw_line in raw_lines]
    f.close()


    #Menghitung Jumlah Kolom
    jumlah_kolom=0
    for i in range (len(lines_all_koma[0])):
        if lines_all_koma[0][i]==',':
            jumlah_kolom += 1 


    #Menghitung Jumlah Baris
    jumlah_data = 1 #Mulai dari 1 karena data kolom terakhir baris terakhir tidak ada ,
    for j in range(len(lines_all_koma)):
        for i in range (len(lines_all_koma[j])):
            if lines_all_koma[j][i]==',':
                jumlah_data += 1 
    jumlah_baris=jumlah_data // jumlah_kolom


    #Membuat List dari CSV
    list_panjang = [] #list semua data yang hanya ke kanan saja (1 Dimensi)
    for j in range (len(lines)):
        word=''
        for i in range (len(lines[j])):
            if lines[j][i] == ',' and word != '':
                list_panjang.append(word)
                word = ''
            else:
                word += lines[j][i]
        if word != '':
            list_panjang.append(word)


    #Menginisialisasi Array untuk Matriks
    list_dummy=[]
    data_csv=[]
    for i in range (jumlah_data):
        list_dummy.append(list_panjang[i])
        if (i+1)%jumlah_kolom == 0:
            data_csv.append(list_dummy)
            list_dummy=[]

    #Mengubah Array menjadi Integer(0)
    def conv_to_int (data_csv,baris_ke):
        for j in range (1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=int(data_csv[j][i])

    #Mengubah Array menjadi Bilangan Real (0.0)
    '''    
    def conv_to_float (data_csv,baris_ke):
        for j in range(1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=float(data_csv[j][i])

    '''


    #Konversi Bentuk dalam Array
    conv_to_int(data_csv,3)


    #HASIL
    return data_csv

def read_consumable_history(nama_file,path_ralatif_terhadap_sekarang):
    #Membuka File CSV
    f = open("{}/{}".format(path_ralatif_terhadap_sekarang,nama_file),"r")
    raw_lines = f.readlines()
    raw_lines_2=[raw_line.replace("\n","") for raw_line in raw_lines]
    lines=[raw_line.replace("\n","") for raw_line in raw_lines_2]
    lines_all_koma=[raw_line.replace("\n",",") for raw_line in raw_lines]
    f.close()


    #Menghitung Jumlah Kolom
    jumlah_kolom=0
    for i in range (len(lines_all_koma[0])):
        if lines_all_koma[0][i]==',':
            jumlah_kolom += 1 


    #Menghitung Jumlah Baris
    jumlah_data = 1 #Mulai dari 1 karena data kolom terakhir baris terakhir tidak ada ,
    for j in range(len(lines_all_koma)):
        for i in range (len(lines_all_koma[j])):
            if lines_all_koma[j][i]==',':
                jumlah_data += 1 
    jumlah_baris=jumlah_data // jumlah_kolom


    #Membuat List dari CSV
    list_panjang = [] #list semua data yang hanya ke kanan saja (1 Dimensi)
    for j in range (len(lines)):
        word=''
        for i in range (len(lines[j])):
            if lines[j][i] == ',' and word != '':
                list_panjang.append(word)
                word = ''
            else:
                word += lines[j][i]
        if word != '':
            list_panjang.append(word)


    #Menginisialisasi Array untuk Matriks
    list_dummy=[]
    data_csv=[]
    for i in range (jumlah_data):
        list_dummy.append(list_panjang[i])
        if (i+1)%jumlah_kolom == 0:
            data_csv.append(list_dummy)
            list_dummy=[]

    #Mengubah Array menjadi Integer(0)
    def conv_to_int (data_csv,baris_ke):
        for j in range (1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=int(data_csv[j][i])

    #Mengubah Array menjadi Bilangan Real (0.0)
    '''
    def conv_to_float (data_csv,baris_ke):
        for j in range(1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=float(data_csv[j][i])
    '''



    #Konversi Bentuk dalam Array
    conv_to_int(data_csv,0)
    conv_to_int(data_csv,1)
    conv_to_int(data_csv,4)


    #HASIL
    return data_csv

def read_gadget_borrow_history(nama_file,path_ralatif_terhadap_sekarang):
    #Membuka File CSV
    f = open("csv_datas/{}".format(nama_file),"r")
    raw_lines = f.readlines()
    raw_lines_2=[raw_line.replace("\n","") for raw_line in raw_lines]
    lines=[raw_line.replace("\n","") for raw_line in raw_lines_2]
    lines_all_koma=[raw_line.replace("\n",",") for raw_line in raw_lines]
    f.close()


    #Menghitung Jumlah Kolom
    jumlah_kolom=0
    for i in range (len(lines_all_koma[0])):
        if lines_all_koma[0][i]==',':
            jumlah_kolom += 1 


    #Menghitung Jumlah Baris
    jumlah_data = 1 #Mulai dari 1 karena data kolom terakhir baris terakhir tidak ada ,
    for j in range(len(lines_all_koma)):
        for i in range (len(lines_all_koma[j])):
            if lines_all_koma[j][i]==',':
                jumlah_data += 1 
    jumlah_baris=jumlah_data // jumlah_kolom


    #Membuat List dari CSV
    list_panjang = [] #list semua data yang hanya ke kanan saja (1 Dimensi)
    for j in range (len(lines)):
        word=''
        for i in range (len(lines[j])):
            if lines[j][i] == ',' and word != '':
                list_panjang.append(word)
                word = ''
            else:
                word += lines[j][i]
        if word != '':
            list_panjang.append(word)


    #Menginisialisasi Array untuk Matriks
    list_dummy=[]
    data_csv=[]
    for i in range (jumlah_data):
        list_dummy.append(list_panjang[i])
        if (i+1)%jumlah_kolom == 0:
            data_csv.append(list_dummy)
            list_dummy=[]

    #Mengubah Array menjadi Integer(0)
    def conv_to_int (data_csv,baris_ke):
        for j in range (1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=int(data_csv[j][i])

    #Mengubah Array menjadi Bilangan Real (0.0)
    '''
    def conv_to_float (data_csv,baris_ke):
        for j in range(1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=float(data_csv[j][i])
    '''



    #Konversi Bentuk dalam Array
    conv_to_int(data_csv,0)
    conv_to_int(data_csv,1)
    conv_to_int(data_csv,4)



    #HASIL
    return data_csv

def read_gadget_return_history(nama_file,path_ralatif_terhadap_sekarang):
    #Membuka File CSV
    f = open("{}/{}".format(path_ralatif_terhadap_sekarang,nama_file),"r")
    raw_lines = f.readlines()
    raw_lines_2=[raw_line.replace("\n","") for raw_line in raw_lines]
    lines=[raw_line.replace("\n","") for raw_line in raw_lines_2]
    lines_all_koma=[raw_line.replace("\n",",") for raw_line in raw_lines]
    f.close()


    #Menghitung Jumlah Kolom
    jumlah_kolom=0
    for i in range (len(lines_all_koma[0])):
        if lines_all_koma[0][i]==',':
            jumlah_kolom += 1 


    #Menghitung Jumlah Baris
    jumlah_data = 1 #Mulai dari 1 karena data kolom terakhir baris terakhir tidak ada ,
    for j in range(len(lines_all_koma)):
        for i in range (len(lines_all_koma[j])):
            if lines_all_koma[j][i]==',':
                jumlah_data += 1 
    jumlah_baris=jumlah_data // jumlah_kolom


    #Membuat List dari CSV
    list_panjang = [] #list semua data yang hanya ke kanan saja (1 Dimensi)
    for j in range (len(lines)):
        word=''
        for i in range (len(lines[j])):
            if lines[j][i] == ',' and word != '':
                list_panjang.append(word)
                word = ''
            else:
                word += lines[j][i]
        if word != '':
            list_panjang.append(word)


    #Menginisialisasi Array untuk Matriks
    list_dummy=[]
    data_csv=[]
    for i in range (jumlah_data):
        list_dummy.append(list_panjang[i])
        if (i+1)%jumlah_kolom == 0:
            data_csv.append(list_dummy)
            list_dummy=[]

    #Mengubah Array menjadi Integer(0)
    def conv_to_int (data_csv,baris_ke):
        for j in range (1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=int(data_csv[j][i])

    #Mengubah Array menjadi Bilangan Real (0.0)
    '''
    def conv_to_float (data_csv,baris_ke):
        for j in range(1,jumlah_baris,1):
            for i in range(jumlah_kolom):
                if i==baris_ke :
                    data_csv[j][i]=float(data_csv[j][i])
    '''



    #Konversi Bentuk dalam Array
    conv_to_int(data_csv,0)
    conv_to_int(data_csv,1)
    conv_to_int(data_csv,4)


    #HASIL
    return data_csv

#Cara Pakai ada di dalam fungsi ini
def load(path_relatif_terhadap_sekarang):
    #Cara Pakai:
    '''
    Data=load("path_relatif_terhadap_sekarang")
    Loaded=data[0]  #menandakana data ada atau tidak
    user=data[1]
    gadget=data[2]
    .
    .
    dst
    '''

    current_path=os.getcwd()
    new_path=os.path.join(current_path,path_relatif_terhadap_sekarang)
    global user
    global gadget
    global consumable
    global consumable_history
    global gadget_borrow_history
    global gadget_return_history
    global loaded
    if os.path.exists(new_path):
        user=read_user("user.csv",path_relatif_terhadap_sekarang)
        gadget=read_gadget("gadget.csv",path_relatif_terhadap_sekarang)
        consumable=read_consumable("consumable.csv",path_relatif_terhadap_sekarang)
        consumable_history=read_consumable_history("consumable_history.csv",path_relatif_terhadap_sekarang)
        gadget_borrow_history=read_gadget_borrow_history("gadget_borrow_history.csv",path_relatif_terhadap_sekarang)
        gadget_return_history=read_gadget_return_history("gadget_return_history.csv",path_relatif_terhadap_sekarang)
        loaded = True
        return loaded,user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history
    else:
        print("Tidak ada data")
        loaded = False
        return loaded

#Contoh Penggunaan
'''
a=read_csv("kdrama.csv")
print(a)
'''