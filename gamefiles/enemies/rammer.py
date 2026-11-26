import pygame
from gamefiles import player
from gamefiles.entity import *
from gamefiles.enemy import *
from gamefiles.player import *

class Rammer(Enemy):
	def __init__(self, x: float, y: float):
		self.default_color = (139, 69, 19)
		super().__init__(
			entity=Entity(
				pos=pygame.Vector2(x, y),
				size=(40, 40),
				color=self.default_color,
				has_collision=False,
				is_visible=True,
				z_index=0,
			), 
			health=60,
			damage=20,
			speed=100,
			worth=30,
		)
		self.cooldown = 4
		self.active_cooldown = self.cooldown
		self.hit_indicator_duration = 0.125
		self.active_hit_indicator_duration = 0.0
		self.state = "passive"
		self.orientation = 0.0
		self.remaining_distance = 0.0
		self.ramming_distance = 650.0
		self.ramming_speed = 700.0
		self.entities_hit = []

	def update(self, world, screen, inputs, delta_time):
		self.color = RED if self.active_hit_indicator_duration > 0.0 else self.default_color

		self.active_cooldown -= delta_time
		self.active_hit_indicator_duration -= delta_time

		self.active_hit_indicator_duration = pygame.math.clamp(self.active_hit_indicator_duration, 0.0, self.hit_indicator_duration)
		self.active_cooldown = pygame.math.clamp(self.active_cooldown, 0.0, self.cooldown)

		if self.state == "passive":
			player_center = world.player.pos + pygame.Vector2(
				world.player.width / 2,
				world.player.height / 2
			)

			self_center = self.pos + pygame.Vector2(
				self.width / 2,
				self.height / 2
			)
			
			distance = self_center.distance_to(player_center)

			if distance >= self.ramming_distance/2:
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
					self.orientation = math.atan2(direction.y, direction.x)

					self.entities_hit = []
					self.state = "ramming"
					self.remaining_distance = self.ramming_distance
            	
					self.active_cooldown = self.cooldown
		elif self.state == "ramming":
			if self.remaining_distance <= 0:
				self.state = "passive"
			else:
				movement = pygame.Vector2(
        			math.cos(self.orientation),
        			math.sin(self.orientation)
    			) * self.ramming_speed * delta_time
				
				self.remaining_distance -= movement.length()
				self.pos += movement
				
				if self.get_rect().colliderect(world.player.get_rect()) and not world.player in self.entities_hit:
					world.player.get_hit(self.damage, world)
					self.entities_hit.append(world.player)

				for entity in world.entities:
					if isinstance(entity, Humanoid) and not entity in self.entities_hit and entity != self:
						if self.get_rect().colliderect(entity.get_rect()):
							entity.get_hit(self.damage, world)
							self.entities_hit.append(entity)
	
	def get_hit(self, damage: int, world):
		self.health -= damage
		self.active_hit_indicator_duration = self.hit_indicator_duration

		if self.health <= 0.0:
			world.entities.remove(self)
			world.player.points += self.worth
