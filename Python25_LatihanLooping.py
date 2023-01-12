# latihan perulangan membuat segitia

sisi = 10

# 1. Menggunakan For

# dummy variable
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for")

# 2. Menggunakan While

print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break

print("akhir dari while")

# 3. Hanya ganjil saja

print("awal while")
count = 1
while True:
    
    if (count%2):
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika genap
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir dari while")

# 4. Segitiga

print("awal while")
count = 1
spasi = int(sisi/2)
print(sisi)
while True:
    
    if (count%2):
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika genap
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir dari while")

# 4. Belah ketupat
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
while True:
    if (count%2): 
        spasi += 1
        print(" "*spasi,"+"*count)
        count -= 1
    else:
        count -= 1
    if count == 0:
        break

 