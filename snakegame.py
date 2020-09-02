#import Tkinter as TK
import turtle
import time

win =turtle.Screen()
win.title("Snake Game by Sang")
win.setup(width=600, height=600)
#win.tracer(0) #turns off screen updates
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.goto(0,0)


head.direction = "left"


delay = 0.1

def go_up():
	head.direction = "up"
def go_down():
	head.direction = "down"
def go_left():
	head.direction = "left"
def go_right():
	head.direction = "right"








#functions
def move():
	if head.direction == 'down':
		y = head.ycor()
		head.sety(y - 20)
	if head.direction == 'up':
		y = head.ycor()
		head.sety(y + 20)
	if head.direction == 'left':
		x = head.xcor()
		head.setx(x - 20)
	if head.direction == 'right':
		x = head.xcor()
		head.setx(x + 20)


# Keyboard bindings
win.listen()
win.onkeypress(go_up, "up")
win.onkeypress(go_down, "down")
win.onkeypress(go_left, "left")
win.onkeypress(go_right, "right")
 



#Main game loop
while True:

	win.update()







move()
time.sleep(delay)

win.mainloop()


