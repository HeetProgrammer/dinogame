import pygame
import sys
from dinosaur import Dinosaur
from settings import Settings
from cactus import Cactus
from time import sleep
import random


class DinoRunner:
    def __init__(self):
        """ Initializes global game attributes"""
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.screen_width, self.screen_height = self.screen.get_size()
        self.framenum = 0
        self.is_gravity = True
        self.player = Dinosaur(self)
        self.cactii = pygame.sprite.Group()
        self.new_game()
        

    def check_events(self):
        """ Contains an event loop that responds to user events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def draw_cactii(self, n):
        for i in range(n):
            cactus = Cactus(self)
            cactus.rect.bottom = self.screen_rect.bottom - 100
            cactus.rect.left = self.screen_rect.right + random.randint(300, 500) * i
            self.cactii.add(cactus)

    def update_cactii(self):
        """ Updates cactii position """
        self.cactii.update()
        self.check_cactus_edges()
        self.check_cactus_dino_collisions()
    
    def check_cactus_dino_collisions(self):
        if pygame.sprite.spritecollideany(self.player, self.cactii):
            sleep(0.5)
            self.new_game()

    def check_cactus_edges(self):
        """ Checks if cactus is off the screen and draws new one"""
        for cactus in self.cactii.sprites():
            if cactus.rect.right <= 5:
                self.cactii.remove(cactus)
                self.draw_cactii(1)
    
    def new_game(self):
        """ Starts new game"""
        self.cactii.empty()
        self.draw_cactii(2)
        self.framenum = 0
        self.player.position_dino(self.framenum)
        self.is_gravity = True


    def check_keydown_events(self, event):
        """ Checks keypress events"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if self.player.bottom == self.screen_rect.bottom - 100:
                self.player.bottom += self.settings.jump_speed

    def check_in_air(self):
        """ Checks if dinosaur is in air"""
        if self.player.bottom == self.screen_rect.bottom - 100:
            self.is_gravity = False
        else:
            self.is_gravity = True
        if self.is_gravity:
            self.player.update_dino_pos()

    def run_game(self):
        """ Main loop"""
        while True:
            self.check_in_air()
            self.update_cactii()
            self.framenum += 1 % len(self.player.frame_group)
            self.check_events()
            self.update_screen()

    def draw_background(self):
        """ Draws the game background"""
        self.bg_image = pygame.image.load('background.jpg')
        self.bg_image_rect = self.bg_image.get_rect()
        self.bg_image_rect.midtop = self.screen_rect.midtop
        self.screen.blit(self.bg_image, self.bg_image_rect)

    def update_screen(self):
        """ Draws the screen on each pass through the loop """
        self.draw_background()
        if self.framenum >= len(self.player.frame_group) - 1:
            self.framenum = 0
        self.player.position_dino(self.framenum)
        self.player.draw_dino()
        for cactus in self.cactii:
            cactus.draw_image()
        pygame.display.flip()


if __name__ == '__main__':
    ob = DinoRunner()
    ob.run_game()
