import random

class Card:
    """Playing cards, numbered 1 through 13.
    This class generates card numbers.
    """

    def __init__(self):
        """Constructs a new instance of Card.
        """
        self.value = 0
        
    def draw(self):
        """Generates a new random value for Card.
        """
        self.value = random.randint(1, 13)