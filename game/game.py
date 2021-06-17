from ursina import *
from random import randint

app = Ursina()

background_texture = load_texture('assets/ssky.png')
cart_texture = load_texture('assets/cart.png')
apple_texture = load_texture('assets/apple.png')
dx = 0.1
dy = 0.09

class Player(Entity):
	def __init__(self):
		super().__init__(
			model = 'cube',
			texture = cart_texture,
			position = (0,-3,0),
			scale = (1,1,.01),
			collider = 'box',
			)
		self.eaten = 0
		self.record = 0

	def update(self):
		global dx
		global dy
		global r
		global apple

		s = True

		if held_keys['d']:
			self.x += dx

		if held_keys['a']:
			self.x -= dx

		if self.x > 3.89:
			self.x = 3.89
		if self.x < -3.89:
			self.x = -3.89

		hit_info = self.intersects()
		if hit_info.hit:
			apple.disable()
			apple = Entity(model = 'cube', texture = apple_texture, scale = (.5,.5,.01), position = (randint(-3,3),4,0), collider = 'box')
			self.eaten += 1
			self.record += 1
			Audio('assets/picked.wav')

		apple.y -= dy
		
		if apple.y < -5:
			apple.disable()
			apple = Entity(model = 'cube', texture = apple_texture, scale = (.5,.5,.01), position = (randint(-4,4),4,0), collider = 'box')
			self.record = 0
			Audio('assets/fell.wav')

		stats.text = 'Score: {}\nRecord: {}'.format(self.eaten, self.record)

stats = Text(text = 'Score: \nRecord: ', scale = (1,1), position = (0.35,0.45), background = True)
apple = Entity(model = 'cube', texture = apple_texture, scale = (.5,.5,.01), position = (0,4,0), collider = 'box')
background = Entity(model = 'quad', texture = background_texture, scale = 10)
aspect_ratio = Entity(model = 'quad', color = color.black, scale = (3, 60), position = (5.8, 0))
aspect_ratio_two = Entity(model = 'quad', color = color.black, scale = (3, 60), position = (-5.8, 0))

player = Player()


app.run()