import pygame #type: ignore
from gamefiles.settings import * #type: ignore
from gamefiles.player import * #type: ignore
from gamefiles.camera import Camera
from gamefiles.menu import *
from gamefiles.controls import *
from gamefiles.level import *
from gamefiles.game import GameState

pygame.init()

screen = pygame.display.set_mode(RESOLUTION) #type:ignore
clock = pygame.time.Clock()

player = player(0, 0) #type: ignore

camera = Camera(screen)

entities = []

game_state = GameState.MENU
inputs: list = []

build_level(screen, entities)

is_game_running = True
while is_game_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False
	print("Game is running...")
	get_inputs(inputs)
	
	if game_state == GameState.MENU:
		game_state_container = [GameState.MENU]
		menu(game_state_container, inputs, screen)
		game_state = game_state_container[0]

	elif game_state == GameState.IN_LEVEL:
		player.move(inputs) #type:ignore

		for entity in entities:
			if entity.has_collision:
				player.uncollide(entity)

		camera.update(player)

		screen.fill((30,30,30))
		#drawing the level and the player
		for entity in entities:
			camera.apply(entity).draw_screen(screen)
		camera.apply(player).draw_screen(screen)
	
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
