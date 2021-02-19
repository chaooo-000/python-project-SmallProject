from turtle import *
t = Turtle()
t.color('red', 'pink')
t.begin_fill()
for i in range(5):
    t.fd(200)
    t.right(144)
t.end_fill()

#   螺旋
#   for i in range(1, 100, 10):
#       t.fd(i)
#       t.right(90)

t.hideturtle()
done()
