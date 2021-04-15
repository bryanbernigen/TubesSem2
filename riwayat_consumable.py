from read_csv import read_consumable
def riwayat_cosumable():
    data = read_consumable("consumable.csv", "csv_datas")
    history = read_consumable("consumable_history.csv", "csv_datas")
    id = input("ID Pengambilan :")
    pengambil = input("Nama Pengambil :")
    consumable = input("Nama Consumable :")
    tanggal = input("Tanggal Pengambilan :")
    jumlah = input("Jumlah :")
    id_consumable = ""
    for i in range(len(data)):
        if (data[i][1]) == consumable:
            id_consumable = data[i][0]
    for i in range(len(history)):
        if (history[i][1]) == id and (history[i][2]) == id_consumable and (history[i][3]) == tanggal and (history[i][4]) == jumlah:
            print(history[i])

riwayat_cosumable()