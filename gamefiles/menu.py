import pygame 
from gamefiles.settings import *
def menu(game_state,inputs,screen):
    
    text_color_1 = WHITE
    
    mouse_pos = inputs[0]
    screen.fill((0,0,0))
    menu_button_1 = pygame.Rect(10,10,200,100)
    menu_button_1.center = screen.get_rect().center
    menu_button_1.y = menu_button_1.y + 180
    
    button_color = GREY
    
    if menu_button_1.collidepoint(mouse_pos):
        button_color = WHITE
        text_color_1 = RED

        
    
    if menu_button_1.collidepoint(mouse_pos)and 30 in inputs :
        print("Die Maus ist im Rechteck und die linke maustaste wird gedrückt")
        button_color = RED
        text_color_1 = WHITE

    text_surface = FONT_36.render("Start",True,(text_color_1))
    text_rect = text_surface.get_rect(center= menu_button_1.center)

    pygame.draw.rect(screen,button_color,menu_button_1)
    screen.blit(text_surface,text_rect)
        

    return menu_button_1
