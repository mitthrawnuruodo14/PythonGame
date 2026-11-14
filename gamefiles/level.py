import pygame #type: ignore
from gamefiles.settings import * #type: ignore

def create_rect_box(rect, rect_list, thickness):
    rect_list.append(pygame.Rect(rect.left, rect.top - thickness, rect.width, thickness))

    rect_list.append(pygame.Rect(rect.left, rect.bottom, rect.width, thickness))

    rect_list.append(pygame.Rect(rect.left - thickness, rect.top, thickness, rect.height))

    rect_list.append(pygame.Rect(rect.right, rect.top, thickness, rect.height))

class level():
    def __init__(self,screen,entities):
        self.x,self.y = screen.get_rect().center
        self.rect = pygame.Rect(self.x,self.y,1000,1000)
        self.color = (0,0,255)
        self.rect.center = screen.get_rect().center
        create_rect_box(self.rect, entities, 50)

    def draw_level(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)
