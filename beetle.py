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

def mouth_ant_eye(legs):
    # To get mouth, antenna and eye.
    acond,econd,mcond,lcond,total_done = False,False,False,False,False  #Initialize the conditions
    ac,ec,mc,lc = 0,0,0,legs #Initialise the organ counts
    p,q,r,s = False,False,False,False 
    if (legs == 999):
        lcond = True
    while not total_done:
        # Run this loop until we get all the parts
        d  = generate_integer()
        if(d==3 and not acond):
            print('Antenna')
            ac+=1
        elif(d==4 and not econd):
            print('Eyes')
            ec+=1
        elif(d==5 and not mcond):
            print('Mouth')
            mc+=1
        elif(d==6 and not lcond):
            print('Legs')
            lc+=1
        
        if(ac == 2 and not p):
            print("Got all the antennas")
            acond = True
            p = True
        if(ec == 2 and not q):
            print("Got all the eyes")
            econd = True
            q = True
        if(mc == 1 and not r):
            print("Got the mouth")
            mcond = True
            r = True
        if(lc == 6 and not lcond and not s):
            print("Got all the Legs")
            lcond = True
            s = True
            
        if(acond and econd and mcond and lcond):
            print("###---Congratulation!!! You have got the WHOLE BODY---###")
            total_done = True
           
starting_body()  
legs = starting_head_or_legs()
mouth_ant_eye(legs)

