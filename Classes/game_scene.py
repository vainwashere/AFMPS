# Example Scene: Game
import pygame
from Classes.scene import Scene
import sys
class GameScene(Scene):
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self, screen):
        screen.fill((0, 0, 100))
        font = pygame.font.SysFont(None, 50)
        text = font.render("Game Scene", True, (255, 255, 255))
        screen.blit(text, (50, 100))