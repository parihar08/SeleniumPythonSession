import string
import random


def random_generator(size=8, chars=string.ascii.lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size) )