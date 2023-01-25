import random
import string

def random_string(length:int) -> str:
    total_string = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return total_string