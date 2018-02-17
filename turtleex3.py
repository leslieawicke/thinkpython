import turtle
import math

def polyline(t, n, len, angle):
	for i in range(n):
		t.fd(len)
		t.lt(angle)

def polygon(t, n, len):
	angle = 360/n
	polygon(t, n, len, angle)

def arc(t, r, angle):
	arclen = 2 * math.pi * r * angle/360
	print('Arc length = {}'.format(arclen))
	n = int(arclen/3) + 1
	print('Number of sides = {}'.format(n))
	step_len = arclen/n
	step_angle = angle/float(n)
	print("step angle = {} step length = {}".format(step_angle, step_len))
	polyline(t, n, step_len, step_angle)

def circle(t,r):
	arc(t, r, 360)

bob = turtle.Turtle()
circle(bob, 100)

turtle.mainloop()