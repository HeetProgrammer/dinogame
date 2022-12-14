import pygame


class Dinosaur:
    def __init__(self, ob):
        self.screen = ob.screen
        self.screen_rect = ob.screen_rect
        self.settings = ob.settings
        self.x = 100
        self.bottom = self.screen_rect.bottom - 100
        self.frame_group = [f'frame{i}.gif' for i in range(1, 21)]
   
    def position_dino(self, framenum):
        self.image = pygame.image.load(self.frame_group[framenum])
        self.rect = self.image.get_rect()
        self.rect.bottom = self.bottom
        self.rect.x = self.x

    def draw_dino(self):
        self.screen.blit(self.image, self.rect)
    
    def update_dino_pos(self):
        if self.bottom != self.screen_rect.bottom - 100:
            self.bottom += self.settings.gravity