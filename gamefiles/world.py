import pygame
from gamefiles.camera import Camera

class World():
	def __init__(self, player):
		self.entities = []
		self.player = player

	def draw_screen(self, camera: Camera, screen: pygame.Surface):
		for entity in self.entities:
			camera.apply(entity).draw_screen(screen)
		camera.apply(self.player).draw_screen(screen)
	
	def update_entities(self, inputs, delta_time):
		self.player.update(self, inputs, delta_time)
		for entity in self.entities:
			entity.update(self, inputs, delta_time)

	def update_draw_order(self):
		self.entities.sort(key=lambda entity: entity.z_index)
