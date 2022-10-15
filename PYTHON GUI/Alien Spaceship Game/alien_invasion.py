import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    #initializes bg settings that pygame needs to start
    pygame.init() 
    #initializing setting class by making object
    ai_settings=Settings()
    #takes a tuple to set the dimension of game window 
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) 
    #sets the title to the game window 
    pygame.display.set_caption("Alien Invasion") 
    #make the play button
    play_button=Button(ai_settings,screen,"Play")
    #instance to store game stats and create scoreboard
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    #making ship object
    ship=Ship(ai_settings,screen)

    #making alien group
    aliens=Group()

    #make group to store bullets thats why sprite module is used
    bullets=Group()

    #making alien fleet
    gf.create_fleet(ai_settings,screen,ship,aliens)

    
    #start main loop for the game
    while True:
        #checking mouse and key pressess
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        #checking when to continue the game
        if stats.game_active:
            #updating ship position
            ship.update()
            #updating bullet position
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            #updating alien position
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
            
        
        #updating screen with image and flip to new screen
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)  


        

run_game()