# Operasi Aritmatika

a = 10
b = 3

# operasi tambah (+)
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan (-)
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian (*)
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian (/)
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus (sisa perbagian) %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division (//)
hasil = a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, operational precedence

'''

    1. tanda kurung
    2. exponen **
    3. perkalian,pembagian, f.division,modulus
    4. pertambahan dan pengurangan

'''


x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z, '+', x,'/',y,'-',y,'%',z,'//',x,'=',hasil)