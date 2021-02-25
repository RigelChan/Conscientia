import pygame
import sys
import time
import os
import scene as s
from graphics import Graphics
from constants import Constants
from variables import Variables

class Game: # The Main Game Class.
    def __init__(self):
        pygame.init()
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=312)

        self.constants = Constants()
        self.variables = Variables()
        self.graphics = Graphics()

        self.screen = pygame.display.set_mode((self.constants.screen_width, self.constants.screen_height))
        pygame.display.set_caption("Conscientia")
        pygame.display.set_icon(pygame.image.load(self.graphics.icon))
        pygame.mouse.set_visible(False)
        
        self.fps = 75
        self.clock = pygame.time.Clock() # Clock.
        self.last_time = time.time()

        # Mouse variables.
        self.variables.clicking = False

        # Menu.
        self.main_menu = s.MainMenu(self)

        # Test Level.
        self.test_level = s.TestLevel(self)

    # Basic Game Logic =======================================================================

    def delta_time(self):
        self.dt = time.time() - self.last_time
        self.dt *= 75
        self.last_time = time.time()

    def draw_cursor(self):
        self.cursor = pygame.image.load(self.graphics.cursor).convert_alpha()
        self.screen.blit(self.cursor, (pygame.mouse.get_pos()[0]-15, pygame.mouse.get_pos()[1]-15))

    def update_screen(self): # Updates the screen each frame.
        if self.variables.inMenu:
            self.main_menu.draw(self.dt)
        if self.variables.inGame:
            self.test_level.draw()
        self.draw_cursor()
        pygame.display.update()

    def check_events(self): # Checks for input events.
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit(0)

            elif event.type == pygame.KEYDOWN:
                self.keyboard_input_d(event)

            elif event.type == pygame.KEYUP:
                self.keyboard_input_u(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_input(event)

            elif event.type == pygame.MOUSEBUTTONUP:
                self.variables.clicking = False

            elif event.type == pygame.MOUSEMOTION:
                self.mouse_movement(event)
                
    def keyboard_input_d(self, event):
        if event.key == pygame.K_PERIOD:
            self.constants.fps_target = 10
        elif event.key == pygame.K_w:
            self.test_level.player.moving_up = True
        elif event.key == pygame.K_s:
            self.test_level.player.moving_down = True
        elif event.key == pygame.K_d:
            self.test_level.player.moving_right = True
        elif event.key == pygame.K_a:
            self.test_level.player.moving_left = True
        elif event.key == pygame.K_g:
            print("unused key")

    def keyboard_input_u(self, event):
        if event.key == pygame.K_w:
            self.test_level.player.moving_up = False
        elif event.key == pygame.K_s:
            self.test_level.player.moving_down = False
        elif event.key == pygame.K_d:
            self.test_level.player.moving_right = False
        elif event.key == pygame.K_a:
            self.test_level.player.moving_left = False

    def mouse_movement(self, event):
        self.main_menu.mouse_menu_movement(event)

    def mouse_input(self, event):
        self.main_menu.mouse_menu_input(event)

    def run_game(self): # Runs the main game functions.
        while True:
            self.delta_time()
            self.check_events()
            self.test_level.update(self.dt)
            self.update_screen()
            self.clock.tick(self.constants.fps_target)

if __name__ == "__main__":
    game = Game()
    game.run_game()
    