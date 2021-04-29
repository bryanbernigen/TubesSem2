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
        for i in range(len(password_and_username)):
            unique_number+=ord(password_and_username[i])
        return unique_number
    number=unique_number(password_and_username)

    #Menambah Panjang password yang kurang dari 32
    def perpanjang_password(password_and_username, unique_number):
        panjang_kurang=32-len(password_and_username)
        for i in range (panjang_kurang):
            password_and_username+=chr(i*unique_number%256)
        return password_and_username
    password_32 = perpanjang_password(password_and_username,number)

    #Mengubah Password menjadi bentuk hashed(integer) agar 1 arah
    def hashed(password_32):
        hashed=0
        for j in range(len(password_32)):
            hashed+=ord(password_32[j])*(10**(j%8)) 
        return hashed
    hashed_pw=hashed(password_32)

    #jika hasil hashed lebih dari 99999999, maka akan di floor agar menjadi kurang dari 99999999
    def final_stage(hashed_pw):
        while len(str(hashed_pw))>8:
            hashed_pw=hashed_pw//10
        return str(hashed_pw)
    password_final=final_stage(hashed_pw)

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