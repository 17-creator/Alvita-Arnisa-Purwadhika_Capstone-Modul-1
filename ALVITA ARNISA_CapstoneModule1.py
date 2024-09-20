from operator import index
from unicodedata import category


Data_Barang_Pertanian = (
    {'NamaBarang': 'Nitrea',
     'Jumlahminimum':100,
     'JumlahRestock': 10000
     },
    # {'NamaBarang': 'Dolomit'
     'Jumlahminimum': 500,
     'JumlahRestock': 20000
     },
    {'NamaBarang': 'Benih BISI 18',
     'Jumlahminimum': 20,
     'JumlahRestock': 100
     },
    {'NamaBarang': 'NPK 18-18-18',
     'Jumlahminimum': 100,
     'JumlahRestock': 5000
     },
    {'NamaBarang': 'Megathane',
     'Jumlahminimum': 10,
     'JumlahRestock': 100
     },
    {'NamaBarang': 'SuperStick',
     'Jumlahminimum': 5,
     'JumlahRestock : 50
     },
    {'NamaBarang': 'Liquid Fertilizer',
     'Jumlahminimum': 20,
     'JumlahRestock': 200
     },
    {'NamaBarang': 'Nordox',
     'Jumlahminimum': 30,
     'JumlahRestock': 150
     },
)

cart = []

# menampilkan seluruh data(Menu Read Data)
def Menampilkan_Data_Barang_Pertanian() :
    print('Data Barang Pertanian')
    print('Index\t| Category \t| jumlahminimum\t| Spesification')
    for i in range(len(Data_Barang_Pertanian)) :
        print(f'{i}'.ljust(8),f'|{Data_Barang_Pertanian[i]["category"]}'.ljust(16), f'| {Data_Barang_Pertanian[i]["brand"]}'.ijust(8),f'|{Data_Barang_Pertanian[i]["Spesification"]}')

# menu create data
def MenambahkanDataBarang() :
    Namabarang = input('Masukkan Kategori Barang : ')
    JumlahminimumBarang = int(input('Masukkan Brand Barang : '))
    JumlahRestock = int(input('Masukkan Spesifikasi Barang: ')) 
    Data_Barang_Pertanian.append({
        'NAMABARANG': Namabarang.upper(),
        'JUMLAHMINIMUMBARANG' : JumlahminimumBarang,
        'JUMLAHRESTOCK' : JumlahRestock   
    })
    MenambahkanDataBarang()

# menu delete data
def MenghapusDataBarang() :
    Menampilkan_Data_Barang_Pertanian()
    indexBarang = int(input('Masukkan indext data yang ingin dihapus: '))
    del Data_Barang_Pertanian[indexBarang]
    Menampilkan_Data_Barang_Pertanian()    

# menu update data
def MengubahDataBarang() :
    MenambahkanDataBarang
    while True :
        indexBarang = int(input('Masukkan index pasien yang ingin di bayar: '))
        BrandBarang = int(input('Masukkan brand barang: '))
        if(Jumlahminimum != Data_Barang_Pertanian[indexBarang]['BRANDBARANG']) : # type: ignore
            print('brang salah')
        else :
            cart.append({
                'CATEGORY' : Data_Barang_Pertanian[indexBarang]['BRANDBARANG'],
                'indexBarang' : indexBarang
            })
           print('Isi Cart :')
        print('Category\t| Brand\t| Spesification')
        print(Data_Barang_Pertanian[indexBarang])
    checker = input('Apa ingin memasukkan data yang lain? (Ya/Tidak) = ')
    if(checker == 'tidak') :
        # break

print('Barang Data Reorder:')
print('Category\t| jumlahminimum\t| Spesification\t|')
Restock = Data_Barang_Pertanian[index.Barang]['BRANDBARANG']
while True :
    print('Total Yang Harus Diorder = {}'.format(JumlahBarang))
    JumlahBarang = int(input('Masukkan jumlah barang:'))
    nama = input ('Masukkan nama category :')
    if(JumlahBarang > Restock) :
        Restock = JumlahBarang - Restock
        print('Terima kasih{} \n\nJumlah barang yang harus dibeli : {}'.format(category, JumlahBarang))
        break
    elif (JumlahBarang == JumlahBarang) :
        print('Terima kasih {}' .format(category))
        break
    else: JumlahBarang - JumlahBarang
    print('Maaf dengan jumlah barang{}, Kebutuhan pertanian tidak akan tercukupi{}'. format(namabarang, jumlahbarang)) # type: ignore

# menu utama
while True:
    pilihanMenu = input('''
        Welcome In Our Agriculture Warehouse
    
        List Menu :
        1. Show Data Based On Category
        2. Add Goods Data
        3. Change Goods Warehouse Data
        4. Delete Goods Data
        5. Exit menu
                    
        Masukkan angka Menu yang ingin dijalankan : ''')
    if pilihanMenu == '1' :
        Menampilkan_Data_Barang_Pertanian()
    elif pilihanMenu == '2' :
        MenambahkanDataBarang()
    elif pilihanMenu == '3' :
        MengubahDataBarang()
    elif pilihanMenu == '4' :
        MenghapusDataBarang()
    elif pilihanMenu == '5' :
        print('program berhenti untuk dijalankan')
        break
