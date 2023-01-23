# __main__ 
# is top level code environment

# __name__ == "__main__" # will hapeen if 
# it is in the main program

## __name__ in main program file
print(f"value __name__ in main.py = '{__name__}'")

## __name__ in external program file
import function

## usage example __main__ 

# declaration
def function_plus(a:int,b:int)->int:
    return a+b

# main function
if __name__ == "__main__":
    number1 = 10
    number2 = 15
    result = function_plus(number1,number2)
    print(f"plus result = {result}")

## import package
import package 


