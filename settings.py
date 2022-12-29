class Settings:
    def __init__(self):
        """ Initializes game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.gravity = 5
        self.jump_speed = -120
           
    def reset_dynamic_settings(self):
        self.cactus_speed = 10
        self.difficulty_limit = [300, 500]


