import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        #initialize the ship and set its starting position
        super(Ship,self).__init__()
        self.screen=screen

        #load ship image ang get rect() of screen and ship image
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #position the ship at bottom center os game window
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.ai_settings=ai_settings
        #store decimal value of ship's center
        self.center=float(self.rect.centerx)

        #movement flags
        self.moving_right=False
        self.moving_left=False

    #updating ship position on movement flag
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed_factor

        #update rect object from self.center
        self.rect.centerx=self.center
    
    #center the ship when new ship reloads
    def center_ship(self):
        self.center=self.screen_rect.centerx
        
    #drawing the ship at given location
    def blitme(self):
        #providing position and image for ship to display
        self.screen.blit(self.image,self.rect)


