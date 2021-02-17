import pymunk
from player import Player

class Qwop:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = 0, -1000  # Set gravity of space to -1000

        self.body = pymunk.Body()  # pass rigid body in for editing
        self.player = Player(space, body)

    def get_player(self):
        return self.player

    def get_space(self):
        return self.space