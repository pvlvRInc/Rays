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
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos_x += SPEED * cos_a
            self.pos_y += SPEED * sin_a
        elif keys[pygame.K_s]:
            self.pos_x -= SPEED * cos_a
            self.pos_y -= SPEED * sin_a
        if keys[pygame.K_a]:
            self.pos_x += SPEED * sin_a
            self.pos_y += -SPEED * cos_a
        elif keys[pygame.K_d]:
            self.pos_x += -SPEED * sin_a
            self.pos_y += SPEED * cos_a

        if keys[pygame.K_LEFT]:
            self.angle -= ANGLE_VELOCITY
        elif keys[pygame.K_RIGHT]:
            self.angle += ANGLE_VELOCITY