import math

WIDTH = 1200
HEIGHT = 600
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
TILE = 1200 // 33

NUM_RAYS = 360
FOV = math.pi / 2
HALF_FOV = FOV/2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = HALF_WIDTH
DIST = NUM_RAYS / 2 * math.tan(HALF_FOV)
PROJ_COEF = TILE * DIST * 10
SCALE = WIDTH // NUM_RAYS

FPS_POS = (WIDTH - 65, 5)
FPS = 60

# Player
SPEED = 2
RADIUS = 10
ANGLE_VELOCITY = 0.05
RAY_DIST = WIDTH

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)