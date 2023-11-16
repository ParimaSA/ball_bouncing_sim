import turtle
import random


class Ball_list:
    def __init__(self, canvas_width, canvas_height, ball_radius, num_balls):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.num_balls = num_balls
        self.all_ball = []
        self.add_ball()

    def add_ball(self):
        for _ in range(self.num_balls):
            pos_x = (random.randint(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            pos_y = (random.randint(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            velo_x = (random.randint(1, 0.01 * self.canvas_width))
            velo_y = (random.randint(1, 0.01 * self.canvas_height))
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            new_ball = Ball(color, pos_x, pos_y, velo_x, velo_y, self.ball_radius)
            self.all_ball.append(new_ball)

    def display_screen(self):
        while (True):
            turtle.clear()
            for i in range(num_balls):
                self.all_ball[i].draw_circle()
                self.all_ball[i].move_circle(self.canvas_width, self.canvas_height)
            turtle.update()

class Ball:
    def __init__(self, color, x, y, velo_x, velo_y, r):
        self.color = color
        self.x = x
        self.y = y
        self.vx = velo_x
        self.vy = velo_y
        self.radius = r

    def draw_circle(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()

    def move_circle(self, canvas_width, canvas_height):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.x += self.vx
        self.y += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.x + self.vx) > (canvas_width - self.radius):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.y + self.vy) > (canvas_height - self.radius):
            self.vy = -self.vy


num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
all_ball = Ball_list(canvas_width, canvas_height, ball_radius, num_balls)
all_ball.display_screen()


# draw_circle('yellow', 20,0, 0)
# draw_circle('red', 40,100, 100)