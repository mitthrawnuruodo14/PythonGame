import pygame #type: ignore
from gamefiles.settings import * #type: ignore

class level():
    def __init__(self,screen):
        self.x,self.y = screen.get_rect().center
        self.rect = pygame.Rect(self.x,self.y,1000,1000)
        self.color = (0,0,255)
        self.rect.center = screen.get_rect().center


    def draw_level(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)