from enum import IntEnum
import pygame

class Input(IntEnum):
    D = 1
    A = 2
    W = 3
    S = 4
    BACKSPACE = 5
    MOUSE_LEFT = 30
    MOUSE_RIGHT = 40
    MOUSE_POS_IDX = 0

def get_inputs(inputs):
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    inputs.append(mouse_pos)
    if keys[pygame.K_s]:
        inputs.append(Input.S)
    if keys[pygame.K_w]:
        inputs.append(Input.W)
    if keys[pygame.K_d]:
        inputs.append(Input.D)
    if keys[pygame.K_a]:
        inputs.append(Input.A)
    if keys[pygame.K_BACKSPACE]:
        inputs.append(Input.BACKSPACE)
    if mouse[0]:
        inputs.append(Input.MOUSE_LEFT)
    if mouse[2]:
        inputs.append(Input.MOUSE_RIGHT)
