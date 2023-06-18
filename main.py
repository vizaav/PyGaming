import pygame
from pygame import constants
from pygame.constants import K_UP, K_RIGHT, K_LEFT, K_a, K_d, K_w, K_s, K_DOWN, K_ESCAPE, K_SPACE
import mySprites
from mySprites.locations import bushfence_locations
import random


def colliding(hero, *obstacles):
    """Returns True if hero is colliding with any of the obstacles.
    Otherwise, returns False.
    :param hero: the sprite to check for collisions against the obstacles
    :param obstacles: any number of sprites to check for collisions against
    :return: True if hero is colliding with any of the obstacles; False otherwise"""
    for obstacle in obstacles:
        if hero.rect.colliderect(obstacle.rect):
            return True
    return False


# it just has to be here
pygame.init()


# screen - do not touch
size = WINDOWWIDTH, WINDOWHEIGHT = 800, 600
speed = [5, 5]
cat_speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brajanek Defence")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
background_image = pygame.image.load("assets/background.png")
background_image = pygame.transform.scale(background_image, (WINDOWWIDTH, WINDOWHEIGHT))
screen.blit(background_image, (0, 0))

# UI font
font = pygame.font.SysFont('consolas', 20)
fontend = pygame.font.SysFont('consolas', 50)

# COIN STUFF
cgroup = []
counter = 0

# PLAYER
player = mySprites.Player()

# brajanek
brajanek = mySprites.BrajanekSprite()
clock = pygame.time.Clock()
running = True
previous_direction = "DOWN"

# GUN STUFF
bgroup = []
bspeed = [10, 10]

# BUSHFENCES - load from locations.py
bushfences = []
for location in bushfence_locations:
    bushfences.append(mySprites.Bushfence(location[2]))
    bushfences[-1].set_location(location[0], location[1])

