from time import time
from . import Database
from .Util import random_string
import time
import os

def delete(no_book):
    try:
        with open(Database.DB_NAME,'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_book - 1:
                    pass
                else:
                    with open("d:/python/PythonDasar/Python67 - Delete-ProjectCRUD/data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")
    
    os.rename("data_temp.txt",Database.DB_NAME)

def update(no_book,pk,data_add,year,title,writer):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["writer"] = writer + Database.TEMPLATE["writer"][len(writer):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'
    
    data_length = len(data_str)

    try:
        with open(Database.DB_NAME,'r+',encoding="utf-8") as file:
            file.seek(data_length*(no_book-1))
            file.write(data_str)
    except:
        print("update data error")

def create(year,title,writer):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["writer"] = writer + Database.TEMPLATE["writer"][len(writer):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'
    
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data Failed")

def create_first_data():
    writer = input("Writer: ")
    title = input("Title: ")
    while(True):
        try:
            year = int(input("Year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("year must be a number, please input the year again (yyyy)")    
        except:
            print("year must be a number, please input the year again (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["writer"] = writer + Database.TEMPLATE["writer"][len(writer):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["title"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Failed")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            total_book = len(content)
            if "index" in kwargs:
                index_book = kwargs["index"]-1
                if index_book < 0 or index_book > total_book:
                    return False
                else:    
                    return content[index_book]
            else:
                return content
    except:
        print("Read database error")
        return False