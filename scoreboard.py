import pygame
class Scoreboard():
    def __init__(self, ob):
        pygame.init()
        self.screen = ob.screen
        self.screen_rect = ob.screen.get_rect()
        self.settings = ob.settings
        self.font = pygame.font.SysFont(None, 50)
        self.colour = (60, 60, 60)
    
    def prep_score(self, score):
        score_str = str(score)
        self.image = self.font.render(score_str, True, self.colour)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (100, 100)
    
    def draw_score(self):
        self.screen.blit(self.image, self.image_rect)
        