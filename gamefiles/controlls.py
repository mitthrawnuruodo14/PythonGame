import pygame


def get_inputs(inputs):
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    inputs.append(mouse_pos)
    if keys[pygame.K_s]:
        inputs.append(4)
    if keys[pygame.K_w]:
        inputs.append(3)
    if keys[pygame.K_d]:
        inputs.append(1)
    if keys[pygame.K_a]:
        inputs.append(2)
    if keys[pygame.K_BACKSPACE]:
        inputs.append(5)
    if mouse[0]:
        inputs.append(30)
    if mouse[2]:
        inputs.append(40)

    else:
        pass
    