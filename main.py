import pygame #type: ignore
from gamefiles.settings import * #type: ignore
from gamefiles.player import * #type: ignore
from gamefiles.camera import Camera
from gamefiles.menu import *
from gamefiles.controlls import get_inputs

def create_rect_box(entity: Entity, entities: list, thickness: int):
    entities.append(Entity(
    	rect=pygame.Rect(entity.rect.left, entity.rect.top - thickness, entity.rect.width, thickness),
		color=(0, 0, 0),
		is_visible=False,
		has_collision=True,
    ))

    entities.append(Entity(
    	rect=pygame.Rect(entity.rect.left, entity.rect.bottom, entity.rect.width, thickness),
    	color = (0, 0, 0),
    	is_visible=False,
    	has_collision=True

	))

    entities.append(Entity(
		rect=pygame.Rect(entity.rect.left - thickness, entity.rect.top, thickness, entity.rect.height),
		color=(0, 0, 0),
		is_visible=False,
		has_collision=True,
    ))


    entities.append(Entity(
    	rect=pygame.Rect(entity.rect.right, entity.rect.top, thickness, entity.rect.height),
		color = (0, 0, 0),
		is_visible=False,
		has_collision=True,
    ))

def build_level(screen: pygame.Surface, entities: list):
		background = Entity(
			rect=pygame.Rect(-500,-500,1000,1000),
			color=(0, 0, 255),
			has_collision=False,
			is_visible=True,
		)
		entities.append(background)
		create_rect_box(background, entities, 50)

pygame.init()

screen = pygame.display.set_mode(RESOLUTION) #type:ignore
clock = pygame.time.Clock()

player = player(0,0) #type: ignore

camera = Camera(screen)

entities = []

game_state = "in_level"
inputs: list = []

build_level(screen, entities)

is_game_running = True
while is_game_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_running = False
	print("Game is running...")
	get_inputs(inputs)
	if game_state == "menu":
		pass

	elif game_state == "in_level":
		player.move(inputs) #type:ignore
		inputs.clear()

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
