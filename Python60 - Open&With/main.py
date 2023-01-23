## read external file

print(3*"=", "Read file txt", 3*"=")
file = open("d:\python\PythonDasar\Python60 - Open&With\data.txt",mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

## read all file
print(file.read())

## read by line
# print(file.readline(), end="") # read first line
# print(file.readline(), end="") # read second line

## read all line as list
# print(file.readlines())

print(f"is the file closed? : {file.closed}")
file.close()
print(f"is the file closed? : {file.closed}")

## one of the way to open file in python

print("\n",3*"=", "Read file txt with 'with'", 3*"=")

with open("d:\python\PythonDasar\Python60 - Open&With\data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
print(f"is the file closed? : {file.closed}")

