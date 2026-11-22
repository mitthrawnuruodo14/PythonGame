import pygame 
from gamefiles.settings import *
from gamefiles.controls import *
from gamefiles.game import GameState
from gamefiles.ui import *
from gamefiles.leaderboard import *

class Menu():
    def __init__(self,screen):

  
        self.start_button = Button(30,30,200,80,"Start",35)
        self.end_button = Button(30,600,200,80,"Beenden",30)

        leaderboard = read_leaderboard()
        self.leaderboard_buttons = []
        leaderboard_y = 100
        player_number = 1
        for punkte,name in leaderboard:
            text = f"{player_number}. {name} - {punkte}"
            btn = Button(800,leaderboard_y,400,45,text,22)
            self.leaderboard_buttons.append(btn)
            leaderboard_y += 55
            player_number += 1

    def update(self, game_state,inputs):
        start_button_out = self.start_button.update_ui(inputs)
        end_button_out = self.end_button.update_ui(inputs)
        if end_button_out == 1:
            pygame.quit()
        if start_button_out == 1:
            game_state =GameState.IN_LEVEL
        return game_state
        
    def draw(self,screen):
        screen.fill((0,0,100))
        self.start_button.draw_screen(screen)
        self.end_button.draw_screen(screen)
        for btn in self.leaderboard_buttons:   # <--- Steht das drin?
            btn.draw_screen(screen) 
       
    
