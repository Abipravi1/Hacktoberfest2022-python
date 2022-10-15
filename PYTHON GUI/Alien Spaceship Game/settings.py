class Settings():
    #setting to store the settings of alien invasion
    def __init__(self):
        """initializes games static settings"""
        #screen settings
        self.screen_height=700
        self.screen_width=1200
        self.bg_color=(230,230,230)

        #ship settings
        self.ship_limit=3

        #bullet settings
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=10

        #alien settings
        self.fleet_drop_speed=10
        
        #how quickly the game speed up
        self.speedup_scale=1.1
        #how quickly the alien points value increase
        self.score_scale=1.5

        self.initialize_dynamic_settings()

    """initialize dynamic settings of game"""
    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.fleet_direction=1 #1=right,-1=left
        #scoring
        self.alien_points=50
       
     #increse alien speed and point scale   
    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
