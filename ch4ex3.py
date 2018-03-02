import math
import turtle
from ch4ex import arc

bob = turtle.Turtle()
radius = 100
n = 5
p = 6
d = 7


def triangle(t, r, n):
	a = 360 / n
	ab = (180 - a)/2
	t = a/2
	b = r * math.sin(math.radians(t))
	bob.lt(t)
	bob.fd(r)
	bob.rt(180 - ab)
	bob.fd(2 * b)
	bob.rt(180 - ab)
	bob.fd(r)
	bob.rt(180 - (a +t))

def pie (t, r, n):
	for i in range(n):
		triangle(t, r, n)

bob.pu()
bob.bk(radius * 2 + 10)
bob.pd()
pie(bob, radius, n)
bob.pu()
bob.fd(radius * 2 + 10)
bob.pd()
pie(bob, radius, p)
bob.pu()
bob.fd(radius * 2 + 10)
bob.pd()
pie(bob, radius, d)
turtle.mainloop()

# theta = 360/2n
# hypoteneuse = radius
# adjacent = hypoteneuse * cos(theta)
# opposite = hypoteneuse * sin(theta)
# base = 2 * opposite
# angle = 360/n