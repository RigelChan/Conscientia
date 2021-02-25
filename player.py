import pygame
from constants import Constants

class Player:
    def __init__(self):
        self.player_speed = 5
        self.constants = Constants()
        self.player_sprite = pygame.image.load("assets/player_temp.png")
        self.player_rect = self.player_sprite.get_rect()
        self.player_rect.x, self.player_rect.y = self.constants.screen_width/2, self.constants.screen_height/2

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self): # TODO RE-ADD DELTA TIME
        if self.moving_up:
            self.player_rect.y -= self.player_speed #* dt
        if self.moving_down:
            self.player_rect.y += self.player_speed #* dt
        if self.moving_right:
            self.player_rect.x += self.player_speed #* dt
        if self.moving_left:
            self.player_rect.x -= self.player_speed #* dt

    def draw(self, screen):
        screen.blit(self.player_sprite, self.player_rect)