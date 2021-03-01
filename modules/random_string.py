import random
import string


def generate_random_string():
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(4))
    return rand_string
