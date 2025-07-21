import pygame as pg
import sys
from classes.controller import Controller
from classes.partial_menu import PartialMenu
import pygame_gui as pg_g
# Main Game Loop
def main():
    pg.init()
    info = pg.display.Info()
    screen_w, screen_h = info.current_w, info.current_h
    screen = pg.display.set_mode((screen_w, screen_h))
    controller = Controller('partial_menu')

    while True:
        controller.current_state.tick()
        events = pg.event.get()
        controller.current_state.handle_events(events)
        if controller.breakloop:
            controller.breakloop = not controller.breakloop
            continue
        controller.current_state.update()
        controller.current_state.draw(screen)
        pg.display.flip()

if __name__ == "__main__":
    main()
