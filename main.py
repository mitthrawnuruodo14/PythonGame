import pygame #type: ignore
from gamefiles.settings import * #type: ignore
from gamefiles.player import * #type: ignore
from gamefiles.level import * #type:ignore
pygame.init()


screen = pygame.display.set_mode(RESOLUTION) #type:ignore
clock = pygame.time.Clock()

#Temporary player object for testing
player = player(100, 200) #type: ignore

#Temporary pos from map for testing
level = level() #type: ignore

is_game_running = True
while is_game_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False
	print("Game is running...")
	#Testing the player class and its movements this is temporary and will be moved later
	player.move(GROUND) #type:ignore

	screen.fill((30,30,30))
	#drawing the level and the player
	level.draw_level(screen)
	player.draw_player(screen)
	


	pygame.display.flip()
	clock.tick(60)

pygame.quit()
