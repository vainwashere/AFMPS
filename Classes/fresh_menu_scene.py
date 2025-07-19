# Example Scene: Menu
import pygame as pg
import pygame_gui as pg_g
from pygame_gui.core import ObjectID
from Classes.scene import Scene
from Classes.game_scene import GameScene
from Classes.complete_menu_scene import CompleteMenuScene
import sys
import time
import random
import math

class FreshMenuScene(Scene):
    def __init__(self, UI_MANAGER): # UI_MANAGER is a special parameter of the FreshMenuScene class.
        self.load_at = 0
        self.bumps = [10,50,80]
        self.ui_manager = UI_MANAGER
        screen_w, screen_h = pg.display.get_surface().get_size()
        self.progress_bar = pg_g.elements.ui_progress_bar.UIProgressBar(relative_rect=pg.Rect(screen_w//2-300, screen_h//2+200, 600, 5),manager=self.ui_manager, object_id = ObjectID(object_id="#start_menu_loading_bar"))
        for i, v in enumerate(self.bumps):
            self.bumps[i] = random.randint(0,v) if i == 0 else random.randint(self.bumps[i-1],v)
        print(self.bumps)

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
        screen.fill((20, 20, 20))
        
    def update(self):
        if math.floor(self.load_at) in self.bumps:
            time.sleep(random.randint(1,3))
            self.load_at += 1
        self.load_at += 0.1
        self.progress_bar.set_current_progress(self.load_at)
        time.sleep(0.01)
        if self.load_at >= 100:
            self.scene_manager.go_to(CompleteMenuScene())
 
        # if self.progress_bar_val >=and self.progress_bar_val < 100:
        #     self.progress_bar.set_current_progress(100)
        # elif self.progress_bar_val < 90:
        #     self.progress_bar.set_current_progress(self.progress_bar_val)
        #     self.progress_bar_val += round(random.random(),1)
        #     time.sleep(0.1)
        # else:
        #     pass
