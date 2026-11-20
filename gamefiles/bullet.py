import math
import pygame
from gamefiles.entity import Entity
from gamefiles.humanoid import Humanoid

class Bullet(Entity):
	def __init__(self, parent: Entity, pos: pygame.Vector2, size: tuple[int, int], orientation: float, speed: int, damage: int):
		super().__init__(
			pos=pygame.Vector2(pos),
			size=size,
			color=(0, 0, 0),
			is_visible=True,
			has_collision=False,
			z_index=100,
		)
		self.parent = parent
		self.orientation = orientation
		self.speed = speed
		self.damage = damage

	def update(self, world, screen, inputs, delta_time):
		for	entity in world.entities:
			if isinstance(entity, Humanoid) and entity != self.parent:
				if self.get_rect().colliderect(entity.get_rect()):
					entity.get_hit(self.damage)

		movement = pygame.Vector2(
        	math.cos(self.orientation),
        	math.sin(self.orientation)
    	) * self.speed

		self.pos += movement * delta_time
