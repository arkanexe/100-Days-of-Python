# clock.py
from datetime import datetime
from hand import Hand

class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.hour_hand = Hand(length=100, thickness=6, color="black")
        self.minute_hand = Hand(length=150, thickness=4, color="black")
        self.second_hand = Hand(length=170, thickness=2, color="red")

    def update(self):
        now = datetime.now()
        # TODO: work out the three angles using the formulas above
        # TODO: call point_to() on each hand
        self.screen.update()
        self.screen.ontimer(self.update, 1000)
