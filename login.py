from read_csv import read_user

def login():
    user = read_user("user.csv","csv_datas")
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    valid = False
    for i in range(len(user)):
            if (user[i][1]) == username and (user[i][4]) == password:
                valid = True
                break
    if valid:
        print("Halo",username,"! Selamat datang di Kantong Ajaib")
    else:
        print("username dan password tidak cocok atau akunmu belum terdaftar")
login()