import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__() #or super().__init__()

        self.screen=screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #store bullet position as decimal value
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
    
    def update(self):
        #move the bullets up the screen
        self.y-=self.speed_factor
        #maintaining the x cordinate only y cordinate of bullet changes
        self.rect.y=self.y

    #drawing bullet on screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
