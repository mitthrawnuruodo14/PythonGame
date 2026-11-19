from __future__ import annotations
import pygame

class Entity:
	def __init__(self, pos: pygame.Vector2, size: tuple[int, int], color: tuple, has_collision: bool, is_visible: bool, z_index: int):
		self.pos = pos
		self.width = size[0]
		self.height = size[1]
		self.color = color
		self.has_collision = has_collision
		self.is_visible = is_visible
		self.z_index = z_index

	def get_rect(self):
		return pygame.Rect(round(self.pos.x), round(self.pos.y), self.width, self.height)

	def uncollide(self, entity: Entity):
		self_rect = self.get_rect()
		entity_rect = entity.get_rect()

		if not self_rect.colliderect(entity_rect):
			return

		overlap_left = self_rect.right - entity_rect.left
		overlap_right = entity_rect.right - self_rect.left
		overlap_top = self_rect.bottom - entity_rect.top
		overlap_bottom = entity_rect.bottom - self_rect.top

		min_overlap = min(
			overlap_left,
			overlap_right,
			overlap_top,
			overlap_bottom
		)

		if min_overlap == overlap_left:
			self.pos.x = entity_rect.left - self.width

		elif min_overlap == overlap_right:
			self.pos.x = entity_rect.right

		elif min_overlap == overlap_top:
			self.pos.y = entity_rect.top - self.height

		else:
			self.pos.y = entity_rect.bottom

	def draw_screen(self, screen: pygame.Surface):
		if self.is_visible:
			pygame.draw.rect(screen, self.color, self.get_rect())

	def update(self, world, inputs, delta_time):
		pass
