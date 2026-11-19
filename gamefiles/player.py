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
        
    def move(self, inputs: list):
        if Input.D in inputs:
            self.pos.x += 3
        if Input.A in inputs:
            self.pos.x -= 3
        if Input.W in inputs:
            self.pos.y -= 3
        if Input.S in inputs:
            self.pos.y += 3
