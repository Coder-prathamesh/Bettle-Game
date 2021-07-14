import random
counter = 0

def generate_integer():
    global counter         #for using outside variables
    counter = counter + 1
    x = random.randint(1,6)
    print("You have rolled", x)
    return x

def starting_body():
    #To run until we get Body
    x = 0
    while x != 1:
        x = generate_integer()
    print("Got the Body")    
    
def starting_head_or_legs():
    #To run until we get Head/Legs
    legs = 0
    x = 0
    while x != 2:
        x = generate_integer()
        if (x == 6 and legs < 6):
            print('Legs')
            legs = legs + 1
        elif legs == 6 :
    # if we get legs before head. consider all legs before head
            legs = 999 # Just a number   
    print("Got the Head")
    return legs
