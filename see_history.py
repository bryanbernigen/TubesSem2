import os

def see_gadget_borrow_history(user,consumable,gadget_borrow_history):
    
    #Membuat array dengan id transaksi, user, item, tanggal (dalam integer)
    list_full=[]
    for j in range(1,len(gadget_borrow_history)):
        if gadget_borrow_history[j][3]!='gacha':
            list_dummy=[]
            list_dummy.append(gadget_borrow_history[j][0])
            for jj in range (len(user)):
                if gadget_borrow_history[j][1]==user[jj][0]:
                    list_dummy.append(user[jj][1])
                    break
            for jj in range(len(consumable)):
                if gadget_borrow_history[j][2]==consumable[jj][0]:
                    list_dummy.append(consumable[jj][1])
                    break
            #membuat tanggal menjadi sebuah integer
            tanggal_int=''
            tanggal_int+=gadget_borrow_history[j][3][6]+gadget_borrow_history[j][3][7]+gadget_borrow_history[j][3][8]+gadget_borrow_history[j][3][9]
            tanggal_int+=gadget_borrow_history[j][3][3]+gadget_borrow_history[j][3][4]
            tanggal_int+=gadget_borrow_history[j][3][0]+gadget_borrow_history[j][3][1]
            tanggal_int=int(tanggal_int)
            list_dummy.append(tanggal_int)
            list_dummy.append(gadget_borrow_history[j][4])
            list_full.append(list_dummy)

    #Mengurutkan List
    list_terurut=[]
    jj=len(list_full)+1
    for j in range(len(list_full)):
        jj-=1
        list_dummy=list_full[j]
        for i in range(1,jj):
            if list_dummy[3]<list_full[i][3]:
                list_dummy,list_full[i]=list_full[i],list_dummy
        list_terurut.append(list_dummy)
    
    #mengembalikan tanggal ke bentuk string
    for j in range(len(list_terurut)):
        list_terurut[j][3]=str(list_terurut[j][3])
        panjang_tanggal=len(list_terurut[j][3])
        while panjang_tanggal<8:
            list_terurut[j][3]='0'+list_terurut[j][3]
            panjang_tanggal=len(list_terurut[j][3])
        tanggal_str=''
        tanggal_str+=list_terurut[j][3][6]+list_terurut[j][3][7]+'/'
        tanggal_str+=list_terurut[j][3][4]+list_terurut[j][3][5]+'/'
        tanggal_str+=list_terurut[j][3][0]+list_terurut[j][3][1]+list_terurut[j][3][2]+list_terurut[j][3][3]
        list_terurut[j][3]=tanggal_str

    #menampilkan data
    awal=0
    akhir=5
    again=True
    while again:
        for j in range(awal,akhir):
            print("ID Pengambilan       : ",list_terurut[j][0])
            print("Nama Pengambil       : ",list_terurut[j][1])
            print("Nama consumable      : ",list_terurut[j][2])
            print("Tanggal Pengambilan  : ",list_terurut[j][3])
            print("Jumlah               : ",list_terurut[j][4]) 
            print("")
        lagi=input("Next Data? (y/n) : ")
        os.system("cls")
        if lagi=='y':
            awal+=5
            akhir+=5
            if akhir>len(list_full):
                akhir=len(list_full)
            if awal>=akhir:
                print("Tidak ada data lagi")
                again=False
        else:
            again=False

