import turtle
t = turtle.Pen()
colors = ["blue", "green", "red", "orange", "purple", "green", "black"]
noc = int(turtle.numinput("# of the greatest circles", 
                         "how many circles in your rossete", 6))
ip = int(turtle.numinput("speed of drawing your circles", "speed please types: fastest=0, fast=10, normal=6, slow=3, slowest=1", 0))
nn = int(turtle.numinput("how many colors should you use", "max is 7", 7))

for x in range(noc):
	t.pencolor(colors[x%nn])
	t.circle(100)
	t.left(360/noc)
	t.speed(ip)
