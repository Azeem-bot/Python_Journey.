from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
for _ in range(15):
    jimmy.forward(10)
    jimmy.penup()
    jimmy.forward(10)
    jimmy.pendown()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()