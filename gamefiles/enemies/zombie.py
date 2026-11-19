import pygame
from gamefiles.entity import *
from gamefiles.enemy import *
from gamefiles.player import *

class Zombie(Enemy):
	def __init__(self, x: int, y: int):
		super().__init__(
			entity=Entity(
				pos=pygame.Vector2(x, y),
				size=(100, 100),
				color=(255, 255, 255),
				has_collision=False,
				is_visible=True,
				z_index=0,
			), 
			health=100,
			damage=100,
			speed=2
		)

	def update(self, world, inputs):
		player_center = world.player.pos + pygame.Vector2(
			world.player.width / 2,
			world.player.height / 2
		)

		self_center = self.pos + pygame.Vector2(
			self.width / 2,
			self.height / 2
		)

		self_center = self_center.move_towards(
			player_center,
			self.speed
		)

		self.pos = self_center - pygame.Vector2(
			self.width / 2,
			self.height / 2
		)
