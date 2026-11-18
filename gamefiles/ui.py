import pygame
from gamefiles.settings import *
from gamefiles.entity import *
from gamefiles.controls import *

class Button(Entity):
    def __init__(self,x,y,width,height):
        super().__init__(
            rect=pygame.Rect(x,y,width,height),
            color= RED,
            has_collision = False,
            is_visible = True,
            z_index=0
        )

    def update_ui(self, inputs):
        mouse_pos = inputs[Input.MOUSE_POS_IDX]
        if self.rect.collidepoint(mouse_pos):
            self.color = GREEN
            if Input.MOUSE_LEFT in inputs:
                self.color = WHITE
                return 1
            else:
                 return 0
        else:
                self.color = RED
                return 0
        
