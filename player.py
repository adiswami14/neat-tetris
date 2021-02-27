import pymunk

class Player:
    def __init__(self, space):
        self.space = space  # space is given by pymunk.Space() func

        self.head = pymunk.Body()
        self.head.position = 500, 200
        self.headshape = pymunk.Circle(self.head, 10)
        self.headshape.mass = 10
        self.space.add(self.head, self.headshape)

        self.torso = pymunk.Body(50)
        self.torso.position = 500, 500


    def get_head(self):
        return self.head