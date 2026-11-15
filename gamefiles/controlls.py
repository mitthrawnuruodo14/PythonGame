import pygame


def get_inputs(inputs):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        inputs.append(4)
    if keys[pygame.K_w]:
        inputs.append(3)
    if keys[pygame.K_d]:
            inputs.append(1)
    if keys[pygame.K_a]:
            inputs.append(2)