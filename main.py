import pygame as pg
import sys
from Classes.scene_manager import SceneManager
from Classes.fresh_menu_scene import FreshMenuScene
import pygame_gui as pg_g
# Main Game Loop
def main():
    pg.init()
    info = pg.display.Info()
    screen_w, screen_h = info.current_w, info.current_h
    clock = pg.time.Clock()
    ui_manager = pg_g.UIManager((screen_w, screen_h),"theme.json")
    time_delta = clock.tick(60)/1000.0

    screen = pg.display.set_mode((screen_w, screen_h))

    manager = SceneManager(FreshMenuScene(ui_manager), ui_manager)

    while True:
        events = pg.event.get()

        for event in events:
            ui_manager.process_events(event)
        manager.scene.handle_events(events)

        manager.scene.update()
        ui_manager.update(time_delta)

        manager.scene.draw(screen)
        ui_manager.draw_ui(screen)

        pg.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
