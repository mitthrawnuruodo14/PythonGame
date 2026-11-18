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
