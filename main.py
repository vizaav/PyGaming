import pygame
from pygame import constants, sprite, image, transform, time
from pygame.constants import K_UP, K_RIGHT, K_LEFT, K_a, K_d, K_w, K_s, K_DOWN, K_ESCAPE
import mySprites


def colliding(hero, *obstacles):
    """Returns True if hero is colliding with any of the obstacles."""
    for obstacle in obstacles:
        if hero.rect.colliderect(obstacle.rect):
            return True
    return False


# it just must be here
pygame.init()

# screen - do not touch
size = WINDOWWIDTH, WINDOWHEIGHT = 800, 600
speed = [5, 5]
cat_speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brajanek Defence")
pygame.display.set_icon(pygame.image.load("assets/background.png"))
background_image = pygame.image.load("assets/background.png")
background_image = pygame.transform.scale(background_image, (WINDOWWIDTH, WINDOWHEIGHT))
screen.blit(background_image, (0, 0))

# brajanek
brajanek = mySprites.BrajanekSprite()
clock = pygame.time.Clock()
running = True

# BUSHFENCES
bushfences = []

# inner fences
for i in range(0, 4):
    bushfences.append(mySprites.Bushfence(True))
bushfences[0].set_location(225, 150)
bushfences[1].set_location(425, 150)
bushfences[2].set_location(225, 400)
bushfences[3].set_location(425, 400)

for i in range(0, 4):
    bushfences.append(mySprites.Bushfence(False))

bushfences[4].set_location(225, 150)
bushfences[5].set_location(525, 150)
bushfences[6].set_location(225, 340)
bushfences[7].set_location(525, 340)

# outer fences
for i in range(0, 4):
    bushfences.append(mySprites.Bushfence(True))
bushfences[8].set_location(50, 50)
bushfences[9].set_location(600, 50)
bushfences[10].set_location(50, 500)
bushfences[11].set_location(600, 500)

for i in range(0, 4):
    bushfences.append(mySprites.Bushfence(False))

bushfences[12].set_location(50, 50)
bushfences[13].set_location(700, 50)
bushfences[14].set_location(50, 425)
bushfences[15].set_location(690, 425)

for i in range(0, 4):
    bushfences.append(mySprites.Bushfence(True))
bushfences[16].set_location(150, 50)
bushfences[17].set_location(500, 50)
bushfences[18].set_location(150, 500)
bushfences[19].set_location(500, 500)

for i in range(0, 4):
    bushfences.append(mySprites.Bushfence(False))

bushfences[20].set_location(50, 125)
bushfences[21].set_location(700, 125)
bushfences[22].set_location(50, 350)
bushfences[23].set_location(700, 350)

# CATS
cats = []
for i in range(0, 100):
    cats.append(mySprites.Cat())
cat_adding_frequency = 1

is_running = False  # Flag to track movement state
current_direction = None  # Track the current movement direction

# main loop
while running:
    pygame.display.flip()

    for event in pygame.event.get():

        # quit
        if event.type == pygame.QUIT:
            running = False
        elif event.type == constants.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RIGHT or event.key == K_d:
                # change of appearance
                brajanek.change_image("bieg_D_lewanoga")
                is_running = True
                current_direction = "RIGHT"
            elif event.key == K_LEFT or event.key == K_a:
                # change of appearance
                brajanek.change_image("bieg_A_lewanoga")
                is_running = True
                current_direction = "LEFT"
            elif event.key == K_UP or event.key == K_w:
                # change of appearance
                brajanek.change_image("bieg_W_lewanoga")
                is_running = True
                current_direction = "UP"
            elif event.key == K_DOWN or event.key == K_s:
                # change of appearance
                brajanek.change_image("bieg_S_lewanoga")
                is_running = True
                current_direction = "DOWN"
        elif event.type == constants.KEYUP:
            # change of direction
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
                # when key is released, change of appearance
                brajanek.change_image("stanie_" + current_direction)
                is_running = False
                current_direction = None

    # motion
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

    # cats
    # add a new cat every 5 seconds

    if pygame.time.get_ticks() % 5000 < 10:
        cats.append(mySprites.Cat())
        for i in range(0, cat_adding_frequency):
            cats.append(mySprites.Cat())
            cats[-1].rect.center = (cats[-1].catX, cats[-1].catY)
            screen.blit(cats[-1].image, cats[-1].rect)

        cat_adding_frequency += 1

    for cat in cats:
        collision = False
        for bushfence in bushfences:
            if cat.check_collision(bushfence):
                collision = True
                break
        if collision:
            cat.change_direction()
            cat.move(brajanek)
        else:
            cat.move(brajanek)
        cat.rect.center = (cat.catX, cat.catY)

    if pygame.sprite.spritecollide(brajanek, cats, False):
        """DEATH OF BRAJANEK"""
        # BRAJANEK HAS FALLEN
        print("BRAJANEK HAS FALLEN")
        brajanek.change_image("porazka")
        brajanek.rect.center = (brajanek.brajanekX, brajanek.brajanekY)
        pygame.display.flip()
        screen.blit(brajanek.image, brajanek.rect)
        pygame.display.flip()
        pygame.time.wait(1000)
        running = False

    # drawing - do not touch
    screen.fill(black)
    screen.blit(background_image, (0, 0))
    screen.blit(brajanek.image, brajanek.rect)
    for bushfence in bushfences:
        screen.blit(bushfence.image, bushfence.rect)
    for cat in cats:
        screen.blit(cat.image, cat.rect)
    pygame.display.flip()

    # collision detection
    for bushfence in bushfences:
        if bushfence.check_collision(brajanek):
            if current_direction == "RIGHT":
                brajanek.brajanekX -= brajanek.speed[0]
            elif current_direction == "LEFT":
                brajanek.brajanekX += brajanek.speed[0]
            elif current_direction == "UP":
                brajanek.brajanekY += brajanek.speed[1]
            elif current_direction == "DOWN":
                brajanek.brajanekY -= brajanek.speed[1]

    clock.tick(60)  # Limit the frame rate to 60 FPS
