import pygame #type: ignore
from gamefiles.settings import *
from gamefiles.player import *
pygame.init()


screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

#Temporary player object for testing
player = player(100, 200)

is_game_running = True
while is_game_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False
	print("Game is running...")
	#Testing the player class and its movements this is temporary and will be moved later
	player.move()

	screen.fill((30,30,30))
	player.draw(screen)


	pygame.display.flip()
	clock.tick(60)

pygame.quit()
