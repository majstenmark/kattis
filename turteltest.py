from turtle import *

leo = Turtle()
leo.color('black', 'green')
leo.shape("turtle")
leo.pencolor('red')
leo.pensize(5)
leo.speed(0)
leo.setheading(90)
def square(side,color, fill=True):
    leo.fillcolor(color)
    leo.pencolor(color)
    
    if fill:
        leo.begin_fill()
    for i in range(4): # 0, 1, 2, 3
        leo.forward(side)
        leo.right(90)
    if fill :
        leo.end_fill()

    





#square(200,'lightgreen')
#square(100,'aqua')
#square(50,'violet')
#square(150,'pink', False)
def draw(x,y,color,side, fill = True):    
    leo.penup()
    leo.setx(x)

    leo.sety(y)
    leo.pendown()
    square(side,color,fill)
    
draw(-150,-150,'green',300)
draw(0,0,'red',30)
draw(60,60,'black',50,False)
draw(63,63,'white',44)
draw(-36,60,'black',50,False)
draw(-33,63,'white',44)
draw(85,60,'black',10)
draw(-16,60,'black',10)
draw(-20,-100,'red', 70)
draw(-10,-90,'black',50)




done()



