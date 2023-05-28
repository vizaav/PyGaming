import sys
import pygame
from pygame import constants
from pygame.constants import K_UP, K_RIGHT, K_LEFT, K_a, K_d, K_w, K_s, K_DOWN, K_ESCAPE
from brajanek import Brajanek

pygame.init()

size = WINDOWWIDTH, WINDOWHEIGHT = 800, 600
speed = [5, 5]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brajanek Defence")
pygame.display.set_icon(pygame.image.load("assets/background.png"))

background_image = pygame.image.load("assets/background.png")
background_image = pygame.transform.scale(background_image, (WINDOWWIDTH, WINDOWHEIGHT))
screen.blit(background_image, (0, 0))

brajanek = Brajanek(WINDOWWIDTH, WINDOWHEIGHT)
clock = pygame.time.Clock()
running = True

is_running = False  # Flag to track movement state
current_direction = None  # Track the current movement direction

while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == constants.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RIGHT or event.key == K_d:
                brajanek.change_image("bieg_D_lewanoga")
                is_running = True
                current_direction = "RIGHT"
            elif event.key == K_LEFT or event.key == K_a:
                brajanek.change_image("bieg_A_lewanoga")
                is_running = True
                current_direction = "LEFT"
            elif event.key == K_UP or event.key == K_w:
                brajanek.change_image("bieg_W_lewanoga")
                is_running = True
                current_direction = "UP"
            elif event.key == K_DOWN or event.key == K_s:
                brajanek.change_image("bieg_S_lewanoga")
                is_running = True
                current_direction = "DOWN"
        elif event.type == constants.KEYUP:
            if (
                    (event.key == K_RIGHT or event.key == K_d)
                    and current_direction == "RIGHT"
            ) or (
                    (event.key == K_LEFT or event.key == K_a)
                    and current_direction == "LEFT"
            ) or (
                    (event.key == K_UP or event.key == K_w)
                    and current_direction == "UP"
            ) or (
                    (event.key == K_DOWN or event.key == K_s)
                    and current_direction == "DOWN"
            ):
                brajanek.change_image("stanie_" + current_direction)
                is_running = False
                current_direction = None

    if is_running:
        if current_direction == "RIGHT":
            brajanek.brajanekX += brajanek.speed[0]
        elif current_direction == "LEFT":
            brajanek.brajanekX -= brajanek.speed[0]
        elif current_direction == "UP":
            brajanek.brajanekY -= brajanek.speed[1]
        elif current_direction == "DOWN":
            brajanek.brajanekY += brajanek.speed[1]

    brajanek.rect.center = (brajanek.brajanekX, brajanek.brajanekY)

    screen.fill(black)
    screen.blit(background_image, (0, 0))
    screen.blit(brajanek.image, brajanek.rect)

    pygame.display.flip()

    clock.tick(60)  # Limit the frame rate to 60 FPS
