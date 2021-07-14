import random
head_x = False
body_x = False
counter = 0

def generate_integer():
    global counter         #for using outside variables
    counter = counter + 1
    x = random.randint(1,6)
    print("You have rolled", x)
    return x
