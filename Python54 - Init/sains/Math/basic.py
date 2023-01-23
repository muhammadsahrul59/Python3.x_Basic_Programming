def plus(*args):
    result = 0

    for data in args:
        result += data

    return result
    
def times(*args):
    result = 1

    for data in args:
        result *= data

    return result