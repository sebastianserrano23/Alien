import sys
import pygame
from ship import Ship

from settings import Settings

class AlienInvasion:
    """
    Overall class to manage game assets and behavior
    """
    def __init__(self):
        """
        initalizing the game, and create game resources
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # set the background color
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        """
        start the main loop of the game
        """
        while True:
            # watch out for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass throught the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

