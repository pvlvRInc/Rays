import pygame

from drawing import Drawing
from settings import *
from player import *
from ray_casting import *
from map import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc.fill((0, 0, 0))
pygame.display.set_caption('THE GAME')
clock = pygame.time.Clock()

player = Player(HALF_WIDTH, HALF_HEIGHT)
draw = Drawing(sc, world_map)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(GREY)
    draw.world(player.pos, player.angle)
    draw.fps(clock)
    player.movement()

    #pygame.draw.circle(sc, GREEN, player.pos, RADIUS)

    pygame.display.flip()
