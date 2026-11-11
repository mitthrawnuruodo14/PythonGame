import pygame
from gamefiles import settings
pygame.init()


screen = pygame.display.set_mode(settings.RESOLUTION)

is_game_running = True
while is_game_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False
	print("Game is running...")

pygame.quit()
