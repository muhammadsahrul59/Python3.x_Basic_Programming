import os
import CRUD as CRUD

if __name__ == "__main__":
    operation_system = os.name

    match operation_system:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("WELCOME TO THE PROGRAM")
    print("LIBRARY DATABASE")
    print("======================")

    # check if database exist or not
    CRUD.init_console()

    while(True):
        match operation_system:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("WELCOME TO THE PROGRAM")
        print("LIBRARY DATABASE")
        print("======================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"2. Delete Data\n")

        user_option = input("Input Option: ")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": print("Delete Data")

        is_done = input("Is it done (y/n)?: ")
        if is_done == "y" or is_done == "Y":
            break

    print("Thank you for visiting this project.")