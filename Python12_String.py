data = "ini adalah string"
print(data)
print(type(data))


# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan single quote"
print(data)

# contoh menggabungkan single dan double quote
print('"Halo, apa kabar"') 
print("'Halo, apa kabar'") 

# 2. Menggunakan tanda \

# membuat tanda ` menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup\totong,jauhan")
print("ucup\t\totong, semakin jauh")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed
print("baris pertama.\rbaris kedua.") # carriage return
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return

# 3. String literal atau raw

# hati-hati
print('C:\new folder') #akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD
Website : www.ucup.com/newID
""")
