import pygame
from gamefiles import player
from gamefiles.entity import *
from gamefiles.enemy import *
from gamefiles.player import *

class Skeleton(Enemy):
	def __init__(self, x: int, y: int):
		super().__init__(
			entity=Entity(
				pos=pygame.Vector2(x, y),
				size=(60, 60),
				color=(200, 200, 200),
				has_collision=False,
				is_visible=True,
				z_index=0,
			), 
			health=60,
			damage=20,
			speed=75,
		)
		self.cooldown=2.25
		self.active_cooldown = 0.0
		self.hit_indicator_duration = 0.125
		self.active_hit_indicator_duration = 0.0

	def update(self, world, screen, inputs, delta_time):
		SKELETON_MAX_DISTANCE = 500

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
		
		distance = self_center.distance_to(player_center)

		if distance >= SKELETON_MAX_DISTANCE:
			self_center = self_center.move_towards(
				player_center,
				self.speed * delta_time
			)

			self.pos = self_center - pygame.Vector2(
				self.width / 2,
				self.height / 2
			)
		else:
			if self.active_cooldown == 0.0:
				direction = world.player.pos - self.pos
				angle = math.atan2(direction.y, direction.x)
            
				bullet_pos = pygame.Vector2(self.pos.x + self.width/2, self.pos.y + self.height/2)
				world.entities.append(Bullet(self, bullet_pos, (10, 10), angle, 1200, 20, 1))

				self.active_cooldown = self.cooldown
	
	def get_hit(self, damage: int, world):
		self.health -= damage
		self.active_hit_indicator_duration = self.hit_indicator_duration

		if self.health <= 0.0:
			world.entities.remove(self)
