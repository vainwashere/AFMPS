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

class Menu(GameState):
    def __init__(self) -> None:
        self.OPACITY_FULL = False # Why a constant...? Idk
        self.CONTROLLER : Controller
        self.first_draw_onscreen : bool = True #whether the state is being drawn for the first time, say, after being unloaded. 
        self.CLOCK = pg.time.Clock()
        self.BUMPS: List[int] = [10, 50, 80]
        self.SCREEN_W, self.SCREEN_H = pg.display.get_surface().get_size() #type: ignore
        self.UI_MANAGER = pg_g.UIManager(window_resolution=(self.SCREEN_W, self.SCREEN_H))

    def start(self) -> Optional[Any]:
        self.boot()
        self.transition_bg()
        self.first_draw_onscreen = not self.first_draw_onscreen

    def opacity(self) -> None:
        colorfill = [20,20,20]
        while colorfill[-1] != 255:
            for i in colorfill:
                i += 1
            screen.fill((colorfill[0], colorfill[1], colorfill[2])) #type:ignore
            time.sleep(0.02)

    def boot(self) -> Optional[Any]:
        self.R = 20
        self.G = 20
        self.B = 20
        self.Opacit = False
        # Check to see if we have been assigned a Controller yet...
        if not isinstance(self.CONTROLLER, Controller):
            raise ValueError

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

    def draw(self, screen) -> Optional[Any]:
        print("normal draw called")
        screen.fill((255, 255, 255))
        self.UI_MANAGER.draw_ui(screen)
        
    def update(self) -> Optional[Any]:
        if not self.time_delta:
            self.time_delta = self.CLOCK.tick(60)/1000.0
        self.UI_MANAGER.update(self.time_delta)
        pass
 
    def tick(self) -> Optional[Any]:
        self.time_delta = self.CLOCK.tick(60)/1000.0

    def close(self):
        pass
        #self.CONTROLLER.go_to('menu')