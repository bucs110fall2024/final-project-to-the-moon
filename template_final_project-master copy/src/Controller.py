import pygame
from src.GameController import GameController
from src.UserInterface import UserInterface
from src.GameBoard import GameBoard

class Controller:
    def __init__(self, screen):
        """Initialize the game controller, userinterface, and game board

        Args:
            screen (pygame): The screen where the game will be displayed 
        """
        self.screen = screen
        self.game_board = GameBoard(self.screen)  
        self.game_controller = GameController(self.game_board.ladders, self.game_board.slides, [1, 1])
        self.ui_manager = UserInterface(self.screen, self.game_board, self.game_controller)

    def run(self):
        """It allows the user to start the game, play the game, and quit the game
        """
        running = True
        in_start_screen = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN and in_start_screen and event.key == pygame.K_SPACE:
                    in_start_screen = False  

                if event.type == pygame.MOUSEBUTTONDOWN and not in_start_screen:
                    mouse_pos = pygame.mouse.get_pos()
                    button_rect = self.ui_manager.draw_dice_roll()  
                    if button_rect.collidepoint(mouse_pos) and not self.game_controller.rolled:
                        self.game_controller.roll_dice()

            if in_start_screen:
                self.ui_manager.draw_start_screen()  
            else:
                if self.game_controller.rolled:
                    if self.game_controller.move_player(): 
                        self.ui_manager.draw_end_screen(self.game_controller.current_player)  
                        running = False  

                self.ui_manager.draw_game_screen()  

            pygame.display.flip()
            pygame.time.Clock().tick(30)
