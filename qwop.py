import pymunk
from player import Player

class Qwop:
    def __init__(self,space):
        self.space = space

        self.player = Player(self.space)

    def get_player(self):
        return self.player

    def get_space(self):
        return self.space