import turtle as tr  
import random
import time

# константи
R = 6271000		# радіус землі в метрах
M = 5.9722 * 10 ** 24	# маса землі в кілограмах
G = 6.674 * 10 ** (-11)		# гравітаційна стала (м3 * кг-1 * с-2)

# ключові змінні:
COUNT = 1000
SPEED_MULT = 100
WIN_W = 720
WIN_H = 720

class Asteroid:
	def __init__(self, x, y, x_speed, y_speed):
		self.x = x
		self.y = y 
		self.x_speed = x_speed  
		self.y_speed = y_speed 
		self.turtle = tr.Turtle()
		self.turtle.color("#" + random.choice("1233456789AB") * 3)
		self.turtle.shape("circle")
		self.turtle.shapesize(random.uniform(0.2, 0.7))
		self.turtle.up()

	def Move(self, time):
		distance = (self.x ** 2 + self.y ** 2) ** 0.5
		if distance < R:
			self.turtle.ht()
			return False                       
		a = G * M / distance ** 2     # прискорення тяжіння
		#  прискорення горизонтальне та вертикальне:
		x_a = a * self.x / distance
		y_a = a * self.y / distance
		self.x_speed -= x_a * time
		self.y_speed -= y_a * time
		# нові координати:
		self.x += self.x_speed * time
		self.y += self.y_speed * time
		return True

	def Print(self):
		self.turtle.goto(m_px(self.x), m_px(self.y))

def px_m(px):			# конвертує пікселі в метри
	return px * 100000   

def m_px(m):	
	return m / 100000	# конвертує метри в пікселі

# start - умовний початок програми 

window = tr.Screen()
window.setup(WIN_W, WIN_H)
window.tracer(0)
window.bgpic("bg.png")
window.register_shape("Earth125.gif")

# малюємо землю:
earth = tr.Turtle()
earth.color("#000", "#1486FF") 
earth.shape("Earth125.gif")



asteroids = []
for i in range(COUNT):
	asteroids.append(
		Asteroid(
			random.randint(-px_m(WIN_W//2), px_m(WIN_W//2)),
			random.randint(-px_m(WIN_H//2), px_m(WIN_H//2)),
			random.randint(-8000, 8000),
			random.randint(-8000, 8000)))

while True:
	for asteroid in asteroids:
		if asteroid.Move(SPEED_MULT):
			asteroid.Print()
		else:
			asteroids.remove(asteroid)		

	window.update()
