import os
import time
from interface import *
from hashing import hashing

def login(user):
    global valid
    #Ini Kalo Bisa ditambah sesuatu kaya halo selamat datang, trus gambar doraemon pake garis"
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    password=hashing(password,username)
    valid = False
    for i in range(len(user)):
        if (user[i][1]) == username and (user[i][4]) == password:
            baris_user=i
            valid = True
            break
    if valid:
        global curret_id
        global curret_role
        os.system("cls")
        kantongajaib()
        print("Halo",username,"! Selamat datang di Kantong Ajaib")
        time.sleep(2)
        curret_id=user[baris_user][0]
        curret_role=user[baris_user][5]
        return True,curret_id,curret_role
    else:
        os.system("cls")
        print("username dan password tidak cocok atau akunmu belum terdaftar")
        return False,'',''