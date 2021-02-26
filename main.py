
import pygame as pg
import pymunk as pm
from qwop import Qwop


pg.init()
pg.display.set_caption("NEAT QWOP")
screen = pg.display.set_mode((1000, 1000))

space = pm.Space()
space.gravity = 0, 100

game = Qwop(space)
player = game.get_player()

gameOver = False
while not gameOver:
    pg.draw.rect(screen, (50,50,75), (0, 0,1000, 1000), 0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
                gameOver = True
    
    headpos = player.get_head().position
    pg.draw.circle(screen, (255, 0, 0), headpos ,50)
    if headpos.y > 1000:
        player.get_head().velocity*=-1
    space.step(1/10.0)
    pg.display.flip()

pg.quit()
