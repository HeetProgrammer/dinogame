import pygame


class Cactus(pygame.sprite.Sprite):
    def __init__(self, ob):
        super().__init__()
        self.screen = ob.screen
        self.screen_rect = ob.screen.get_rect()
        self.settings = ob.settings
        self.image = pygame.image.load('cactus.png')
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= self.settings.cactus_speed

    def draw_image(self):
        self.screen.blit(self.image, self.rect)
