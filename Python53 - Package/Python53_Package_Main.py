import sains.Python53_Package_Math
from sains import Python53_Package_Physics
from sains.Python53_Package_Physics import gaya as force

hasil_tambah = sains.Python53_Package_Math.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}") 

gaya = Python53_Package_Physics.gaya(90,10)
print(f"gaya adalah = {gaya}")

gaya = force(90,10)
print(f"gaya adalah = {gaya}")