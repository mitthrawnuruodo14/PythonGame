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
        self.hintergrund_leaderboard = Button(790,90,420,560,None,None)
        self.hintergrund_leaderboard.color = (30,30,30)

        leaderboard = read_leaderboard()
        self.leaderboard_buttons = []
        leaderboard_y = 100
        player_number = 1
        for punkte,name in leaderboard[:10]:
            text = f"{player_number}. {name} - {punkte}"
            btn = Button(800,leaderboard_y,400,45,text,22)
            btn.start_y = leaderboard_y  
            self.leaderboard_buttons.append(btn)
            leaderboard_y += 55
            player_number += 1

    def update(self, game_state,inputs):
        start_button_out = self.start_button.update_ui(inputs)
        end_button_out = self.end_button.update_ui(inputs)
        
        for btn in self.leaderboard_buttons:
            btn_out = btn.update_ui(inputs)
            if btn_out == 1:
                btn.color = GREEN
                btn.width = 420
                btn.pos.x = 790
                btn.height = 52.5
                btn.pos.y = btn.start_y  -5

            else:
                btn.color = RED
                btn.width = 400
                btn.pos.x = 800
                btn.height = 45
                btn.pos.y = btn.start_y
                

                

        #end Button
        if end_button_out == 1:
            self.end_button.color = GREEN
        else:
            self.end_button.color = RED
        if end_button_out == 2:
            pygame.quit()
        #start Button
        if start_button_out == 1:
            self.start_button.color = GREEN
        else:
            self.start_button.color = RED
        if start_button_out == 2:
            game_state =GameState.IN_LEVEL

        return game_state
        
    def draw(self,screen):
        screen.fill((0,0,100))
        self.start_button.draw_screen(screen)
        self.end_button.draw_screen(screen)
        self.hintergrund_leaderboard.draw_screen(screen)
        for btn in self.leaderboard_buttons:   
            btn.draw_screen(screen) 
       
    
