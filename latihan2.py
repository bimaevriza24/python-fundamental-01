
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