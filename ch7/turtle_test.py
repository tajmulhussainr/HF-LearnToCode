import turtle

window = turtle.Screen()
window.setup(100,100)
while True:
	window.update()

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')

def make_square(the_turtle):
	for i in range(0,4):
		the_turtle.forward(100)
		the_turtle.right(90)

make_square(slowpoke)

window.mainloop()