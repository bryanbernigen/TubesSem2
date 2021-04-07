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


from read_csv import read_csv
from write_csv import write_csv

# Fungsi akan menambah data dengan jumlah kolom yang sama dengan data acuan;
# Fungsi tidak akan memvalidasi input yang sama (Contoh: Username sama tidak apa-apa)
# Jika ingin divalidasi silahkan  edit pada bagian meminta user untuk memasukkan data
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

#Contoh Penggunaan
'''
data=read_csv("clone.csv")
add_data(data)
write_csv(data,"clone.csv")
'''