import pygame #type: ignore
from gamefiles.settings import * #type: ignore
from .entity import Entity

#Working on the playre class and Testing it in the main.py file
class player(Entity):
    def __init__(self,x,y):
        super().__init__(
            rect=pygame.Rect(x, y, 100, 100),
            color=(255, 255, 255),
            has_collision=True,
            is_visible=True
        )
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.centerx -= 5
        if keys[pygame.K_a]:
            self.rect.centerx += 5
        if keys[pygame.K_w]:
            self.rect.centery += 5
        if keys[pygame.K_s]:
            self.rect.centery -= 5
