
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