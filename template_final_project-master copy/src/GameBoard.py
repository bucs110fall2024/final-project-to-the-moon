import pygame

class GameBoard:
    def __init__(self, screen, grid_size=10, cell_size=50, origin=(50, 100)):
        """Create the board game 

        Args:
            screen (pygame): The screen in which the game board will be created
            grid_size (int): The number of rows and columns within the grid. Defaults to 10.
            cell_size (int): The size of each square within the grid. Defaults to 50.
            origin (tuple): Where the top-left corner of the grid resides on the screen. Defaults to (50, 100).
        """
        self.screen = screen
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.origin = origin
        self.ladders = {3: 22, 8: 26, 20: 29, 36: 44, 51: 67, 62: 81, 71: 91}
        self.slides = {17: 4, 19: 7, 54: 34, 64: 60, 87: 24, 95: 75, 99: 78}

    def draw_board(self):
        """Draw the board which consists of a grid
        """
        
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x = self.origin[0] + col * self.cell_size
                y = self.origin[1] + row * self.cell_size
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)  

        self.draw_specials()

    def draw_specials(self):
        """Draw the ladders and slides on the board
        """
        for start, end in self.ladders.items():
            self.draw_connection(start, end, (0, 255, 0))
        for start, end in self.slides.items():
            self.draw_connection(start, end, (255, 0, 0))

    def draw_connection(self, start, end, color):
        """Draw lines on the board which reprsent either ladders or slides

        Args:
            start (int): The starting grid position of either the ladder of slide
            end (int): The ending grid positon of either the ladder or slide
            color (tuple): The color of said line
        """
        start_pos = self.get_coordinates(start)
        end_pos = self.get_coordinates(end)
        pygame.draw.line(self.screen, color, start_pos, end_pos, 5)

    def get_coordinates(self, position):
        """Get the coordinates of a given grid position

        Args:
            position (int): Uses the grid position to calculate the screen coordinates

        Returns:
            tuple: The screen coordinates, so the player can land in the correct grid positon
        """
        row = (position - 1) // self.grid_size
        col = (position - 1) % self.grid_size if row % 2 == 0 else self.grid_size - 1 - ((position - 1) % self.grid_size)
        x = self.origin[0] + col * self.cell_size
        y = self.origin[1] + (self.grid_size - 1 - row) * self.cell_size
        return x + self.cell_size // 2, y + self.cell_size // 2

    def draw_players(self, players):
        """Draw the players as circles on the board

        Args:
            players (list): A list the reprsents the positions of the players on the board
        """
        for i, player_pos in enumerate(players):
            player_color = (0, 0, 255) if i == 0 else (255, 0, 0)  
            player_pos_coords = self.get_coordinates(player_pos)
            pygame.draw.circle(self.screen, player_color, player_pos_coords, 15) 
