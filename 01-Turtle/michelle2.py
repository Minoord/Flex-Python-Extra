import turtle             
colors = [ "red","purple","blue","green","orange","yellow"]
turtle.speed(0)
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.circle(x)
   my_pen.right(90)
   
turtle.done()
