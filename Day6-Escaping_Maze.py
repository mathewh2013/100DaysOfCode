# Functions, Code Blocks and While Loops

#Functions 
#Built In
# e.g. print(), len(), int()

# To create a fuction use the term 'def'

#def my_function():
#    print("hello")
#    print("bye")
    
# To call function just enter name + ()

#my_function()

# Todays exersise was using Functions, Code Blocks and While Loops on Reeborgs world (https://reeborg.ca/) to give instructions to a robot to exit a maze. While it wont make sense here find below code:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: 
        turn_left()