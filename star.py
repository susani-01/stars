import pygame

from pygame.sprite import Sprite

class Star(Sprite):
	"""A class to represents a single star"""

	def __init__(self,stars_game):
		"""Initialize the star and set its starting position"""
		super().__init__()
		self.screen = stars_game.screen

		#load the star image and set its rect attribute.
		self.image = pygame.image.load("star.png")
		self.rect = self.image.get_rect()

		#start  each new star near  the top of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store the star's exact vertical position.
		self.y = float(self.rect.y)

	