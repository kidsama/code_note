import random
import string


def generate_random_password(length=12):
    part_1 = string.ascii_letters
    part_2 = string.digits
    part_3 = string.punctuation
    random_password = ''.join([random.choice(part_1 + part_2 + part_3) for _ in range(length)])
    print(random_password)
    return random_password

generate_random_password()