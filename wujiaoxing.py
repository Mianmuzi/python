import turtle

turtle.fillcolor('red')
turtle.begin_fill()


while True:
    turtle.forward(220)
    turtle.right(144)
    if abs(turtle.pos())<1:
        break

turtle.fd(84)
for i in range(5):
    turtle.fd(52)
    turtle.right(72)
turtle.end_fill()
turtle.done()
