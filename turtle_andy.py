import click
import turtle

t=turtle.Pen()
t.shape("turtle")
t2=t.clone()
t2.color("red")

while True:
    c = click.getchar()
    move1 = False
    move2 = False
    if c == 'a':
    #if c == '\u0061' or  c.encode('utf-8') == '\xc3\xa0K':
        t.seth(180)
        move1 = True
    elif c ==  's':
        t.seth(180+90)
        move1 = True
    elif c ==  'd' or c == '2':
        t.seth(0)
        move1 = True        
    elif c ==  'w':
        t.seth(90)
        move1 = True        
    elif c == 'j':
        t2.seth(180)
        move2 = True
    elif c ==  'k':
        t2.seth(180+90)
        move2 = True
    elif c ==  'l' or c == '2':
        t2.seth(0)
        move2 = True        
    elif c ==  'i':
        t2.seth(90)
        move2 = True        
    elif c ==  'h':
        t.home()
        t2.home()
        move1 = False
        move2 = False
    elif c ==  'x':
        exit(0)
    else:
        print('Invalid input: ' + c)
        move1 = False
        move2 = False
    print(repr(c.encode('utf-8')))
    if(move1):
        t.forward(100)
    if(move2):
        t2.forward(100)

 
