import random
from turtle import Turtle, Screen

screen = Screen()

is_race_on = False
screen.setup(width = 500, height= 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70,-40, -10,20,50,80]
turtle_list = []



for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x= -220, y= y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is winner!")

        turtle.forward(random.randint(0, 10))




screen.exitonclick()