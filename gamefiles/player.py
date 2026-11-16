import pygame #type: ignore
from gamefiles.settings import * #type: ignore
from gamefiles.entity import Entity
from gamefiles.controls import *

#Working on the playre class and Testing it in the main.py file
class player(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(
            rect=pygame.Rect(x, y, 100, 100),
            color=(255, 255, 255),
            has_collision=True,
            is_visible=True
        )
        
    def move(self, inputs: list):
        if Input.D in inputs:
            self.rect.centerx += 5
        if Input.A in inputs:
            self.rect.centerx -= 5
        if Input.W in inputs:
            self.rect.centery -= 5
        if Input.S in inputs:
            self.rect.centery += 5
