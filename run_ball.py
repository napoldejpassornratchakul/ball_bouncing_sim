from ball import *
import turtle

num_balls = int(input("Number of balls to simulate: "))
speed = turtle.speed(0)
frame = turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)

ball = Ball(speed, frame)
ball.initializing(num_balls)
while (True):
    turtle.clear()
    for i in range(num_balls):
        ball.draw_circle(i)
        ball.move_circle(i)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()