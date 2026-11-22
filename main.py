import math
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
from gamefiles.enemies.skeleton import Skeleton
from gamefiles.enemies.splitter import Splitter
from gamefiles.enemies.rammer import Rammer

def get_spawn_interval(time_survived: float) -> float:
    initial_interval = 2.5
    min_interval = 0.4
    growth_factor = 0.02

    return min_interval + (initial_interval - min_interval) * math.exp(-growth_factor * time_survived)

screen = pygame.display.set_mode(RESOLUTION,pygame.SCALED | pygame.FULLSCREEN) #type:ignore
clock = pygame.time.Clock()

camera = Camera(screen)

world = World(Player(0, 0))

menu = Menu(screen)

game_state = GameState.MENU
inputs: list = []

build_level(screen, world.entities)

world.update_draw_order()

last_spawned_enemy_timestamp = 0
time_passed = 0
is_game_running = True
while is_game_running:
	delta_time = clock.tick(120) / 1000.0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False

	get_inputs(inputs)
	
	if game_state == GameState.MENU:
		game_state = menu.update(game_state,inputs)
		menu.draw(screen) 

	elif game_state == GameState.IN_LEVEL:
		time_passed += delta_time
		spawn_interval = get_spawn_interval(time_passed)
		print(spawn_interval)

		if time_passed - last_spawned_enemy_timestamp > spawn_interval:
			world.entities.append(Zombie(50, 50))
			last_spawned_enemy_timestamp = time_passed

		world.update_entities(screen, inputs, delta_time)

		for entity in world.entities:
			if entity.has_collision:
				world.player.uncollide(entity)

		camera.update(world.player)

		screen.fill((30,30,30))

		world.draw_screen(camera, screen)
	
	pygame.display.flip()

pygame.quit()
