import random

class GameController:
    def __init__(self, ladders, slides, players):
        """_summary_

        Args:
            ladders (dict): A dictionary in which the keys are the starting location of the ladders and the values are the end location where the player will climb up to
            slides (dict): A dictionary in which the keys are the starting location of the slides and the values are the end location where the player will slide down to
            players (list): Represents the starting positions of the players 
        """
        self.ladders = ladders
        self.slides = slides
        self.players = players
        self.current_player = 0
        self.dice_roll = 0
        self.rolled = False

    def roll_dice(self):
        """Roll a six-sided dice using a random integer generator, then the program is notified that the player has rolled and is ready to move, and return the result of the dice roll 

        """
        self.dice_roll = random.randint(1, 6)
        self.rolled = True

    def move_player(self):
        """Move the current player based on dice roll, while taking into account any ladders or slides

        Returns:
            boolean: Returns "True" is the player has reached the 100th position, and false otherwise which makes the other player go 
        """
        if self.rolled:
            self.players[self.current_player] += self.dice_roll

            if self.players[self.current_player] > 100:
                self.players[self.current_player] = 100

            final_position = self.players[self.current_player]
            if final_position in self.ladders:
                self.players[self.current_player] = self.ladders[final_position]
            elif final_position in self.slides:
                self.players[self.current_player] = self.slides[final_position]

            if self.players[self.current_player] == 100:
                return True  

            self.rolled = False
            self.current_player = (self.current_player + 1) % len(self.players)

        return False  
