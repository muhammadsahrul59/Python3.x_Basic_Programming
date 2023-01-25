from . import Operation

DB_NAME = "d:/python/PythonDasar/Python65 - Write-ProjectCRUD/data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "title":255*" ",
    "writer":255*" ",
    "year":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database available, init done!")
    except:
        print("Database doesn't exist, please make a new database")
        Operation.create_first_data()
        

