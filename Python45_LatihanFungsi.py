'''Latihan Fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# # membuat header program
# os.system("cls")

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user
# LEBAR = int(input("Masukkan nilai lebar: "))
# PANJANG = int(input("Masukkan nilai panjang: "))

# # Program menghitung luas dan keliling
# LUAS = PANJANG*LEBAR    
# KELILING = 2*(PANJANG+LEBAR)

# # tampilkan hasilnya
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''fungsi header'''
    # membuat header program
    os.system("cls")

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    # Mengambil input user
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilaipanjang: "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi lebar'''
    return 2*(panjang+lebar)

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")

# Program Utamanya
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display(f"luas", LUAS)
    display(f"keliling", KELILING)

    isContinue = input("apakah lanjut (y/n): ")
    if isContinue == "n":
        break

print("Program selesai, terima kasih")

