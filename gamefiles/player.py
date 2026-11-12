import pygame #type: ignore
from gamefiles.settings import * #type: ignore

#Working on the playre class and Testing it in the main.py file
class player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,50,100)
        self.velocity = 0
        self.one_ground = False  
        

    def move(self,):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5 
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_SPACE] and self.one_ground:
            self.velocity = -JUMP_HEIGHT #type: ignore
            self.one_ground = False
        self.velocity += GRAVITY #type: ignore
        self.rect.y += self.velocity


        if self.rect.bottom >= 550:
            self.rect.bottom = 550
            self.velocity = 0
            self.one_ground = True 
    
    def draw(self,screen):
        pygame.draw.rect(screen,(255,0,0),self.rect)
        
    