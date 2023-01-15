# import

# fungsinya adalah untuk mengambil
# program dari file external .py

# 1. untuk menyambung program dari external
import Python51_ImportStatement_Print
import Python51_ImportStatement_Ucup

# 2. import dengan data
import Python51_ImportStatement_Variabel
import Python51_ImportStatement_Math

# data ada di namespace variable
print(Python51_ImportStatement_Variabel.data)

# 3. import dengan fungsi
import Python51_ImportStatement_Math

hasil = Python51_ImportStatement_Math.tambah(4,5)
print(hasil)