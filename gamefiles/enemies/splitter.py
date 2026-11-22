import pygame
from gamefiles.entity import *
from gamefiles.enemy import *
from gamefiles.player import *

class Splitter(Enemy):
	def __init__(self, x: float, y: float, health, level, speed):
		self.default_color = (0, 0, 255)
		super().__init__(
			entity=Entity(
				pos=pygame.Vector2(x, y),
				size=((level**1.5)*25, (level**1.5)*25),
				color=self.default_color,
				has_collision=False,
				is_visible=True,
				z_index=0,
			), 
			health=health,
			damage=20,
			speed=speed,
		)
		self.level = level
		self.cooldown=1.5
		self.active_cooldown = 0.0
		self.hit_indicator_duration = 0.125
		self.active_hit_indicator_duration = 0.0
		self.original_health = health

	def update(self, world, screen, inputs, delta_time):
		self.color = RED if self.active_hit_indicator_duration > 0.0 else self.default_color

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
			if (self.level - 1) > 0:
				world.entities.append(Splitter(self.pos.x + self.width/2, self.pos.y, self.original_health/2, self.level - 1, self.speed*2))
				world.entities.append(Splitter(self.pos.x - self.width/2, self.pos.y, self.original_health/2, self.level - 1, self.speed*2))

			world.entities.remove(self)
