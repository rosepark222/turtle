import click
import turtle

t=turtle.Pen()
t.shape("turtle")

while True:
    c = click.getchar()
    move = True
    #if c == 'a':
    if c == '\u0061' or  c.encode('utf-8') == '\xc3\xa0K':
        t.seth(180)
    elif c ==  's':
        t.seth(180+90)
    elif c ==  'd' or c == '2':
        t.seth(0)
    elif c ==  'w':
        t.seth(90)
    elif c ==  'h':
        t.home()
        move = False
    elif c ==  'x':
        exit(0)
    else:
        print('Invalid input: ' + c)
        move = False
    print(repr(c.encode('utf-8')))
    if(move):
        t.forward(100)

 
