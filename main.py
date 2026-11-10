import pygame

pygame.init()

RESOLUTION = WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode(RESOLUTION)

is_game_running = True
while is_game_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False
	print("Game is running...")

pygame.quit()
