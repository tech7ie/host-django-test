import random
import string

#тут просто генерируется строка для code
def generateCode(length=8):
    characters = string.ascii_letters + (string.digits*3) + ('-_'*8)
    result = ''.join(random.choice(characters) for _ in range(length))
    return result
