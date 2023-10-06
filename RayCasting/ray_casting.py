import pygame
from math import cos, sin

from map import *
from settings import *


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_cast(sc, pl_pos, pl_angle):
    start_angle = pl_angle - FOV / 2
    xo, yo = pl_pos

    for ray in range(NUM_RAYS):

        ray_angle = start_angle + ray * DELTA_ANGLE
        cos_a = cos(ray_angle)
        sin_a = sin(ray_angle)

        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            pygame.draw.line(sc, WHITE, pl_pos, (x, y), 2)
            if mapping(x, y) in world_map:
                break


def ray_cast_brez(sc, pl_pos, pl_angle):
    start_angle = pl_angle - FOV / 2
    xo, yo = pl_pos
    xm, ym = mapping(xo, yo)

    for ray in range(NUM_RAYS):
        ray_angle = start_angle + ray * DELTA_ANGLE
        cos_a = cos(ray_angle)
        sin_a = sin(ray_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - xo) / cos_a
            y = yo + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE

        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - yo) / sin_a
            x = xo + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE

        depth = depth_v if depth_v < depth_h else depth_h
        x = xo + depth * cos_a
        y = yo + depth * sin_a
        proj_coef = PROJ_COEF/depth
        #pygame.draw.line(sc, WHITE, pl_pos, (x, y), 2)
        c = 255/(1 + depth * depth * 0.0001)
        color = (c,c,c)
        pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_coef//2, SCALE, proj_coef))


def player_sight(sc, pl_pos, pl_angle):
    xo, yo = pl_pos
    cos_a = cos(pl_angle)
    sin_a = sin(pl_angle)

    x = xo + RAY_DIST * cos_a
    y = yo + RAY_DIST * sin_a

    pygame.draw.line(sc, RED, pl_pos, (x, y), 2)
