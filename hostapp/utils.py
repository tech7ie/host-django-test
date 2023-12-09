import random
import string

def generateCode(length=8):
    characters = string.ascii_letters + (string.digits*3) + ('-_'*5)
    result = ''.join(random.choice(characters) for _ in range(length))
    return result
