import pygame
import sys
from button import Button
from player import Player
from graphics import Graphics

class Scene:
    def __init__(self):
        pass
    def update(self):
        pass
    def enter(self):
        pass
    def exit(self):
        pass
    def input(self):
        pass
    def draw(self):
        pass

class MainMenu(Scene): 
    def __init__(self, game):
        self.screen = game.screen
        self.variables = game.variables
        self.constants = game.constants
        self.graphics = Graphics()

        self.play_button = Button(self.constants.screen_width/2-150, 250, 300, 100)
        self.settings_button = Button(self.constants.screen_width/2-150, 400, 300, 100)
        self.exit_button = Button(self.constants.screen_width/2-150, 550, 300, 100)
    
    def draw(self, dt):
        background_image = pygame.image.load(self.graphics.main_menu_image)
        self.screen.blit(background_image, (self.variables.mm_bg_pos,0))
        self.screen.blit(background_image, (self.variables.mm_bg_pos + 1280,0))

        self.variables.mm_bg_pos -= self.constants.mm_bg_speed * dt
        if self.variables.mm_bg_pos <= -1280:
            self.variables.mm_bg_pos = 0

        title_image = pygame.image.load(self.graphics.title).convert_alpha()
        self.screen.blit(title_image, (self.constants.screen_width/2-400 , 50))

        self.play_button_image = pygame.image.load(self.graphics.play).convert_alpha()
        self.en_play_button_image = pygame.image.load(self.graphics.en_play).convert_alpha()
        
        if self.variables.overPlay:
            self.screen.blit(self.en_play_button_image, (self.constants.screen_width/2-150, 250))
        else:
            self.screen.blit(self.play_button_image, (self.constants.screen_width/2-150, 250))

        self.settings_button_image = pygame.image.load(self.graphics.settings).convert_alpha()
        self.en_settings_button_image = pygame.image.load(self.graphics.en_settings).convert_alpha()

        if self.variables.overSettings:
            self.screen.blit(self.en_settings_button_image, (self.constants.screen_width/2-150, 400))
        else:
            self.screen.blit(self.settings_button_image, (self.constants.screen_width/2-150, 400))

        self.exit_button_image = pygame.image.load(self.graphics.exit).convert_alpha()
        self.en_exit_button_image = pygame.image.load(self.graphics.en_exit).convert_alpha()

        if self.variables.overExit:
            self.screen.blit(self.en_exit_button_image, (self.constants.screen_width/2-150, 550))
        else:
            self.screen.blit(self.exit_button_image, (self.constants.screen_width/2-150, 550))

    def mouse_menu_movement(self, event):
        pos = pygame.mouse.get_pos()
        if self.variables.inMenu:
            if self.play_button.isOver(pos):
                self.variables.overPlay = True
            else:
                self.variables.overPlay = False
            if self.settings_button.isOver(pos):
                self.variables.overSettings = True
            else:
                self.variables.overSettings = False
            if self.exit_button.isOver(pos):
                self.variables.overExit = True
            else:
                self.variables.overExit = False

    def mouse_menu_input(self, event):
        self.variables.clicking = True
        if self.variables.inMenu:
            if self.variables.overPlay:
                self.variables.inMenu = False
                self.variables.inGame = True
            if self.variables.overExit:
                sys.exit(0)


class TestLevel(Scene): 
    def __init__(self, game):
        self.variables = game.variables
        self.constants = game.constants
        self.graphics = Graphics()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.player = Player()
        

    def draw(self):
        temp_bg = pygame.image.load(self.graphics.test_bg).convert_alpha()
        self.screen.blit(temp_bg, (0, 0))
        self.player.draw(self.screen)

    def update(self, dt):
        self.player.update(dt)

class TransitionScence(Scene): # TODO
    def __init__(self):
        pass

class FadeTransitionScene(TransitionScence): # TODO
    def __init__(self):
        pass