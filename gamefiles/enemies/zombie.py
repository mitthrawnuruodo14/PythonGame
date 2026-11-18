from gamefiles.entity import *
from gamefiles.enemy import *
from gamefiles.player import *

class Zombie(Enemy):
	def __init__(self, x: int, y: int):
		super().__init__(
			entity=Entity(
				rect=pygame.Rect(x, y, 100, 100),
				color=(255, 255, 255),
				has_collision=False,
				is_visible=True
			), 
			health=100,
			damage=100,
			speed=100
		)

	def update(self, world):
		self.rect.centerx += 1
