import turtle
colours = ['red',  'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolour('grey')
for x in range(360):
    t.pencolours(colours[x % 6])
    t.width(x/100 + 1)
    t.foward(x)
    t.left(50)
    
turtle.done()