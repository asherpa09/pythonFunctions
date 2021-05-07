    # should print a random integer between 0 to 50
import random
def randInt():
    num = int(random.random()*50)
    return num
print(randInt())

    # should print a random integer between 0 to 100
import random
def randInt():
    num = int(random.random()* 100)
    return num
print(randInt())

    # should print a random integer between 50 to 100
import random
def randInt():
    num = int(random.random()*50 + 50)
    return num
print(randInt())

# should print a random integer between 50 and 500
import random
def randInt():
    num = int(random.random()* 450 + 50)
    return num
print(randInt())