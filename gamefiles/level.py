from gamefiles.entity import Entity
import pygame

def create_rect_box(entity: Entity, entities: list, thickness: int):
    entities.append(Entity(
    	pos=pygame.Vector2(entity.pos.x, entity.pos.y - thickness),
		size=(entity.width, thickness),
		color=(0, 0, 0),
		is_visible=False,
		has_collision=True,
		z_index=0,
    ))

    entities.append(Entity(
    	pos=pygame.Vector2(entity.pos.x, entity.pos.y + entity.height),
    	size=(entity.width, thickness),
    	color = (0, 0, 0),
    	is_visible=False,
    	has_collision=True,
		z_index=0,
	))

    entities.append(Entity(
		pos=pygame.Vector2(entity.pos.x - thickness, entity.pos.y),
		size=(thickness, entity.height),
		color=(0, 0, 0),
		is_visible=False,
		has_collision=True,
		z_index=0,
    ))

    entities.append(Entity(
    	pos=pygame.Vector2(entity.pos.x + entity.width, entity.pos.y),
    	size=(thickness, entity.height),
		color=(0, 0, 0),
		is_visible=False,
		has_collision=True,
		z_index=0,
    ))

def build_level(screen: pygame.Surface, entities: list):
		background = Entity(
			pos=pygame.Vector2(-50, -500),
			size=(1000, 1000),
			color=(0, 0, 255),
			has_collision=False,
			is_visible=True,
			z_index=-1,
		)
		entities.append(background)
		create_rect_box(background, entities, 50)
