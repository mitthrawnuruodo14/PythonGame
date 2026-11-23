import math
import random
from copy import copy
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
from gamefiles.leaderboard import *

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

enemies = [
	Zombie(50, 50),
	Skeleton(700, 500),
	Splitter(-50, -400, 100, 3, 40),
	Rammer(600, 200)
]

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

		if time_passed - last_spawned_enemy_timestamp > get_spawn_interval(time_passed):
			enemy = copy(random.choice(enemies))
			enemy_pos = world.player.pos
			while (enemy_pos - world.player.pos).length() < 800:
				enemy_pos = pygame.Vector2(random.randint(-710, 700), random.randint(-710, 700))
			enemy.pos = enemy_pos
			world.entities.append(enemy)
			last_spawned_enemy_timestamp = time_passed

		world.update_entities(screen, inputs, delta_time)

		for entity in world.entities:
			if entity.has_collision:
				for _entity in world.entities:
					if entity.has_collision and _entity != entity and isinstance(_entity, Humanoid):
						_entity.uncollide(entity)
				world.player.uncollide(entity)

		camera.update(world.player)

		screen.fill((30,30,30))

		world.draw_screen(camera, screen)
	
	pygame.display.flip()

pygame.quit()
