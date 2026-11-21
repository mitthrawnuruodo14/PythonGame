import pygame
from gamefiles.entity import *
from gamefiles.enemy import *
from gamefiles.player import *

class Zombie(Enemy):
	def __init__(self, x: int, y: int):
		super().__init__(
			entity=Entity(
				pos=pygame.Vector2(x, y),
				size=(60, 60),
				color=(255, 255, 255),
				has_collision=False,
				is_visible=True,
				z_index=0,
			), 
			health=100,
			damage=20,
			speed=100,
		)
		self.cooldown=1.5
		self.active_cooldown = 0.0
		self.hit_indicator_duration = 0.125
		self.active_hit_indicator_duration = 0.0

	def update(self, world, screen, inputs, delta_time):
		self.color = RED if self.active_hit_indicator_duration > 0.0 else WHITE

		self.active_cooldown -= delta_time
		self.active_hit_indicator_duration -= delta_time

		self.active_hit_indicator_duration = pygame.math.clamp(self.active_hit_indicator_duration, 0.0, self.hit_indicator_duration)
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
			world.player.get_hit(self.damage, world)
			self.active_cooldown = self.cooldown
	
	def get_hit(self, damage: int, world):
		self.health -= damage
		self.active_hit_indicator_duration = self.hit_indicator_duration

		if self.health <= 0.0:
			world.entities.remove(self)
