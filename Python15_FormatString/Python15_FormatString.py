#format string

# contoh generic
# string
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.5432
format_str = f"desimal = {angka:.3f}"
print(format_str)

# menampilkan leading zero
angka = 2005.5432
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persentase
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"

print(format_persen)

# melakukan operasi aritmatika dalam placeholder
harga = 10000
jumlah = 5

format_str = f"harga total = Rp. {harga*jumlah:,}"
print(format_str)

# format angka lain (binary,octal,hex)forformat_mat_

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)




