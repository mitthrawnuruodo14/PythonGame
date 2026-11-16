from gamefiles.entity import Entity
import pygame

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
