import math
import pygame
from gamefiles.entity import Entity
from gamefiles.humanoid import Humanoid

class Bullet(Entity):
	def __init__(self, parent: Entity, pos: pygame.Vector2, size: tuple[int, int], orientation: float, speed: int, damage: int, penetrate_count: int,split_count: int = 0,ignore_entities: list | None = None ):
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
		self.penetrate_count = penetrate_count
		self.entities_hit = list(ignore_entities) if ignore_entities else []
		self.split_count = split_count

	def spawn_split_bullets(self, world):
		for angle_offset in (-1.57,1.57):
			new_bullet = Bullet(
                parent=self.parent,
                pos=self.pos.copy(),
                size=(self.width, self.height),
                orientation=self.orientation + angle_offset,
                speed=self.speed,
                damage=self.damage,
                penetrate_count=1,
                split_count=self.split_count - 1,
                ignore_entities=self.entities_hit)
			world.entities.append(new_bullet)

	def update(self, world, screen, inputs, delta_time):
		if self.parent != world.player:
			if self.get_rect().colliderect(world.player.get_rect()) and not world.player in self.entities_hit:
				world.player.get_hit(self.damage, world)
				self.entities_hit.append(world.player)

				self.penetrate_count -= 1
				if self.penetrate_count == 0:
					world.entities.remove(self)

		if self.parent == world.player:
			for	entity in world.entities:
				if isinstance(entity, Humanoid) and entity != self.parent and not entity in self.entities_hit:
					if self.get_rect().colliderect(entity.get_rect()):
						entity.get_hit(self.damage, world)
						self.entities_hit.append(entity)

						if len(self.entities_hit) >= 1 and self.split_count > 0:
							self.spawn_split_bullets(world)

						self.penetrate_count -= 1
						if self.penetrate_count == 0:
							world.entities.remove(self)

		movement = pygame.Vector2(
        	math.cos(self.orientation),
        	math.sin(self.orientation)
    	) * self.speed

		self.pos += movement * delta_time

		if (self.pos - world.player.pos).length() >= 2000:
			world.entities.remove(self)
