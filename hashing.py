#READ ME
'''
password akan di hash sesuai dengan kamus pada fungsi
untuk keamanan ektra silahkan ubah urutan pada kamus (alphabetnya tidak terurut)
ukuran kamus juga dapat diubah sesuai kebutuhan
'''

def hashing(password,username):
    
    kamus=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    panjang_kamus=len(kamus)

    #Menanbah username agar username dengan password sama akan memiliki hash yang berbeda
    def add_username(password,username):
        return password+username
    password_and_username=add_username(password,username)

    #Membuat Angka unik dari setiap password dan username
    def unique_number(password_and_username):
        unique_number=0
        pengali=1
        for i in range(len(password)):
            for ii in range (panjang_kamus):
                if password[i]==kamus[ii]:
                    unique_number += ii*pengali
                    pengali*=10
        return unique_number
    unique_number=unique_number(password)

    #Menambah Panjang password yang kurang dari 32
    def perpanjang_password(password_and_username, unique_number):
        panjang_kurang=32-len(password_and_username)
        for i in range (panjang_kurang):
            algorithm_number=(unique_number*i + i)%panjang_kamus 
            password_and_username+=kamus[algorithm_number]
        return password_and_username
    password_32 = perpanjang_password(password_and_username,unique_number)


    #Mengubah Password menjadi Array
    def array_password(password):
        array_password=[]
        for i in range(len(password)):
            array_password.append(password[i])
        return array_password
    array_password=array_password(password_32)

    #Menghashed Password
    def hashed(array_password,unique_number):
        for i in range(len(array_password)):
            for ii in range(panjang_kamus):
                if array_password[i]==kamus[ii]:
                    algorithm_number=(unique_number*i + unique_number*ii + unique_number*i*ii + i*ii + i + ii + unique_number)%panjang_kamus
                    array_password[i]=kamus[algorithm_number]
        return array_password
    password_hashed=hashed(array_password,unique_number)

    #Mengembalikan Hasil Hashed dalam array ke bentuk string
    def password_final(password_hashed):
        password_final=""
        for i in range(len(password_hashed)):
            password_final+=password_hashed[i]
        return password_final
    password_final=password_final(password_hashed)

    return password_final


#Contoh Pengaplikasian
'''
username='admin'
password='aaaaaaaaaaaaaaaaaaaaaaaaaaa'          #Password dummy agar while jalan
while(len(password))>12:                        #mengulang jika password telalu panajang
    password=str(input("Masukkan Password :"))
password_hashed=hashing(password,username)
print(password_hashed)
'''