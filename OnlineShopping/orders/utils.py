import string
import random

def id_generator(size=6,digits=string.digits):
    return "OR"+"".join(random.choice(digits) for x in range(size))
