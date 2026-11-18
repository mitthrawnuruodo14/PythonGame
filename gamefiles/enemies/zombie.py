import pygame
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
			speed=2
		)

	def update(self, world):
		direction = pygame.Vector2(
			world.player.rect.center
		) - pygame.Vector2(self.rect.center)

		if direction.length() != 0:
			direction = direction.normalize()

		self.rect.centerx += round(direction.x * self.speed)
		self.rect.centery += round(direction.y * self.speed)
