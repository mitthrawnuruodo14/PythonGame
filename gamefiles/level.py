import pygame #type: ignore
from gamefiles.settings import * #type: ignore

class level():
    def __init__(self):
        self.rect = pygame.Rect(5,5,2000,500)
        self.color = (0,0,255)


    def draw_level(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)