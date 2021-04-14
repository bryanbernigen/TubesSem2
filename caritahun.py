from read_csv import read_gadget

def caritahun(gadget):
    x=input('Masukkan tahun :')
    y=input('Masukkan kategori:')
    print ('hasil pencarian :')

    for i in range (len(gadget)):
        if y== ">=":
            if  gadget[i][5]>= x :
                for j in range (5):
                    print (gadget[0]+":"+gadget[j+1])         
            else:
                print ("Tidak ada gadget yang ditemukan")
        elif y=="=":
            print (gadget[0]+':'+gadget[i])
        elif y== "<=":
            

