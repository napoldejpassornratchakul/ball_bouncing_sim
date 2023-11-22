import turtle
import random

class Ball:
    def __init__(self, speed = 0,size = 0):
        self.canvas_height = turtle.screensize()[1]
        self.canvas_width = turtle.screensize()[0]
        self.speed = speed
        self.size = size
        self.xpos = []
        self.ypos = []
        self.vy = []
        self.vx = []
        self.ball_color = []
        self.ball_radius = 0.05 * self.canvas_width




    def draw_circle(self,i):
        turtle.penup()
        turtle.color(self.ball_color[i])
        turtle.fillcolor(self.ball_color[i])
        turtle.goto(self.xpos[i],self.ypos[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.ball_radius)
        turtle.end_fill()

# def draw_circle(color, size, x, y):
#     # draw a circle of radius equals to size at x, y coordinates and paint it with color
#     turtle.penup()
#     turtle.color(color)
#     turtle.fillcolor(color)
#     turtle.goto(x,y)
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.circle(size)
#     turtle.end_fill()

    def move_circle(self,num_of_ball):
    # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos[num_of_ball] += self.vx[num_of_ball]
        self.ypos[num_of_ball] += self.vy[num_of_ball]
# def move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
#     # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
#     xpos[i] += vx[i]
#     ypos[i] += vy[i]
#
#     # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[num_of_ball] + self.vx[num_of_ball]) > self.canvas_width - self.ball_radius:
            self.vx[num_of_ball] = -self.vx[num_of_ball]
#     if abs(xpos[i] + vx[i]) > (canvas_width - ball_radius):
#         vx[i] = -vx[i]
#
#     # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[num_of_ball] + self.vy[num_of_ball]) > self.canvas_height - self.ball_radius:
            self.vy[num_of_ball] = -self.vy[num_of_ball]
#     if abs(ypos[i] + vy[i]) > (canvas_height - ball_radius):
#         vy[i] = -vy[i]
    def initializing(self,num_of_balls):
        for i in range(num_of_balls):
            self.xpos.append(
                random.randint(-1 * self.canvas_width - self.ball_radius , self.canvas_width - self.ball_radius))


            self.ypos.append(
                random.randint(-1 * self.canvas_height - self.ball_radius, self.canvas_height - self.ball_radius))


            self.vx.append(random.randint(1, 0.01 * self.canvas_width))
            self.vy.append(random.randint(1, 0.01*self.canvas_height))
            self.ball_color.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
# def initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
#     # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
#     for i in range(num_balls):
#         xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
#         ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
#         vx.append(random.randint(1, 0.01*canvas_width))
#         vy.append(random.randint(1, 0.01*canvas_height))
#         ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
