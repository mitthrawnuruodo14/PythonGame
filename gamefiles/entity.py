from __future__ import annotations
import pygame

class Entity:
	def __init__(self, rect: pygame.Rect, color: tuple, has_collision: bool, is_visible: bool):
		self.rect = rect
		self.color = color
		self.has_collision = has_collision
		self.is_visible = is_visible

	def uncollide(self, entity: Entity):
		if not self.rect.colliderect(entity.rect):
			return

		overlap_left = self.rect.right - entity.rect.left
		overlap_right = entity.rect.right - self.rect.left
		overlap_top = self.rect.bottom - entity.rect.top
		overlap_bottom = entity.rect.bottom - self.rect.top

		min_overlap = min(
			overlap_left,
			overlap_right,
			overlap_top,
			overlap_bottom
		)

		if min_overlap == overlap_left:
			self.rect.right = entity.rect.left

		elif min_overlap == overlap_right:
			self.rect.left = entity.rect.right

		elif min_overlap == overlap_top:
			self.rect.bottom = entity.rect.top

		else:
			self.rect.top = entity.rect.bottom

	def draw_screen(self, screen: pygame.Surface):
		if self.is_visible:
			pygame.draw.rect(screen, self.color, self.rect)

	def update(self, world):
		pass
