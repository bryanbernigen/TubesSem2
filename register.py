
from add_data import add_data_user


def register():
    data = read_user("user.csv", "csv_datas")
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    unik = True
    for i in range(len(data)):
        if (data[i][1]) == username:
            unik = False
            break
    if unik:
        password = input("Masukan password: ")
        alamat = input("Masukan alamat: ")
        role = "user"
        new_data = [id,username, nama, alamat, password,role]

register()