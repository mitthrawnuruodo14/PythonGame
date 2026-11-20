import pygame #type: ignore
from gamefiles.settings import * #type: ignore
from gamefiles.entity import Entity
from gamefiles.controls import *

class Player(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(
            pos=pygame.Vector2(x, y),
            size=(60, 60),
            color=(255, 255, 255),
            has_collision=True,
            is_visible=True,
            z_index=0,
        )
        self.health = 100
        self.hit_indicator_duration = 0.125
        self.active_hit_indicator_duration = 0.0
        
    def update(self, world, inputs: list, delta_time):
        self.color = RED if self.active_hit_indicator_duration > 0.0 else WHITE

        self.active_hit_indicator_duration -= delta_time
        self.active_hit_indicator_duration = pygame.math.clamp(self.active_hit_indicator_duration, 0.0, self.hit_indicator_duration)

        if Input.D in inputs:
            self.pos.x += 200 * delta_time
        if Input.A in inputs:
            self.pos.x -= 200 * delta_time
        if Input.W in inputs:
            self.pos.y -= 200 * delta_time
        if Input.S in inputs:
            self.pos.y += 200 * delta_time

    def get_hit(self, damage: int):
        self.health -= damage
        self.active_hit_indicator_duration = self.hit_indicator_duration
