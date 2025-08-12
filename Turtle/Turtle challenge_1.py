from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("red")
for _ in range(4):
    jimmy.forward(100)
    jimmy.right(90)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()



