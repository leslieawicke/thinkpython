import math
import turtle
from ch4ex import arc

bob = turtle.Turtle()
radius = 250
n = 5
overlap = 45


def petal(t, r, n, o):
	"""draws a petal shape with given radius (r) and angle (a) derived from the number of petals desired (n).
	t = turtle"""
	a = 360/n + o
	arc(t, r, a)
	bob.lt(180 - a)
	arc(t, r, a)
	bob.lt(180 - o)


def flower(t, r, n, o):
	for i in range(n):
		petal(t, r, n, o)


flower(bob, radius, n, overlap)
turtle.mainloop()

# the angle of bob's turn at the end of his first arc should be 180 degrees minus the angle of the arc he just drew.