import pymunk

class Player:
    def __init__(self, space):
        self.space = space  # space is given by pymunk.Space() func

        self.head = pymunk.Body()
        self.head.position = 500, 200

        #self.torso = pymunk.Body(50)
        #self.torso.position = 

        self.shape = pymunk.Circle(self.head, 10)
        self.shape.mass = 10
        self.shape.friction = 1
        self.space.add(self.head, self.shape)

    def get_head(self):
        return self.head