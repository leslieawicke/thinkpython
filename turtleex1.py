import turtle

def square(t, len):
	for i in range(4):
		t.fd(len)
		t.lt(90)

bob = turtle.Turtle()
square(bob, 145)

turtle.mainloop()