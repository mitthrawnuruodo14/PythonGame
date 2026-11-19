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

screen = pygame.display.set_mode(RESOLUTION,pygame.SCALED | pygame.FULLSCREEN) #type:ignore
clock = pygame.time.Clock()

camera = Camera(screen)

world = World(Player(0, 0))

world.entities.append(Zombie(50, 50))

menu = Menu(screen)

game_state = GameState.MENU
inputs: list = []

build_level(screen, world.entities)

world.update_draw_order()

is_game_running = True
while is_game_running:
	delta_time = clock.tick(60) / 1000.0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False
	print(f"deltatime: {delta_time}")
	get_inputs(inputs)
	
	
	if game_state == GameState.MENU:
		game_state = menu.update(game_state,inputs)
		menu.draw(screen) 

	elif game_state == GameState.IN_LEVEL:
		world.update_entities(inputs, delta_time)

		for entity in world.entities:
			if entity.has_collision:
				world.player.uncollide(entity)

		camera.update(world.player)

		screen.fill((30,30,30))

		world.draw_screen(camera, screen)
	
	pygame.display.flip()

pygame.quit()
