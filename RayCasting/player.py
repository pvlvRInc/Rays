import pygame
from settings import *

class Player():
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.angle = 0

    @property
    def pos(self):
        return (self.pos_x, self.pos_y)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos_y -= SPEED
        elif keys[pygame.K_s]:
            self.pos_y += SPEED
        if keys[pygame.K_a]:
            self.pos_x -= SPEED
        elif keys[pygame.K_d]:
            self.pos_x += SPEED

        if keys[pygame.K_LEFT]:
            self.angle -= ANGLE_VELOCITY
        elif keys[pygame.K_RIGHT]:
            self.angle += ANGLE_VELOCITY