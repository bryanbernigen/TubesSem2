#READ ME
'''
---
'''


from read_csv import read_csv

#Fungsi memerlukan 2 input yaitu data yang akan di save dan tempat data tersebut akan di save
#Tempat data tersebut di save harus sudah ada (boleh kosong)
def write_csv(data_yang_akan_di_save,nama_file_yang_di_save):
    data=data_yang_akan_di_save

    #menghitung jumlah kolom dan baris dari data yang di read
    jumlah_baris=len(data)
    jumlah_kolom=len(data[0])
    
    #Mengubah data ke bentuk string
    for j in range(jumlah_baris):
        for i in range (jumlah_kolom):
            data[j][i]=str(data[j][i])
    
    #Mengubah data ke bentuk 1 array panjang (1 Dimensi)
    list_array=[]
    for j in range(jumlah_baris):
        for i in range(jumlah_kolom):
            list_array.append(data[j][i])

    
    #Mengubah data ke bentuk barisan karakter (1 Dimensi)
    var_dummy=""
    for j in range (len(list_array)):
        if j>0:
            if j%jumlah_kolom == 0:
                var_dummy+="\n "
            else:
                var_dummy+=","
        for i in range(len(list_array[j])):
            var_dummy+=list_array[j][i]
    #list_panjang.append(var_dummy)

    f=open("csv_datas/{}".format(nama_file_yang_di_save),"w")
    f.write(var_dummy)


#Contoh Penggunaan
'''
data=read_csv("kdrama.csv")     #membaca data
data[1][2]=10.0                 #mengubah data
write_csv(data,"clone.csv")     #mensave data
'''