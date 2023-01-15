'''Default Argument'''

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

# contoh 1
def say_hello(nama = "Ganteng"):
    '''fungsi dengan default argument'''
    print(f"Hallo {nama}")

say_hello("Ucup")
say_hello()

# contoh dua

def sapa_dia(nama, pesan = "Apa kabar?"):
    '''fungsi dengan satu input biasa, dan satu default'''
    print(f"hai {nama}, {pesan}")

sapa_dia("Dudung","Hai Ganteeng")
sapa_dia("Otong")

# contoh tiga

def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

# contoh empat

def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))