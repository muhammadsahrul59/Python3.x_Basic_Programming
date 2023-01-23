# Exception will happen when the program
# encounters an error runtime

# Example to catch exception

from math import nan

## example
# input_user = int(input("input numbers: "))
# total = nan 

# try:
#     total =10/input_user
# except:
#     print("input cannot be 0 ")

# print(f"total = {total}")

# example in application

while(True):
    numbers = int(input("input the divisor number: "))
    try:
        total = 10/numbers
        print(f"total = {total}")
        is_done = input("continue (y/n)? ")
        if is_done == "n":
            break
    except:
        print("0 divisor, please input again")

print("End of the program 1")

# example application to create file data.txt
try:
    with open("d:/python/PythonDasar/Python62 - Exception&Error&Try&Except/data.txt",'r') as file:
        print(file.read())
except:
     print("file data.txt not found, create new file")
     with open("d:/python/PythonDasar/Python62 - Exception&Error&Try&Except/data.txt",'w',encoding='utf-8') as file:
         file.write("new file")
         
print("End of the program 2")



