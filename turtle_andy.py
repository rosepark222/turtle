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
