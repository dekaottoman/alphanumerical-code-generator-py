import random

def character(no):
    alphanum = "ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwxyz1234567890"
    return alphanum[no]

def gen_string():
    random.seed()
    code = ""
    i = 0
    while(i<16):
        code += character(random.randint(0,60))
        i += 1
    return code

print(gen_string())
