from turtle import Turtle,Screen
import random
myscreen = Screen()
myscreen.setup(width=500, height=400)  #to resize screen

game_on = False
#takes text input from user in a dialog box
user_bet = myscreen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour (V/B/G/Y/O/R):")

if user_bet: #if user entered a value
    game_on = True

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for index in range(0,6): #to get turtles to starting line
    new_turt = Turtle(shape="turtle")
    new_turt.color(colors[index])
    new_turt.penup()
    new_turt.goto(-230, y_positions[index])
    turtles.append(new_turt)

while game_on: #to continue moving a turtle by a random distance
    for turt in turtles: #to move all the 6 turtle simulatneously
        if turt.xcor()>230:  #checking x coordinate for finish line
            game_on = False
            winning_turtle = turt.pencolor()
            if user_bet.lower() == winning_turtle:
                print(f"You won! The {winning_turtle} turtle won the race!")
            else:
                print(f"You lost! The {winning_turtle} turtle won the race!")
        random_distance = random.randint(0,10)
        turt.forward(random_distance)

myscreen.exitonclick()
