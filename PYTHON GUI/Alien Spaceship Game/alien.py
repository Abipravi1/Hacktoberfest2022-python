import pygame

from pygame.sprite import Sprite

#class to represent single alien
class Alien(Sprite):

    def __init__(self,ai_settings,screen):
        #initializing parent class as inherited as sprite
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #loading alien image and set its rect attribute
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #putting alien to top left having space equal to width and height as top space
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #store aliens exact position
        self.x=float(self.rect.x)

    #drawing alien on screen
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    #checking edges/return true if alien is at edge
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True


    
    #moving the alien left/right
    def update(self):
        self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x=self.x