def see_gadget_return_history(user,gadget,gadget_return_history):
    
    #Membuat array dengan id transaksi, user, item, tanggal (dalam integer)
    list_full=[]
    for j in range(1,len(gadget_return_history)):
        list_dummy=[]
        list_dummy.append(gadget_return_history[j][0])
        for jj in range (len(user)):
            if gadget_return_history[j][1]==user[jj][0]:
                list_dummy.append(user[jj][1])
                break
        for jj in range(len(gadget)):
            if gadget_return_history[j][2]==gadget[jj][0]:
                list_dummy.append(gadget[jj][1])
                break
        #membuat tanggal menjadi sebuah integer
        tanggal_int=''
        tanggal_int+=gadget_return_history[j][3][6]+gadget_return_history[j][3][7]+gadget_return_history[j][3][8]+gadget_return_history[j][3][9]
        tanggal_int+=gadget_return_history[j][3][3]+gadget_return_history[j][3][4]
        tanggal_int+=gadget_return_history[j][3][0]+gadget_return_history[j][3][1]
        tanggal_int=int(tanggal_int)
        list_dummy.append(tanggal_int)
        list_full.append(list_dummy)

    #Mengurutkan List
    list_terurut=[]
    jj=len(list_full)+1
    for j in range(len(list_full)):
        jj-=1
        list_dummy=list_full[j]
        for i in range(1,jj):
            if list_dummy[3]<list_full[i][3]:
                list_dummy,list_full[i]=list_full[i],list_dummy
        list_terurut.append(list_dummy)
    
    #mengembalikan tanggal ke bentuk string
    for j in range(len(list_terurut)):
        list_terurut[j][3]=str(list_terurut[j][3])
        panjang_tanggal=len(list_terurut[j][3])
        while panjang_tanggal<8:
            list_terurut[j][3]='0'+list_terurut[j][3]
            panjang_tanggal=len(list_terurut[j][3])
        tanggal_str=''
        tanggal_str+=list_terurut[j][3][6]+list_terurut[j][3][7]+'/'
        tanggal_str+=list_terurut[j][3][4]+list_terurut[j][3][5]+'/'
        tanggal_str+=list_terurut[j][3][0]+list_terurut[j][3][1]+list_terurut[j][3][2]+list_terurut[j][3][3]
        list_terurut[j][3]=tanggal_str

    #menampilkan data
    awal=0
    akhir=5
    again=True
    while again:
        for j in range(awal,akhir):
            print("ID Pengambilan       : ",list_terurut[j][0])
            print("Nama Pengambil       : ",list_terurut[j][1])
            print("Nama Gadget          : ",list_terurut[j][2])
            print("Tanggal Pengembalian : ",list_terurut[j][3])
            print("")
        lagi=input("Next Data? (y/n) : ")
        os.system("cls")
        if lagi=='y':
            awal+=5
            akhir+=5
            if akhir>len(list_full):
                akhir=len(list_full)
            if awal>=akhir:
                print("Tidak ada data lagi")
                again=False
        else:
            again=False

def see_consumable_history(user,consumable,consumable_history):
    
    #Membuat array dengan id transaksi, user, item, tanggal (dalam integer)
    list_full=[]
    for j in range(1,len(consumable_history)):
        if consumable_history[j][3]!='gacha':
            list_dummy=[]
            list_dummy.append(consumable_history[j][0])
            for jj in range (len(user)):
                if consumable_history[j][1]==user[jj][0]:
                    list_dummy.append(user[jj][1])
                    break
            for jj in range(len(consumable)):
                if consumable_history[j][2]==consumable[jj][0]:
                    list_dummy.append(consumable[jj][1])
                    break
            #membuat tanggal menjadi sebuah integer
            tanggal_int=''
            tanggal_int+=consumable_history[j][3][6]+consumable_history[j][3][7]+consumable_history[j][3][8]+consumable_history[j][3][9]
            tanggal_int+=consumable_history[j][3][3]+consumable_history[j][3][4]
            tanggal_int+=consumable_history[j][3][0]+consumable_history[j][3][1]
            tanggal_int=int(tanggal_int)
            list_dummy.append(tanggal_int)
            list_dummy.append(consumable_history[j][4])
            list_full.append(list_dummy)

    #Mengurutkan List
    list_terurut=[]
    jj=len(list_full)+1
    for j in range(len(list_full)):
        jj-=1
        list_dummy=list_full[j]
        for i in range(1,jj):
            if list_dummy[3]<list_full[i][3]:
                list_dummy,list_full[i]=list_full[i],list_dummy
        list_terurut.append(list_dummy)
    
    #mengembalikan tanggal ke bentuk string
    for j in range(len(list_terurut)):
        list_terurut[j][3]=str(list_terurut[j][3])
        panjang_tanggal=len(list_terurut[j][3])
        while panjang_tanggal<8:
            list_terurut[j][3]='0'+list_terurut[j][3]
            panjang_tanggal=len(list_terurut[j][3])
        tanggal_str=''
        tanggal_str+=list_terurut[j][3][6]+list_terurut[j][3][7]+'/'
        tanggal_str+=list_terurut[j][3][4]+list_terurut[j][3][5]+'/'
        tanggal_str+=list_terurut[j][3][0]+list_terurut[j][3][1]+list_terurut[j][3][2]+list_terurut[j][3][3]
        list_terurut[j][3]=tanggal_str

    #menampilkan data
    awal=0
    akhir=5
    again=True
    while again:
        for j in range(awal,akhir):
            print("ID Pengambilan       : ",list_terurut[j][0])
            print("Nama Pengambil       : ",list_terurut[j][1])
            print("Nama consumable      : ",list_terurut[j][2])
            print("Tanggal Pengambilan  : ",list_terurut[j][3])
            print("Jumlah               : ",list_terurut[j][4]) 
            print("")
        lagi=input("Next Data? (y/n) : ")
        os.system("cls")
        if lagi=='y':
            awal+=5
            akhir+=5
            if akhir>len(list_full):
                akhir=len(list_full)
            if awal>=akhir:
                print("Tidak ada data lagi")
                again=False
        else:
            again=False


