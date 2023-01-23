#operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieezzZZzz"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool, harus diubah ke str
print(salam + " is lower = " + str(apakah_lower))
apakah_lower = salam.isupper() # hasilnya bool, harus diubah ke str
print(salam + " is upper = " + str(apakah_lower))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk mengecekhuruf dan angka
# isdecimal() <-- untuk mengecek angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar
# capitalize() = Mengubah Kata yang huruf depannya lowercase jadi uppercase

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya bool

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() 
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust() dan center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(20,'-')
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip('-') # menghilangkan tanda -
print("'"+tengah+"'")