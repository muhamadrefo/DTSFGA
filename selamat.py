import turtle
from turtle import *

huruf1 =('Mongolian Baiti','30','bold')
huruf2 =('Mongolian Baiti','30','bold')
t= turtle.Turtle()

def hut():
    t.penup()
    t.goto(-600, 300)
    t.pendown()
    t.hideturtle()
    hut = 'DIRGAHAYU REPUBLIK INDONESIA KE-76'

    for i in hut:
        t.pencolor('red')
        t.fillcolor('white')
        t.write(i,font=huruf1,align='center')
        t.forward(35)
        t.speed(6)
        

def hastag1():
    t.penup()
    t.goto(-500, 220)
    t.pendown()
    t.hideturtle()
    hstg1 = '#IndonesiaTangguh'
    
    for i in hstg1:
        #t.pencolor('')
        t.fillcolor('white')
        t.write(i,font=huruf2,align='left')
        t.forward(25)
        t.speed(6)
        #t.hideturtle()
        
def hastag2():
    t.penup()
    t.goto(95, 220)
    t.pendown()
    t.hideturtle()
    hstg2 = '#IndonesiaTumbuh'
    
    for i in hstg2:
        #t.pencolor('red')
        t.fillcolor('white')
        t.write(i,font=huruf2,align='center')
        t.forward(25)
        t.speed(6)
        #t.hideturtle()