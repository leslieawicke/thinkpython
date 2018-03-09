import math
import turtle
from ch4ex import arc
from ch4ex import polyline

def letterline(t, n, length, angle,):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
    	t.lt(angle)
    	t.fd(length)

def draw_a(t):
	'''Draws the letter A.
	t = the turtle'''
	t.pd()
	letterline(t, n = 1, length = 100, angle = 60)
	letterline(t, n = 1, length = 100, angle = -120)
	t.pu()
	letterline(t, n = 1, length = 40, angle = 180)
	t.pd()
	letterline(t, n = 1, length = 60, angle = 60)
	t.pu()
	t.lt(180)
	letterline(t, n = 1, length = 60, angle = 0)
	letterline(t, n = 1, length = 40, angle = -60)
	t.lt(60)

def draw_b(t):
	'''Draws the letter B.
	t = the turtle.'''
	t.pd()
	letterline(t, n = 1, length = 90, angle = 90)
	t.lt(-90)
	arc(t, r = 30, angle = -120)
	t.lt(120)
	arc(t, r = 30, angle = -120)
	letterline(t, n = 1, length = 52, angle = -60)
	t.pu()
	letterline(t, n = 1, length = 52, angle = 180)

def draw_c(t):
	'''Draws the letter C.
	t = the turtle.'''
	t.lt(90)
	t.fd(90)
	t.rt(90)
	t.fd(90)
	t.lt(180)
	t.pd()
	arc(t, r = 45, angle = 100)
	arc(t, r = 45, angle = 100)
	t.pu()


#draw the letter A
bob = turtle.Turtle()
draw_a(bob)
bob.fd(30)
draw_c(bob)

# wait for the user to close the window
turtle.mainloop()