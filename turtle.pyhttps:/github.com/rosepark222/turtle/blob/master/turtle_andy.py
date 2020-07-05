import click
import turtle

t=turtle.Pen()
t.shape("turtle")

while True:
    c = click.getchar()
    if c == 'a':
        t.seth(180)
    elif c ==  's':
        t.seth(180+90)
    elif c ==  'd':
        t.seth(0)
    elif c ==  'w':
        t.seth(90)
    elif c ==  'c':
        exit(0)
    else:
        print('Invalid input :(')
    t.forward(100)


import turtle
#turtle.setup (width=200, height=200, startx=0, starty=0)
t=turtle.Pen()
t.shape("circle")

while(1):
    sec = input("type a or d")
    if sec == 'a':
        t.left(90)
        t.forward(100)        
    elif sec == 'd':
        t.right(90)
        t.forward(100)        
    prev = sec


        
t.shape("turtle")
t.left(45)
sec = input("Press Enter to quick.\n")
t.forward(100)
sec = input("Press Enter to quick.\n")
t.left(135)
sec = input("Press Enter to quick.\n")
t.forward(70)
sec = input("Press Enter to quick.\n")
t.left(90)
sec = input("Press Enter to quick.\n")
t.forward(70)
sec = input("Press Enter to quick.\n")


#colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange']
#t=turtle.Pen()
#t.shape("turtle")
#turtle.bgcolor('black')
#for x in range(360,0,-1):
#   t.pencolor(colors[x%6])
#   t.width(x/100+1)
#   t.forward(x)
#   t.left(59)

