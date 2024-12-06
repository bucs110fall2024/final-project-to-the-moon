import pygame 

class UserInterface:
    def __init__(self, screen, game_board, game_controller):
        """Initializes the game screen, game board, and game controller

        Args:
            screen (pygame): The screen where the User Interface will be drawed on 
            game_board (GameBoard): Utilizes the gameboard class
            game_controller (GameController): utilizes the gameboard class
        """
        self.screen = screen
        self.game_board = game_board
        self.game_controller = game_controller

    def draw_start_screen(self):
        """Draw the start screen which includes the title 
        """
        font = pygame.font.Font(None, 74)
        text = font.render("Slides and Ladders", True, (0, 0, 0))
        instructions = pygame.font.Font(None, 36).render("Press SPACE to Start", True, (0, 0, 0))
        
        self.screen.fill((255, 255, 255))  
        
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, 100))  
        self.screen.blit(instructions, (self.screen.get_width() // 2 - instructions.get_width() // 2, 200))  
        
        pygame.display.flip()  

    def draw_game_screen(self):
        """Draw the board game, dice roll buttom, and player turn, current dice roll, and current players' positions
        """
        self.screen.fill((255, 255, 255)) 
        self.game_board.draw_board()  
        self.game_board.draw_players(self.game_controller.players)  
        self.draw_dice_roll() 
        self.draw_turn_info()  

    def draw_dice_roll(self):
        """Draw the dice roll button and the current dice value

        Returns:
            pygame.rect: The dice roll button 
        """
        font = pygame.font.Font(None, 36)
        dice_text = font.render(f"Dice Roll: {self.game_controller.dice_roll}", True, (0, 0, 0))
        self.screen.blit(dice_text, (50, 20))

        button_text = font.render("Roll Dice", True, (255, 255, 255))
        button_width = button_text.get_width() + 20  
        button_rect = pygame.Rect(self.screen.get_width() // 2 - button_width // 2 - 50, 20, button_width, 40)  
        pygame.draw.rect(self.screen, (0, 0, 255), button_rect)
    
        self.screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2, button_rect.y + (button_rect.height - button_text.get_height()) // 2))

        return button_rect
        

    def draw_turn_info(self):
        """Draw the current player's turn info
        """
        font = pygame.font.Font(None, 36)
        turn_text = font.render(f"Player {self.game_controller.current_player + 1}'s Turn", True, (0, 0, 0))
        self.screen.blit(turn_text, (self.screen.get_width() - 200, 20))

    def draw_end_screen(self, winner):
        """Draw the end screen and announce the winner of the game

        Args:
            winner (int): The index of the winning player taken from the list 
        """
        font = pygame.font.Font(None, 74)
        text = font.render(f"Player {winner + 1} Wins!", True, (0, 255, 0))
        
        self.screen.fill((255, 255, 255))  
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, self.screen.get_height() // 2))  
        pygame.display.flip()  
        pygame.time.wait(2000)  
