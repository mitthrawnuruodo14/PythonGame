import pygame #type: ignore
from gamefiles.settings import * #type: ignore
from gamefiles.entity import Entity

#Working on the playre class and Testing it in the main.py file
class player(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(
            rect=pygame.Rect(x, y, 100, 100),
            color=(255, 255, 255),
            has_collision=True,
            is_visible=True
        )
        
    def move(self,inputs:list[int]):
        if  1 in inputs :
            self.rect.centerx += 5
        if 2 in inputs :
            self.rect.centerx -= 5
        if 3 in inputs:
            self.rect.centery -= 5
        if 4 in inputs:
            self.rect.centery += 5
        else:
            pass
