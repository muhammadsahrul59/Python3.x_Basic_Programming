# Example to make exception

from numbers import Number

def plus(a,b):
    if not isinstance(a,Number) or not isinstance (b,Number):
        raise "input should be a number"
    return a+b

print(plus(5,6))

numbers = 0

# try:
#     total = 10/numbers
# except Exception as error_message:
#     print(error_message)

try:
    total = 10/numbers
except ZeroDivisionError as error_message:
    print(error_message)