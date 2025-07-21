import pygame as pg
import pygame_gui as pg_g
from classes.game_state import GameState
# from classes.menu import menu
from classes.controller import Controller
import sys
import time
import random
import math
from typing import List, Union, Optional, Any

class PartialMenu(GameState):
    def __init__(self) -> None:
        self.CONTROLLER : Controller
        self.first_draw_onscreen : bool = True #whether the state is being drawn for the first time, say, after being unloaded. 
        self.CLOCK = pg.time.Clock()
        self.BUMPS: List[int] = [10, 50, 80]
        self.SCREEN_W, self.SCREEN_H = pg.display.get_surface().get_size() #type: ignore
        self.UI_MANAGER = pg_g.UIManager(window_resolution=(self.SCREEN_W, self.SCREEN_H))

    def start(self) -> Optional[Any]:
        self.boot()
        self.first_draw_onscreen = not self.first_draw_onscreen

    def boot(self) -> Optional[Any]:
        # Check to see if we have been assigned a Controller yet...
        if not isinstance(self.CONTROLLER, Controller):
            raise ValueError
        print("partial menu booting up!")
        self.load_at: float = 0.0
        self.progress_bar = pg_g.elements.UIProgressBar(relative_rect=pg.Rect(self.SCREEN_W//2-300, self.SCREEN_H//2+200, 600, 5),manager=self.UI_MANAGER, object_id = pg_g.core.ObjectID(object_id="#start_menu_loading_bar"))
        for i, v in enumerate(self.BUMPS):
            self.BUMPS[i] = random.randint(0,v) if i == 0 else random.randint(self.BUMPS[i-1],v)

    def handle_events(self, events) -> Optional[Any]:
        # By design - the first function that is always ran. Thus, we check for the first_draw, here itself.
        if self.first_draw_onscreen:
            self.start()
        for event in events:
            self.UI_MANAGER.process_events(event)
            match event.type:
                case pg.QUIT:    
                    pg.quit()
                    sys.exit()
                case pg.KEYDOWN:
                    match event.key:
                        case pg.K_ESCAPE:  # Enter key to switch scene
                            pg.quit()
                            sys.exit()
                        case pg.K_BACKSLASH:
                            print("backlash noted")
                            self.close()

    def draw(self, screen) -> Optional[Any]:
        screen.fill((20, 20, 20))
        self.UI_MANAGER.draw_ui(screen)
        
    def update(self) -> Optional[Any]:
        self.UI_MANAGER.update(self.time_delta)

        if math.floor(self.load_at) in self.BUMPS:
            time.sleep(random.randint(1,3))
            self.load_at += 1 # jump to avoid reload
        self.load_at += 0.1
        self.progress_bar.set_current_progress(self.load_at)
        if self.load_at >= 95: 
            self.clean_up()
            #self.close()
        time.sleep(0.01)
 
    def tick(self) -> Optional[Any]:
        self.time_delta = self.CLOCK.tick(60)/1000.0

    def close(self):
        self.CONTROLLER.go_to('menu')