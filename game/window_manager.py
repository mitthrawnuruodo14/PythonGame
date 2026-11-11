import pygame

class WindowManager:
	def __init__(self, resolution):
		self.resolution = resolution
		self.screen = None

	def setup(self):
		self.screen = pygame.display.set_mode((800, 600))
