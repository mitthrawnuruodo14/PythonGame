import pygame #type: ignore
from gamefiles.world import World
from gamefiles.settings import * #type: ignore
from gamefiles.player import * #type: ignore
from gamefiles.camera import Camera
from gamefiles.menu import *
from gamefiles.controls import *
from gamefiles.level import *
from gamefiles.game import GameState
from gamefiles.enemy import Enemy
from gamefiles.enemies.zombie import Zombie

screen = pygame.display.set_mode(RESOLUTION) #type:ignore
clock = pygame.time.Clock()

camera = Camera(screen)

world = World(Player(0, 0))

world.entities.append(Zombie(50, 50))

game_state = GameState.MENU
inputs: list = []

build_level(screen, world.entities)

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
		world.player.move(inputs) #type:ignore

		for entity in world.entities:
			if entity.has_collision:
				world.player.uncollide(entity)

		world.update_entities()

		camera.update(world.player)

		screen.fill((30,30,30))

		world.draw_screen(camera, screen)
	
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
