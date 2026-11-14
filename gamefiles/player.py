import pygame #type: ignore
from gamefiles.settings import * #type: ignore

#Working on the playre class and Testing it in the main.py file
class player():
    def __init__(self,x,y,screen):
        self.x ,self.y= x,y
        self.rect = pygame.Rect(self.x,self.y,100,100)
        self.rect.center = screen.get_rect() .center       
        
        

    def move(self,map):
        old_x , old_y = map.rect.x , map.rect.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            map.rect.x -= 5 
        if keys[pygame.K_a]:
            map.rect.x += 5
        if keys[pygame.K_w]:
            map.rect.y += 5
        if keys[pygame.K_s]:
            map.rect.y -= 5
        if map.rect.contains(self.rect) == False:
            map.rect.x, map.rect.y = old_x,old_y


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
        
    
