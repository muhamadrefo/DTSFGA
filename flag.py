import turtle
from turtle import *

#define a turtle instance
t= turtle.Turtle()
speed(3)

def flag():
    
    #initially penup()
    t.penup() #pen up
    t.goto(-50, 270)
    t.pendown() #pen down

    #bikin warna merah
    t.color('red')
    t.begin_fill()
    t.forward(100) #kanan
    t.right(90) #haluan kanan bawah
    t.forward(25) #lurus bawah
    t.right(90) #haluan kiri
    t.forward(100) #lurus kiri
    t.right(90) #haluan kanan atas
    t.forward(25) #lurus atas
    t.end_fill() #fill with red
    t.left(180) #turn 180 degree
    t.forward(25) #end point red


    #bikin warna putih
    t.color('silver')
    t.begin_poly()
    t.forward(25)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(25)
    t.end_poly()
    t.hideturtle()