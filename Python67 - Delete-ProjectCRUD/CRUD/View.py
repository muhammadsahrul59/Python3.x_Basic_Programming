from . import Operation

def delete_console():
    read_console()
    while(True):
        print("Please, select a book number to be delete")
        no_book = int(input("Book number: "))
        data_book = Operation.read(index=no_book)

        if data_book:
            data_break = data_book.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            writer = data_break[2]
            title = data_break[3]
            year = data_break[4][:-1]

    
            # data yang ingin diupdate
            print("\n"+"="*100)
            print("data you want to delete")
            print(f"1. Title\t: {title:.40}")
            print(f"2. Writer\t: {writer:.40}")
            print(f"3. Year\t: {year:4}")
            is_done = input("Are you sure to delete (y/n)? ")
            if is_done == "y" or is_done == "Y":
                Operation.delete(no_book)
                break
        else:
            print("Invalid number, please enter again: ")

    print("Data deleted successfully")

            
def update_console():
    read_console()
    while(True):
        print("Please, select a book number to be update")
        no_book = int(input("Book Number: "))
        data_book = Operation.read(index=no_book)

        if data_book:
            break
        else:
            print("Invalid number, please enter again: ")
    
    data_break = data_book.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    writer = data_break[2]
    title = data_break[3]
    year = data_break[4][:-1]
    
    while(True):
        # data you want to update
        print("\n"+"="*100)
        print("Please, select data a data to be update")
        print(f"1. Title\t: {title:.40}")
        print(f"2. Writer\t: {writer:.40}")
        print(f"3. Year\t: {year:4}")

        # choose mode to update
        user_option = input("Select data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": title = input("title\t: ")
            case "2": writer = input("writer\t: ")
            case "3": 
                while(True):
                    try:
                        year = int(input("Year\t: "))
                        if len(str(year)) == 4:
                            break
                        else:
                            print("year must be a number, please input the year again (yyyy) ")    
                    except:
                        print("year must be a number, please input the year again (yyyy) ")
            case _: print("index don't match")

        print("Your New Data")
        print(f"1. Title\t: {title:.40}")
        print(f"2. Writer\t: {writer:.40}")
        print(f"3. Year\t: {year:4}")
        is_done = input("Is the data correct (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
    
    Operation.update(no_book,pk,data_add,year,title,writer)
            


def create_console():
    print("\n\n"+"="*100)
    print("Please, add book data\n")
    writer = input("Writer\t: ")
    title = input("Title\t: ")
    while(True):
        try:
            year = int(input("Year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("year must be a number, please input the year again (yyyy) ")    
        except:
            print("year must be a number, please input the year again (yyyy) ")

    Operation.create(year,title,writer)
    print("\nThe following is your new data")
    read_console()

def read_console():
    data_file = Operation.read()
    
    index = "No"
    title = "Title"
    writer = "Writer"
    year = "Year"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {title:40} | {writer:40} | {year:5}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        writer = data_break[2]
        title = data_break[3]
        year = data_break[4]
        print(f"{index+1:4} | {title:.40} | {writer:.40} | {year:4}",end="")

    # Footer
    print("="*100+"\n")