
#Konstruksi dasar python
#sequential (berurutan)

print('bima evriza surya')
print('jl.medokan semampir')

#IF (PERCABANGAN)

aku_ingin_cepat = True #jadi jika pernyataan sesuai kondisi maka muncul pernyataan kesatu
                        # jika pernyataan tidak sesuai kondisi maka muncul pernyataan kedua
if aku_ingin_cepat: # jika menggunakan if harus ada else

    print('jalan lurus saja')
else: #else bisa disebut opsi kedua
    print('jalan berbelok')

aku_ingin_lambat = True #jadi pernyataan sesuia kondisi maka muncul pernyataan kesatu
                        #jika pernyataan tidak sesuai kondisi maka muncul pernyataaan kedua
if aku_ingin_lambat ==True: #lambang samadengan samadengan berarti ada kondisi  yang dibandingkan
    print('jalan kedepan')
else: #else bisa disebut opsi kedua
    print('jalan kesamping')

#FOR (PERULANGAN)

jumlah_anak = 5
# for itu adalah untuk
for index_anak in range (1, jumlah_anak+1) : #jadi index anak untuk mendefinisikan dari jumlah anak
    print(f'halo anak {index_anak}')         #in range adalah dalam jarak
                                             # f itu adalah fungsi, untuk memasukkan variable ke string

# PERULANGAN SELAIN WHILE HARUS MENGETAHUI BATAS AWAL DAN BATAS AKHIR

#WHILE ( JIKA)
mobil = 5
while mobil > 0 : #Jika pernyataan sesuia dengan kondisi maka program akan tereksekusi  #jika pernyataan tidak sesuai kondisi maka program tidak eksekusi
    print('aku ngeprint satu kali')
    mobil = mobil - 1 # bagaimana untuk jika output bisa berhenti sesuai jumlah variable mobil lima kali?
                    # maka ditambahkan pernyataan proses pengurang supaya output muncul lima kali

rumah = 10
while rumah > 2 :
    print('tiga') #jika jumlah rumah ada 10 , maka rumah lebih dari dua
    rumah = rumah /2 # jadi hasilnya pembagaiannya begini, rumahnya kan ada 10:2 maka hasilnya 5 trs dibagi lagi 5:2 maka hasilnya 2,5 trs dibagi lagi 2,5 : 2 hasilnya 1,5
                    # hasilnya (10:2) (5:2) (2,5:2) = ada 3 proses pembagian ( sampai pembagiannya menyentuh angka 2 , maka proses pembagian telah selesai)
                    # proses output maka terbaca 3 output print

gunung = 20
while gunung > 5 : #
    print('sepuluh')
    gunung = gunung % 2 # (simbol persen % jika di pemprograman adalah sisa hasil dari pembagian/modulus)
                        #maka jika mengguanakan modulus, sisa hasil bagi yang menyentuh angka 5 yang dihitung


#LIST (Array dalah kumpulan data yang ditempatkan dalam satu tempat) / DAFTAR

    #BELAJAR TIPE DATA SKALAR (Tipe data sederhana)
Nama_1 = 'haswin'
Nama_2 = 'vendry'
Nama_3 = 'wika'
Nama_4 = 'yasa'
Nama_5 = 'bima'
print(f'Nama saya adalah :{Nama_1}') # fungsi f berguna untuk merubah varibel pada ke string

#contoh jika tidak fungsi f
print('Nama saya adalah : {Nama_1}')
#jika tidak ada f akan terbaca character

    #BELAJAR TIPE DATA LIST
daftar_baju = [ #list selalu diawali kurung siku []
    'kaos',
    'celana',
    'rok'
]
print(daftar_baju) #pada hasil ini menampilkan daftar baju sebelum ditambahi
daftar_baju.append('topi') #append berguna untuk menambakan semua tipe data
print(daftar_baju) #pada hasil ini menampilkan daftar baju setelah ditambahi
print(daftar_baju[1]) # contoh memanggil data yang tersimpan di list melalui indexing
# Tipe data list indexing dimulai dari 0

# aku  punya baju : ...  celana
print(f'aku punya baju : {daftar_baju[1]}')
print(len(daftar_baju)) # len berguna menghitung jumlah data

isi_dompet = 10,3,15,100,18,29,35
print(len(isi_dompet))

#aku pumya rok dan uang 3
print(f'aku punya {daftar_baju[2]} dan uang {isi_dompet[2]}') #menggunakan kurung siku [] tidak harus didalam list, intinya untuk menggunakan kurung [] tidak harus didalam linkmemilih data indexing yang dipanggil