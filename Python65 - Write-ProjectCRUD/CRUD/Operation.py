from time import time
from . import Database
from .Util import random_string
import time

def create(year,title,writer):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["writer"] = writer + Database.TEMPLATE["writer"][len(writer):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year) 

    data_str = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'

    try:
        with open(Database.DB_NAME, 'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Failed")

def create_first_data():
    writer = input("Writer: ")
    title = input("Title: ")
    while(True):
        try:
            year = int(input("Year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("year must be a number, please input the year again (yyyy) ")
        except:
            print("year must be a number, please input the year again (yyyy) ")
    
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["writer"] = writer + Database.TEMPLATE["writer"][len(writer):]
    data["title"] = title + Database.TEMPLATE["title"][len(title):]
    data["year"] = str(year) 

    data_str = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'
    print(data_str)
    year = input("Year: ")
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Failed")

def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Read error database")
        return False
    
    