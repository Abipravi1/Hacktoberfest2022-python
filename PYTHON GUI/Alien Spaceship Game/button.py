import pygame.font

#making play button
class Button():
    def __init__(self,ai_settings,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #set dimensions and properties of the button
        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48) #none means import default font size=48px

        #build the button's rect object and center it
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #the button message need to be prepped only once
        self.prep_msg(msg)
    
    #turn message into rendered image and center it
    def prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    
    #draw blank rect then over it draw msg rect
    def draw_button(self):
        #to daw rectangle over screen we use fill
        self.screen.fill(self.button_color,self.rect)
        #to draw image over screen we use blit
        self.screen.blit(self.msg_image,self.msg_image_rect)
        


