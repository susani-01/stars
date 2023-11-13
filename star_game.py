import sys
from random import randint

import pygame

from settings import Settings
from star import Star

class StarGame:
	"""Overall class to manege game assets and behaviuor."""

	
	def __init__(self):
		"""Initialize the game,and create the  game resources ."""
		

		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Star Game")

		self.stars = pygame.sprite.Group()
		self._create_stars()
	
	def run_game(self):
		"""Start the main loop for the game."""

		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		"""Respond to a key presses and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.K_UP:
				self._check_keyup_events(event)

	def _check_keydown_events(self):
		"""Respond to a key presses. """
		if event.key == pygame.K_q:
			sys.exit()

	def _create_stars(self):
		"""Create a sky full of stars"""

		star = Star(self)
		star_width,star_height = star.rect.size
		available_space_x = self.settings.screen_width - (star_width)
		number_star_x = available_space_x // (2*star_width)

		#determine the number of rows of stars that fit on the screen.
		#we will just fill most of the screen with stars 
		available_space_y = (self.settings.screen_height - (2* star_height))
		number_rows = available_space_y // (2*star_height)

		for row_number in range(number_rows):
			for star_number in range(number_star_x):
				self._create_star(star_number,row_number)

	def _create_star(self,star_number,row_number):
		"""Create an star and place it in  the row."""
		star = Star(self)
		star_width,star_height = star.rect.size
		star.rect.x = star_width + 2* star_width * star_number
		star.rect.y = star.rect.height + 2*star.rect.height*row_number
		
		#Randomize the positions of the stars
		#This effects work better with a tiny star.If you are curious,
		#you might want to play around with the spacing a little.
		star.rect.x += randint(-10, 10)
		star.rect.y += randint(-10,10)

		self.stars.add(star)

	def _update_screen(self):
		"""Update images of the screen,and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)

		pygame.display.flip()

if __name__ == '__main__':
	#make a game instance and run the game.
	sg = StarGame()
	sg.run_game()
