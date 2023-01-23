# search on google "python standard library" and hit enter
# to see more collection of python standard library

import datetime

time_data = datetime.datetime.now()
print(f" datetime now : {time_data}")
print(f" year : {time_data.year}") 
print(f" year : {time_data.strftime('%A')}") 

from collections import Counter
 
data = ["a","b","c","d","b","a","b","d","a","a","c"]
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"total a = {data_count['a']}")
print(f"total b = {data_count['b']}")
print(f"total c = {data_count['c']}")
print(f"total d = {data_count['d']}")

import io 

file = io.open("Python55_StandardLibrary/file_text.txt","r")
print(file.read())
