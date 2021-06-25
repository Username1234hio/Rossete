import turtle
t = turtle.Pen()
noc = int(turtle.numinput("Number of circles", "How many circles", 6))
ip = int(turtle.numinput("speed of drawing your circles", "speed please types: fastest=0, fast=10, normal=6, slow=3, slowest=1", 0))
nn = int(turtle.numinput("how many colors should you use", "max is 7", 7))
colors = ["blue", "green", "teal", "purple", "red", "orange", "black"]
for x in range(noc):
	t.circle(100)
	t.left(360/noc)
	t.speed(ip)
	t.pencolor(colors[x%nn])
	t.circle(75)
	t.left(360/noc)
	t.circle(25)
	t.left(360/noc)
	t.circle(50)
	t.left(360/noc)
	t.circle(25)
	t.left(360/noc)
	

