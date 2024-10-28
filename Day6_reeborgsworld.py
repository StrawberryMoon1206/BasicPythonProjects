print("Please open 'Reeborg's World: Maze' on your browser by holding ctrl/cmd (if operated through terminal) and clicking on this link:-")
linkforthemaze = r"https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"
print(linkforthemaze)
quit()
# Running the following code in the area given for 'python code' in Reeborg's world
# will make Reeborg navigate through the maze and reach the goal
def turn_left():
    '''Predetermined function to make reeborg turn left'''
    pass
def move():
    '''Predetermined function to make reeborg move one step'''
    pass
def at_goal():
    '''Predetermined function to check whether reeborg is at the goal'''
    pass
def front_is_clear():
    '''Predetermined function to check if the front is clear (without any wall or boundary)'''
    pass
def right_is_clear():
    '''Predetermined function to check if the right is clear (without any wall or boundary)'''
    pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():  #this will tackle the case if the robot enters an infinite loop, when the right_is_clear() condition is always true
    move()  #making the robot reach near a wall
turn_left()  #making it turn left so that the robot has a wall on its right

while not at_goal():  #following given algorithm

    if right_is_clear():
        turn_right()
        move()

    elif front_is_clear():
        move()

    else:
        turn_left()
