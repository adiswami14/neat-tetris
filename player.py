import pymunk

class Player:
    def __init__(self, space, body):
        self.space = space  # space is given by pymunk.Space() func
        self.body = body

    def get_body(self):
        return body