# module matematika dengan as / alias

from Python52_Module_Math import tambah as add
from Python52_Module_Math import kali as times
from Python52_Module_Math import pangkat as power



hasil_tambah = add(1,2,3,4,5)
print(f"hasil tambah {hasil_tambah}")


hasil_kali = times(1,2,3,4,5)
print(f"hasil kali {hasil_kali}")

pangkat_3 = power(3)
print(f"hasil pangkat 3 = {pangkat_3(3)}") 