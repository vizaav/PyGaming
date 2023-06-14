from pygame import image, transform, sprite, time, mouse, Surface, draw
import mySprites.wyglad as wyglad
import random


class BrajanekSprite(sprite.Sprite):
    """The main character of the game inherits from the Sprite class"""

    def __init__(self):
        super().__init__()
        self.image = wyglad.stanie_S
        self.image = transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.speed = [2, 2]
        self.brajanekX = self.rect.centerx
        self.brajanekY = self.rect.centery

    def change_image(self, name):
        """Changes the image of the sprite to the one specified by the name
        :param name: name of the image to be changed to
        :return: None"""
        self.image = wyglad.wyglady[name]
        self.image = transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.centerx, self.rect.centery)

    def animate_running(self, left_leg, right_leg):
        """Animates the sprite by changing the image to the left leg and then to the right leg
        :param left_leg: name of the image of the left leg
        :param right_leg: name of the image of the right leg
        :return: None"""

        self.change_image(left_leg)
        time.wait(100)
        self.change_image(right_leg)
        time.wait(100)

    def update(self):
        """Updates the position of the sprite
        :return: None"""
        self.rect.center = (self.brajanekX, self.brajanekY)

    def move(self, direction):
        """Moves the sprite in the specified direction
        :param direction: direction in which the sprite is to be moved
        :return: None"""
        if direction == "RIGHT":
            self.brajanekX += self.speed[0]
        elif direction == "LEFT":
            self.brajanekX -= self.speed[0]
        elif direction == "UP":
            self.brajanekY -= self.speed[1]
        elif direction == "DOWN":
            self.brajanekY += self.speed[1]
        else:
            # Handle unexpected input here
            pass

    def copy(self):
        """Creates a copy of the sprite
        :return: copy of the sprite
        """
        brajanekSpriteCopy = BrajanekSprite()
        brajanekSpriteCopy.image = self.image
        brajanekSpriteCopy.rect = self.rect
        brajanekSpriteCopy.speed = self.speed
        brajanekSpriteCopy.brajanekX = self.brajanekX
        brajanekSpriteCopy.brajanekY = self.brajanekY
        return brajanekSpriteCopy

    def die(self):
        """Changes the image of the sprite to the dead one
        :return: None"""
        self.change_image("assets/brajanek/porazka.png")
        self.image = transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.centerx, self.rect.centery)


class Bushfence(sprite.Sprite):
    """The obstacle of the game inherits from the Sprite class.
    The obstacle can be horizontal or vertical
    """

    def __init__(self, isHorizontal):
        """Initializes the obstacle
        :param isHorizontal: True if the obstacle is horizontal, False if the obstacle is vertical
        """
        super().__init__()
        if isHorizontal:
            self.image = image.load("assets/obstacles/bushfence_horizontal.png")
            # i want to set the rect size manually
            self.rect = self.image.get_rect()
            # self.rect = self.rect.inflate(-10, -10)
        else:
            self.image = image.load("assets/obstacles/bushfence_vertical.png")
            # i want to set the rect size manually
            self.rect = self.image.get_rect()
            # self.rect = self.rect.inflate(-10, -10)

        self.bushfenceX = self.rect.centerx
        self.bushfenceY = self.rect.centery

    def check_collision(self, brajanek):
        """Checks if the obstacle collides with the sprite
        :param brajanek: sprite to check collision with
        :return: True if the obstacle collides with the sprite, False otherwise"""
        if self.rect.colliderect(brajanek.rect):
            return True
        else:
            return False

    def get_direction(self, brajanek):
        """Returns the direction in which the sprite is colliding with the obstacle
        :param brajanek: sprite to check collision with
        :return: direction in which the sprite is colliding with the obstacle"""
        if self.rect.collidepoint(brajanek.rect.midtop):
            return "UP"
        elif self.rect.collidepoint(brajanek.rect.midbottom):
            return "DOWN"
        elif self.rect.collidepoint(brajanek.rect.midleft):
            return "LEFT"
        elif self.rect.collidepoint(brajanek.rect.midright):
            return "RIGHT"
        else:
            return "NONE"

    def set_location(self, x, y):
        """Sets the location of the obstacle
        :param x: x coordinate of the obstacle
        :param y: y coordinate of the obstacle"""
        self.rect.x = x
        self.rect.y = y