# CATS
cats = []
cat_adding_frequency = 1
CAT_SPEED = 0.5

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
            elif event.key == K_SPACE:
                if current_direction is None:
                    # shooting while standing
                    new_shoot = mySprites.Bullet(brajanek, bspeed, previous_direction)
                else:
                    # shooting while running
                    new_shoot = mySprites.Bullet(brajanek, bspeed, current_direction)
                bgroup.append(new_shoot)
                screen.blit(new_shoot.image, new_shoot.rect)
                pygame.display.flip()
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
                previous_direction = current_direction
                current_direction = None
            elif event.key == K_SPACE:
                is_shooting = False

    # Movement of the bullets based on brajanek direction of movement, if movement is halted -> based on previous
    # direction
    for bullet in bgroup:
        # if bullet is out of the screen, remove it from the group
        if bullet.bulletX > WINDOWWIDTH or bullet.bulletX < 0 or bullet.bulletY > WINDOWHEIGHT or bullet.bulletY < 0:
            bgroup.remove(bullet)
            continue
        if bullet.direction == "RIGHT":
            bullet.bulletX += bullet.speed[0]
        elif bullet.direction == "LEFT":
            bullet.bulletX -= bullet.speed[0]
        elif bullet.direction == "UP":
            bullet.bulletY -= bullet.speed[1]
        elif bullet.direction == "DOWN":
            bullet.bulletY += bullet.speed[1]

        bullet.rect.center = (bullet.bulletX, bullet.bulletY)
        screen.blit(bullet.image, bullet.rect)
        pygame.display.flip()

    # MOTION OF BRAJANEK
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

    # CATS BRAINS
    # add a new cat every 5 seconds
    if pygame.time.get_ticks() % 200 == 0:
        for i in range(0, 4):
            if i == 0:
                cats.append(mySprites.Cat(speed=CAT_SPEED, spawn=(0, 300)))
            elif i == 1:
                cats.append(mySprites.Cat(speed=CAT_SPEED, spawn=(800, 300)))
            elif i == 2:
                cats.append(mySprites.Cat(speed=CAT_SPEED, spawn=(400, 0)))
            elif i == 3:
                cats.append(mySprites.Cat(speed=CAT_SPEED, spawn=(400, 600)))
            cats[-1].rect.center = (cats[-1].catX, cats[-1].catY)
            screen.blit(cats[-1].image, cats[-1].rect)
        CAT_SPEED += 0.1

    # CATS MOVEMENT
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

    # COLLISIONS - BRAJANEK, BUSHES, CATS, BULLETS
    if pygame.sprite.spritecollide(brajanek, cats, False):
        if player.lives == 0:
            """DEATH OF BRAJANEK"""
            # BRAJANEK HAS FALLEN
            print("BRAJANEK HAS FALLEN")
            brajanek.change_image("porazka")
            brajanek.rect.center = (brajanek.brajanekX, brajanek.brajanekY)
            pygame.display.flip()
            screen.blit(brajanek.image, brajanek.rect)
            pygame.display.flip()
            pygame.time.wait(1000)
            print("GAME OVER")
            print("SCORE: " + str(player.score))
            print("TIME: " + str(pygame.time.get_ticks() / 1000))
            running = False
    if counter >= 5:
        # Winning condition and end of the game
        waiting = True
        while waiting:
            text = fontend.render("YOU WON", True, (255, 255, 255))
            # Making sure the text is centered (it isn't, and it doesn't like me very much)
            screen.blit(text, (400 - text.get_width() // 2, 300 - text.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(1000)
            waiting = False
        pygame.time.wait(1000)
        running = False

    for cat in cats:
        for bullet in bgroup:
            if pygame.sprite.collide_rect(cat, bullet):
                """DEATH OF CAT"""
                # CAT HAS BEEN SHOT
                player.increase_score(1)
                cats.remove(cat)
                # coin spawn and randomness
                if random.randint(0, 1000) > 800:
                    coin = mySprites.Coin(cat.catX, cat.catY)
                    cgroup.append(coin)
                    player.increase_score(10)
                    coin.rect.center = (coin.coinX, coin.coinY)
                    screen.blit(coin.image, coin.rect)
                bgroup.remove(bullet)
                screen.blit(cat.image, cat.rect)
                screen.blit(bullet.image, bullet.rect)
                pygame.display.flip()
                break
        if pygame.sprite.collide_rect(cat, brajanek):
            """DECREASE OF LIVES"""
            cats.remove(cat)
            player.decrease_lives()
            print("Lives left: " + str(player.lives))

    for coin in cgroup:
        if pygame.sprite.collide_rect(coin, brajanek):
            cgroup.remove(coin)
            counter += 1

    # drawing - do not touch
    screen.fill(black)
    screen.blit(background_image, (0, 0))
    screen.blit(brajanek.image, brajanek.rect)
    for bushfence in bushfences:
        screen.blit(bushfence.image, bushfence.rect)
    for cat in cats:
        screen.blit(cat.image, cat.rect)
    for bullet in bgroup:
        screen.blit(bullet.image, bullet.rect)
    for coin in cgroup:
        screen.blit(coin.image, coin.rect)

    # Drawing Lives of the player
    if player.lives == 3:
        heart1 = mySprites.Heart(20, 15)
        heart2 = mySprites.Heart(50, 15)
        heart3 = mySprites.Heart(80, 15)
        screen.blit(heart1.image, heart1.rect)
        screen.blit(heart2.image, heart2.rect)
        screen.blit(heart3.image, heart3.rect)
    elif player.lives == 2:
        heart1 = mySprites.Heart(20, 15)
        heart2 = mySprites.Heart(50, 15)
        screen.blit(heart1.image, heart1.rect)
        screen.blit(heart2.image, heart2.rect)
    elif player.lives == 1:
        heart1 = mySprites.Heart(20, 15)
        screen.blit(heart1.image, heart1.rect)
    elif player.lives == 0:
        text = font.render("LAST ONE", True, (255, 255, 255))
        screen.blit(text, (20, 15))

    # Drawing Coins and its counter
    money = mySprites.CoinUI(700, 15)
    screen.blit(money.image, money.rect)
    text = font.render(str(counter) + " / 5", False, (255, 255, 255))
    screen.blit(text, (720, 7))

    # Drawing Score of the player
    text = font.render("SCORE: " + str(player.score), True, (255, 255, 255))
    # left bottom corner
    screen.blit(text, (10, 575))

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
