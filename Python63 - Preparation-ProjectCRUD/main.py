import os
import CRUD as CRUD

if __name__ == "__main__":
    operation_system = os.name

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

        print("\n======================\n")

        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")

        print("\n======================\n")

        is_done = input("Is it done (y/n)?)")
        if is_done == "y" or is_done == "Y":
            break

    print("Thank you for visiting this project.")