import pygame #type: ignore
from gamefiles.settings import * #type: ignore

#Working on the playre class and Testing it in the main.py file
class player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,50,100)
        self.velocity = 0
        self.on_ground = False  
        

    def move(self,GROUND):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5 
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity = -JUMP_HEIGHT #type: ignore
            self.on_ground = False
        self.velocity += GRAVITY #type: ignore
        self.rect.y += self.velocity


        if self.rect.bottom >= GROUND:
            self.rect.bottom = GROUND
            self.velocity = 0
            self.on_ground = True 

    def uncollide(self, rect):
        if not self.rect.colliderect(rect):
            return

        overlap_left = self.rect.right - rect.left
        overlap_right = rect.right - self.rect.left
        overlap_top = self.rect.bottom - rect.top
        overlap_bottom = rect.bottom - self.rect.top

        min_overlap = min(
            overlap_left,
            overlap_right,
            overlap_top,
            overlap_bottom
        )

        if min_overlap == overlap_left:
            self.rect.right = rect.left

        elif min_overlap == overlap_right:
            self.rect.left = rect.right

        elif min_overlap == overlap_top:
            self.rect.bottom = rect.top

        else:
            self.rect.top = rect.bottom
    
    def draw_player(self,screen):
        pygame.draw.rect(screen,(255,0,0),self.rect)
        
    
