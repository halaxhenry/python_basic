from myTurtle import *

import turtle

inStr = ''
swidth, sheight = 300, 300
tX, tY, t_Angle, t_Size = [0]*4

turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(5)
inStr = getString()

for ch in inStr:
    tX, tY, t_Angle, t_Size = getXYAS(swidth, sheight)
    r, g, b = getRGB()

    turtle.goto(tX, tY)
    turtle.left(t_Angle)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', t_Size, 'bold'))

turtle.done()
