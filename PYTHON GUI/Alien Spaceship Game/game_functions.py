import pygame
import sys
from time import sleep
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings,screen,ship,bullets):
    #if bullet not reached the limit create new bullet and add to bullets group
    if len(bullets)<ai_settings.bullets_allowed:
        #Create a new bullet and add it to the bullets group.
        new_Bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_Bullet)

#check key presses
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #checking pressing of left and right arrow key
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    #checking pressing of spacebar
    elif event.key==pygame.K_SPACE:
        #fire bullet when press spacebar
        fire_bullet(ai_settings,screen,ship,bullets)
    
    

#check key releases
def check_keyup_events(event,ship):
    #checking release of right and left arrow key
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

#check mouse and gey presses
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    for event in pygame.event.get():
        #exiting the game
        if event.type==pygame.QUIT:
            sys.exit()
        #left right movement of ship
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
            
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        #check pressing of play button
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

#check play button is pressed or not
#start a new game when player clicks play button
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #reset game settings
        ai_settings.initialize_dynamic_settings()
        #hide the mouse cursor when playing starts
        pygame.mouse.set_visible(False)
        #reset the game stats
        stats.reset_stats()
        stats.game_active=True  

        #reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level() 
        sb.prep_ships()

        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create a new fleet and center the ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        

#update image to the screen and flip to new screen
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    #redraw the screen during each pass of while loop
    screen.fill(ai_settings.bg_color)
    #redrawing all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #drawing ship after every iteration of fill
    ship.blitme()
    #draw() is called and inbuilt function, pygame automatically draws alien on screen
    aliens.draw(screen)

    #draw the scoreboard
    sb.show_score()

    #draw play button when game is inactive
    if not stats.game_active:
        play_button.draw_button()
    
    #refreshes the game screen and erases the old screen
    pygame.display.flip()

#updating bullets and removing disappeared bullets from group
#destroyig bullets and aliens when collide
def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
    #removing disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    
    #check collision of alien bullets and create new fleet
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)
    

    
#checking bullet alien collision
def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #group collide runs aloop inside and check or collision bw two groups
    #it runs loop for each alien checking for eah bullet
    #the first 'true' parameter tells to destroy bullet when collide
    #the second 'true' parameter tells to destroy aliens when collide
    #groupcollide() addskey value pair to dictionary whenever bullets and aliens rect overlap
    #return key value pairs dictionary of aliens hit by single bullet
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score+=ai_settings.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
        

    #when the alien fleet destroyed reload the bullets,speed up the game,increse level and create new fleet
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()

        #increase speed
        stats.level+=1
        sb.prep_level()
    
        create_fleet(ai_settings,screen,ship,aliens)

#checking high score
def check_high_score(stats,sb):
    """check to see if there's a new high score"""
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()

#get number of aliens in a row
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x

#get number of rows of fleet initially
def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y=ai_settings.screen_height-(4*alien_height)-ship_height
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows


#create an alien object
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien=Alien(ai_settings,screen)
    #setting x cordinate of alien
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    #adding alien to aliens group
    aliens.add(alien)

#fuction to create alien fleet
def create_fleet(ai_settings,screen,ship,aliens):

    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
    
    
    

#respond appropriately if any alien reached edge
def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

#drop the entire fleet and change fleets direction
def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1

#when ship is hit by aliens reduce ship count by one and reload everything
def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    if stats.ships_left>0:
        #decrement ship count by 1
        stats.ships_left-=1

        #update scoreboard
        sb.prep_ships()

        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create a new fleet and center the ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
        #pause
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)



#check if aliens reached bottom, if yes the destroy the ship and create new one
def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            #same as when ship got hit
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break



#Check if the fleet is at an edge,and then update the postions of all aliens in the fleet.
def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #checking alien ship collision
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
    
    #look for alien hitting bottom of the screen
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)
    
