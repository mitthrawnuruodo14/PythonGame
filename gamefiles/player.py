import pygame #type: ignore

#Working on the playre class and Testing it in the main.py file
class player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,50,100)

    def move(self):
        if pygame.key.get_pressed()[pygame.K_d]:
            self.rect.x -= 5 
    def draw(self,screen):
        pygame.draw.rect(screen,(255,0,0),self.rect)
        
    
