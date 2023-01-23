# 1. mode write

# it will create new file if doesn't exist,
# then it will overwrite its contents 

with open("d:/python/PythonDasar/Python61 - WriteExternalFile/data_1.txt",'w',encoding="utf-8") as file:
    file.write("Jhon Jhonny")

with open("d:/python/PythonDasar/Python61 - WriteExternalFile/data_1.txt",'w',encoding="utf-8") as file:
    file.write("Ucup Surucup")

with open("d:/python/PythonDasar/Python61 - WriteExternalFile/data_1.txt",'w',encoding="utf-8") as file:
    file.write("Overwrite")

# 2. mode append

with open("d:/python/PythonDasar/Python61 - WriteExternalFile/data_2.txt",'w',encoding="utf-8") as file:
    file.write("Jhon Jhonny\n")

with open("d:/python/PythonDasar/Python61 - WriteExternalFile/data_2.txt",'a',encoding="utf-8") as file:
    file.write("Ucup Surucup\n")

with open("d:/python/PythonDasar/Python61 - WriteExternalFile/data_2.txt",'a',encoding="utf-8") as file:
    file.write("Add more with append\n")

# 3. mode r+

with open("d:/python/PythonDasar/Python61 - WriteExternalFile/data_3.txt",'w',encoding="utf-8") as file:
    file.write("data third\n")

with open("d:/python/PythonDasar/Python61 - WriteExternalFile/data_3.txt",'r+',encoding="utf-8") as file:
    file.write("line-1\n")
    file.write("line-2\n")
    file.write("line-3\n")

with open("d:/python/PythonDasar/Python61 - WriteExternalFile/data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("d:/python/PythonDasar/Python61 - WriteExternalFile/data_3.txt",'r+',encoding="utf-8") as file:
    file.write("jhon") #overwrite the contents of the text according to the data length