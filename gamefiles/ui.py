import pygame
from gamefiles.settings import *
from gamefiles.entity import *
from gamefiles.controls import *

class Button(Entity):
    def __init__(self,x,y,width,height,text="",text_size =30,text_color=WHITE):
        text_surf = None
        if text != "":
             font =pygame.font.SysFont("Arial",text_size)
             text_surf = font.render(text,True,text_color)
        self.base_width = width
        self.base_height = height
        self.base_x = x
        self.base_y = y
        
        
        super().__init__(
            pos=pygame.Vector2(x, y),
            size=(width, height),
            color= RED,
            has_collision = False,
            is_visible = True,
            z_index=0,
            surface= text_surf
        )

    def update_ui(self, inputs):
        mouse_pos = inputs[Input.MOUSE_POS_IDX]
        if self.get_rect().collidepoint(mouse_pos) and Input.MOUSE_LEFT in inputs:
            return 2
        if self.get_rect().collidepoint(mouse_pos):
            return 1
       
            
        
        
