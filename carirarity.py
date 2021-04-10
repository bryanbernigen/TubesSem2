from main.py import consumbale 

#Pencarian gadget berdasarkan tahun ditemukan 

A=str(input('Masukkan rarity:'))
print ('Hasil Pencarian:')


with open ('consumable.csv','r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = list(csvreader)
    print ('Hasil pencarian:')

for row in rows[5]:
    if row[4]== A :
        print(row[0] + ":" + row[4])
    else:
        print('Masukkan tidak valid ')

