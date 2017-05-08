import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
def giyuk(size) :
	t1.fd(size)
	t1.rt(90)		
	t1.fd(size)



def giwind(size) :
	
	oldpos = t1.pos()
	giyuk(size)
	turn = 45
	oldheading = t1.heading()
	t1.penup()
	t1.setpos(oldpos)
	t1.pendown()
	t1.setheading(oldheading + turn)
giwind(100)
giwind(100)
giwind(100)
giwind(100)
giwind(100)
giwind(100)
giwind(100)
giwind(100)
wn.exitonclick()