class Cat(sprite.Sprite):

    def __init__(self, speed=0.5, spawn=random.choice([(0, 300), (800, 300), (400, 0), (400, 600)])):
        super().__init__()
        self.color = random.choice(["white", "black"])
        if self.color == "white":
            self.image = wyglad.wyglady_white_cat["down_stand"]
        else:
            self.image = wyglad.wyglady_black_cat["down_stand"]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.speed = [speed, speed]

        self.spawn = spawn
        self.catX = self.spawn[0]
        self.catY = self.spawn[1]
        self.direction = self.get_direction(brajanek=self)

    def change_image(self, name):
        """Changes the image of the sprite to the one specified by the name
        :param name: name of the image to be changed to
        :return: None"""
        if self.color == "white":
            self.image = wyglad.wyglady_white_cat[name]
        else:
            self.image = wyglad.wyglady_black_cat[name]

        # self.image = transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.centerx, self.rect.centery)

    def check_collision(self, brajanek):
        """Checks if the obstacle collides with the sprite
        :param brajanek: sprite to check collision with
        :return: True if the obstacle collides with the sprite, False otherwise"""
        if self.rect.colliderect(brajanek.rect):
            return True
        else:
            return False

    def get_direction(self, brajanek):
        """Returns the direction in which the sprite is colliding with the obstacle
        :param brajanek: sprite to check collision with
        :return: direction in which the sprite is colliding with the obstacle"""
        if self.rect.collidepoint(brajanek.rect.midtop):
            return "UP"
        elif self.rect.collidepoint(brajanek.rect.midbottom):
            return "DOWN"
        elif self.rect.collidepoint(brajanek.rect.midleft):
            return "LEFT"
        elif self.rect.collidepoint(brajanek.rect.midright):
            return "RIGHT"
        else:
            return "NONE"

    def set_location(self, x, y):
        """Sets the location of the obstacle
        :param x: x coordinate of the obstacle
        :param y: y coordinate of the obstacle"""
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """Updates the location of the sprite
        :return: None"""
        self.rect.center = (self.catX, self.catY)

    def move(self, brajanek):
        """Moves the sprite in the direction of the sprite
        :param brajanek: sprite to move towards
        :return: None"""

        if self.catX < brajanek.brajanekX:
            self.change_image("right_stand")
            self.catX += self.speed[0]
        elif self.catX > brajanek.brajanekX:
            self.change_image("left_stand")
            self.catX -= self.speed[0]
        if self.catY < brajanek.brajanekY:
            self.change_image("down_stand")
            self.catY += self.speed[1]
        elif self.catY > brajanek.brajanekY:
            self.change_image("up_stand")
            self.catY -= self.speed[1]

    def change_direction(self):
        """Changes the direction of the sprite
        :return: None"""
        self.speed[0] = -self.speed[0]
        self.speed[1] = -self.speed[1]


"""class shoot, menages the crosshair and bullet sprites and collision with enemies"""


class Bullet(sprite.Sprite):

    def __init__(self, brajanek, speed, direction):
        super().__init__()
        self.image = wyglad.wyglady_bullet["bullet"]
        self.image = transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.center = (brajanek.brajanekX, brajanek.brajanekY)
        self.bulletX = brajanek.brajanekX
        self.bulletY = brajanek.brajanekY
        self.speed = speed
        if direction is None:
            print("My direction is NONE!")
        else:
            self.direction = direction

    # def check_collision(self, cat):
    #     """Checks if the obstacle collides with the sprite
    #     :param cat: sprite to check collision with
    #     :return: True if the obstacle collides with the sprite, False otherwise"""
    #     if self.rect.colliderect(cat.rect):
    #         return True
    #     else:
    #         return False

    def kill(self) -> None:
        """Kills the sprite
        :return: None"""
        super().kill()


"""class money, menages the money sprites and collision with brajanek"""

"""class end, menages the end screen and quiting te program"""

"""class drop, menages random drop, such as money and different gun or it's upgrade"""

class Player:
    def __init__(self):
        self.lives = 3
        self.score = 0

    def get_lives(self):
        return self.lives

    def get_score(self):
        return self.score

    def decrease_lives(self):
        self.lives -= 1

    def increase_score(self, amount):
        self.score += amount


class Coin(sprite.Sprite):

    def __init__(self, catX, catY):
        super().__init__()
        self.image = wyglad.wyglady_coin["coin"]
        self.image = transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (catX, catY)
        self.coinX = catX
        self.coinY = catY


class Heart(sprite.Sprite):

        def __init__(self, x, y):
            super().__init__()
            self.image = wyglad.wyglady_heart["heart"]
            self.image = transform.scale(self.image, (40, 40))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.heartX = x
            self.heartY = y


