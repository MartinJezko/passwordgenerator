import random
import string

input("Press Enter to generte random password... ")

def generateRandom():
    a = str(random.randint(0,9))
    b = str(random.randint(0,9))
    c = str(random.randint(0,9))
    d = str(random.randint(0,9))
    e = str(random.randint(0,9))


    w = random.choice(string.ascii_letters)
    x = random.choice(string.ascii_letters)
    y = random.choice(string.ascii_letters)
    z = random.choice(string.ascii_letters)

    print(a+w+b+x+c+y+d+z+e)

generateRandom()
input("Press Enter to continue... ")