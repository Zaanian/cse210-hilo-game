from gamecards.card import Card

class Game:
    """The hilo game. 
    
    This class runs the main game.

    """
    def __init__(self):
        """Constructs a new Game.
        """
        self.is_playing = True
        self.current_points = 0
        self.score = 0
        self.previous = 0
        self.next = 0
        
        
    def start_game(self):
        """Starts the game by running the main game loop.
        """
        self.start_points = self.current_points + 300
        while self.is_playing:
            self.get_inputs()
            self.higher_lower()
            self.do_updates()
            self.do_outputs()
        
    def get_inputs(self):
        """Ask the user if the next card is higher or lower. Then draws the next card.
        """
        current_card = Card()
        current_card.draw()
        self.current = current_card.value
        print(f"You drew: {self.current}")
        self.guess = input(f"Is the next card higher or lower[h/l]? ")
        
        card = Card()
        card.draw()
        self.next = card.value
        
        
    def higher_lower(self):
        """Test if guess was higher or lower.
        """
        test = self.guess
        if self.next > self.current:
            correct = "h"
        else:
            correct = "l"
        if test == correct:
            self.calculate = True
        else:
            self.calculate = False
        
    def do_updates(self):
        """Updates the player's score.
        """
        if self.calculate == True:
            self.start_points += 100
        else:
            self.start_points -= 75

    def do_outputs(self):
        """Displays the cards and the score. Also asks the player if they want to play again.
        If score is 0 then the game ends. 
        """
        
        values = self.next
        score = self.start_points
        
        
        print(f"You drew: {values}.")
        print(f"")
        print(f"Your score is {score}.")
        
        if self.start_points < 0:
            self.is_playing = False
        if not self.is_playing:
            if self.start_points <= 0:
                print(f"Your score has reached zero or below.")
            print("Game Over. Have a great day!")
            return
        
        play_again = input(f"Do you want to play again? ")
        self.is_playing = (play_again == "y")
        if play_again != "y":
            print(f"Game Over. Have a nice day!")
        
        
        
        
        
       
        
        