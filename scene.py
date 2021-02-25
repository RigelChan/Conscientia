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
    
    def draw(self):
        background_image = pygame.image.load(self.graphics.main_menu_image)
        self.screen.blit(background_image, (self.variables.mm_bg_pos,0))
        self.screen.blit(background_image, (self.variables.mm_bg_pos + 1280,0))

        self.variables.mm_bg_pos -= self.constants.mm_bg_speed # TODO ADD DELTA TIME.
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

    def mouse_menu_input(self, event, sm):
        self.variables.clicking = True
        if self.variables.overPlay:
            sm.push(TestLevel(self))
        if self.variables.overExit:
            sys.exit(0)

    def input(self, event, sm):
        self.mouse_menu_movement(event)
        self.mouse_menu_input(event, sm)

    def exit(self):
        print("Leaving main menu.")

    def enter(self):
        print("Entering main menu.")

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

    def update(self): # TODO RE-ADD DELTA TIME.
        self.player.update()

    def player_key_down(self, event):
        if event.key == pygame.K_w:
            self.player.moving_up = True
        elif event.key == pygame.K_s:
            self.player.moving_down = True
        elif event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_g:
            print("unused key")

    def player_key_up(self, event):
        if event.key == pygame.K_w:
            self.player.moving_up = False
        elif event.key == pygame.K_s:
            self.player.moving_down = False
        elif event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_a:
            self.player.moving_left = False
    
    def input(self, event):
        self.player_key_up(event)
        self.player_key_down(event)

    def exit(self):
        print("Leaving test level.")

    def enter(self):
        print("Entering test level.")

class TransitionScene(Scene):
    def __init__(self, game, fromScene, toScene):
        self.percentage = 0
        self.fromScene = fromScene
        self.toScene = toScene
        self.constants = game.constants
        self.screen = game.screen

    def update(self):
        self.percentage += 2
        if self.percentage <= 100:
            print("Changed Scene.")
            pass # TODO Create a scene manager to handle this.

class FadeTransitionScene(TransitionScene):
    def draw(self):
        if self.percentage <= 50:
            self.fromScene.draw()
        else:
            self.toScene.draw()

        overlay = pygame.Surface(self.constants.screen_width, self.constants.screen_height)
        alpha = int(abs((255 - ((255/50)*self.percentage))))
        overlay.set_alpha(alpha)
        overlay.fill(self.constants.black)
        self.screen.blit(overlay, (0, 0))

class SceneManager:
    def __init__(self):
        self.scenes = []

    def input(self):
        if len(self.scenes) > 0:
            self.scenes[-1].input()

    def update(self):
        if len(self.scenes) > 0:
            self.scenes[-1].update()

    def draw(self):
        if len(self.scenes) > 0:
            self.scenes[-1].draw()

    def sceneExit(self):
        if len(self.scenes) > 0:
            self.scenes[-1].exit()

    def sceneEnter(self):
        if len(self.scenes) > 0:
            self.scenes[-1].enter()

    def pop(self):
        self.sceneExit()
        self.scenes.pop()
        self.sceneEnter()

    def push(self, scene):
        self.sceneExit()
        self.scenes.append(scene)
        self.sceneEnter()
        print(self.scenes)

    def set(self, scene):
        while len(self.scenes) > 0:
            self.pop()
        for s in scenes:
            self.push(s)
