import pygame

from ray_casting import *
from settings import *
from map import world_map

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)


    def world(self, player_pos, player_angle):
        #for x, y in world_map:
        #    pygame.draw.rect(self.sc, WHITE, (x, y, TILE, TILE), 2)

        #ray_cast(self.sc, player_pos, player_angle)
        ray_cast_brez(self.sc, player_pos, player_angle)
        #player_sight(self.sc, player_pos, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)

