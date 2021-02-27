import pygame
import time
import sys
import os
import scene as s
from graphics import Graphics
from constants import Constants
from variables import Variables

class Game: # The Main Game Class.
    def __init__(self):
        pygame.init()
        pygame.mixer.pre_init(frequency=44100, size=16, channels=2, buffer=312)

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

        # Scene objects.
        self.main_menu = s.MainMenu(self)
        self.sm = s.SceneManager()
        self.sm.push(self.main_menu)

    # Basic Game Logic =======================================================================

    def delta_time(self):
        self.dt = time.time() - self.last_time
        self.dt *= 75
        self.last_time = time.time()

    def draw_cursor(self):
        self.cursor = pygame.image.load(self.graphics.cursor).convert_alpha()
        self.screen.blit(self.cursor, (pygame.mouse.get_pos()[0]-15, pygame.mouse.get_pos()[1]-15))

    def update_screen(self): # Updates the screen each frame.
        self.sm.draw()
        self.draw_cursor()
        pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            self.quit(event)
            self.sm.input(event)

    def quit(self, event):
        if event.type == pygame.QUIT:
                sys.exit(0)

    def test_dt(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PERIOD:
                self.constants.fps_target = 10

    def keyboard_input_d(self, event):
        self.test_dt(event)

    def run_game(self): # Runs the main game functions.
        while True:
            self.delta_time()
            self.check_events()
            self.update_screen()
            self.clock.tick(self.constants.fps_target)

if __name__ == "__main__":
    game = Game()
    game.run_game()
    