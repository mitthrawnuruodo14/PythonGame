import pygame 
from gamefiles.settings import *
from gamefiles.controls import *
from gamefiles.game import GameState
from gamefiles.ui import *

class Menu():
    def __init__(self,screen):
        #hier wird der button einmalig erstellt
        self.start_button = Button(30,30,200,80)
        pass

    def update(self, game_state,inputs):
        start_button_out = self.start_button.update(inputs)
        if start_button_out == 1:
            game_state =GameState.IN_LEVEL
        return game_state
        
    def draw(self,screen):
        screen.fill((0,0,100))
        self.start_button.draw_screen(screen)
        #zeichnet die buttons und sprites
        #hier wird der Button und das sprite gezeichnet
    
