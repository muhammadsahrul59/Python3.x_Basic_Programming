## Global dan Local Scope

nama_global = "otong" # <- ini variabel global

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")

## Variabel Local Scope

def fungsi2():
    nama_local = "Ucup" # <- variabel local scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan

## contoh 1: penggunaan

def say_otong():
    print(f"Hello {nama}")

nama = "Otong"
say_otong()

## contoh 2: merubah variabel global
angka = 0
nama = "Ucup"
def ubah(nilai_baru,nama_baru):
    global angka  #fungsi ini mendapat akses merubah angka
    global nama
    angka = nilai_baru
    nama = nama_baru
print(f"Sebelum {angka,nama}")
ubah(10,"Otong")
print(f"Sesudah {angka,nama}")

## contoh 3:
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)

