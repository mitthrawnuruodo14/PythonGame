import pygame
from .window_manager import WindowManager

class Game:
	def __init__(self):
		self.is_running = False
		self.window_manager = WindowManager((800, 600))

	def setup(self):
		pygame.init()
		self.window_manager.setup()
	
	def update(self):
		pass
	
	def cleanup(self):
		pygame.quit()
