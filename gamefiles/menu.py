import pygame 
def menu(game_state,inputs,screen):
    mouse_pos = inputs[0]
    screen.fill((0,0,0))
    menu_button_1 = pygame.Rect(10,10,200,100)
    menu_button_1.center = screen.get_rect().center
    button_color = (30,30,30)
    
    if menu_button_1.collidepoint(mouse_pos):
        button_color = (255,255,255)
        
    
    if menu_button_1.collidepoint(mouse_pos)and 30 in inputs :
        print("Die Maus ist im Rechteck und die linke maustaste wird gedrückt")
        button_color = (255,0,0)

    pygame.draw.rect(screen,button_color,menu_button_1)
        

    return menu_button_1
