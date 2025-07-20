# import pygame as pg
# import time
# from Classes.scene import Scene

# class CompleteMenuScene(Scene):
# 	def __init__(self):
# 		self.SCREEN_R, self.SCREEN_G, self.SCREEN_B = 20, 20, 20 #representating a blackish hue

# 	def draw(self, screen):
# 		screen.fill((self.SCREEN_R, self.SCREEN_G, self.SCREEN_B))

# 	def update(self):
# 		if self.SCREEN_R != 255:
# 			self.SCREEN_R += 1
# 			self.SCREEN_G += 1
# 			self.SCREEN_B += 1
# 			time.sleep(0.1)

# 	def handle_events(self, events):
# 	        for event in events:
# 	            if event.type == pg.QUIT:
# 	                pg.quit()
# 	                sys.exit()
# 	            elif event.type == pg.KEYDOWN:
# 	                if event.key == pg.K_ESCAPE:  # Enter key to switch scene
# 	                    pg.quit()
# 	                    sys.exit()