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
			speed=75,
		)
		self.cooldown=3.0
		self.active_cooldown = 0.0

	def update(self, world, inputs, delta_time):
		self.active_cooldown -= delta_time
		self.active_cooldown = pygame.math.clamp(self.active_cooldown, 0.0, self.cooldown)

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
			self.speed * delta_time
		)

		self.pos = self_center - pygame.Vector2(
			self.width / 2,
			self.height / 2
		)
	
		if self.get_rect().colliderect(world.player.get_rect()) and self.active_cooldown == 0.0:
			world.player.get_hit(self.damage)
			self.active_cooldown = self.cooldown
