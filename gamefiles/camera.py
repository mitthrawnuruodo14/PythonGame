from gamefiles.entity import Entity
import pygame

class Camera():
    def __init__(self, screen: pygame.Surface):
        self.offset_x = 0
        self.offset_y = 0
        self.screen = screen

    def update(self, entity: Entity):
        self.offset_x = entity.get_rect().centerx - self.screen.get_width() // 2
        self.offset_y = entity.get_rect().centery - self.screen.get_height() // 2

    def apply(self, entity: Entity):
        return Entity(
            pos=pygame.Vector2(entity.pos.x - self.offset_x, entity.pos.y - self.offset_y),
            size=(entity.width, entity.height),
            has_collision=entity.has_collision,
            is_visible=entity.is_visible,
            color=entity.color,
            z_index=entity.z_index,
        )
