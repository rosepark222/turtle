import click
import turtle

t=turtle.Pen()
t.shape("turtle")

while True:
    c = click.getchar()
    move = True
    if c == 'a':
        t.seth(180)
    elif c ==  's':
        t.seth(180+90)
    elif c ==  'd':
        t.seth(0)
    elif c ==  'w':
        t.seth(90)
    elif c ==  'h':
        t.home()
        move = False
    elif c ==  'x':
        exit(0)
    else:
        print('Invalid input :(')
        move = False
    if(move):
        t.forward(100)
 
