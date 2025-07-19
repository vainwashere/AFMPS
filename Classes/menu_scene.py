# Example Scene: Menu
import pygame as pg
import pygame_gui as pg_g
from pygame_gui.core import ObjectID
from Classes.scene import Scene
from Classes.game_scene import GameScene
import sys
import time
import random
class MenuScene(Scene):
    def __init__(self, ui_manager):
        self.progress_bar_val = 0
        self.ui_manager = ui_manager
        screen_w, screen_h = pg.display.get_surface().get_size()
        self.progress_bar = pg_g.elements.ui_progress_bar.UIProgressBar(relative_rect=pg.Rect(10, screen_h-90, screen_w-10, 20),manager=ui_manager, object_id = ObjectID(object_id="#start_menu_loading_bar"))

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:  # Enter key to switch scene
                    pg.quit()
                    sys.exit()

    def draw(self, screen):
        ui_manager = self.ui_manager
        screen.fill((255, 255, 255))
        
    def update(self):
        if not self.progress_bar_val >= 100.0:
            self.progress_bar.set_current_progress(self.progress_bar_val)
            self.progress_bar_val += round(random.random(),1)
            time.sleep(0.1)
        else:
            pass
