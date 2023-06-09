from pygame import image, transform, sprite, time, mouse, Surface, draw
import mySprites.wyglad as wyglad
import random


class BrajanekSprite(sprite.Sprite):
    """The main character of the game inherits from the Sprite class"""

    def __init__(self):
        """
        Initializes the player sprites
        """
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
    """The cat of the game inherits from the Sprite class. A feral cat that wants to kill brajanek"""
    def __init__(self, speed=0.5, spawn=random.choice([(0, 300), (800, 300), (400, 0), (400, 600)])):
        """
        Initializes the cat, it's two different states and colours
        :param speed: How fast is the cat, and how feral it is (BE SCARED)
        :param spawn: The location where the cat spawns
        """
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


class Bullet(sprite.Sprite):
    """ The bullet of the game inherits from the Sprite class. Used to kill ferals, has a limited range."""
    def __init__(self, brajanek, speed, direction):
        """
        Initiates the bullet sprite, sets the image size and location based on a player coordinates
        :param brajanek: takes player coordinates
        :param speed: sets speed of the bullet
        :param direction: sets direction of the bullet based upon players last input direction
        """

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

    def kill(self) -> None:
        """Kills the sprite
        :return: None"""
        super().kill()


class Player:
    def __init__(self):
        """
        Initializes the player class, sets the lives to 3 and score to 0, it is meant to be used outside of player so
        that Brajanek doesnt have too many functions
        """
        self.lives = 3
        self.score = 0

    def get_lives(self):
        """
        Returns the amount of lives the player has
        :return: returns how many lives the player has left
        """
        return self.lives

    def get_score(self):
        """
        Returns the score of the player
        :return: how many cats the player had neutralized :)
        """
        return self.score

    def decrease_lives(self):
        """
        Decreases the amount of lives the player has by 1
        :return: Players new amount of lives
        """
        self.lives -= 1

    def increase_score(self, amount):
        """
        Increases the score of the player by the given amount
        :param amount: set in main :)
        :return: the new score of the player
        """
        self.score += amount


class Coin(sprite.Sprite):
    """ The coin of the game inherits from the Sprite class. Used as a game end mechanic."""
    def __init__(self, catX, catY):
        """
         Initializes the coin sprite, changes it's image size to 20x20 and sets it's location to the given coordinates
        :param catX: takes it from the Cat class it's used to set the x location of the coin
        :param catY: takes it from the Cat class it's used to set the y location of the coin
        """
        super().__init__()
        self.image = wyglad.wyglady_coin["coin"]
        self.image = transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (catX, catY)
        self.coinX = catX
        self.coinY = catY


class Heart(sprite.Sprite):
    """ The heart of the game inherits from the Sprite class. Used as a visual representation of lives left."""
    def __init__(self, x, y):
        """
        Initializes the heart sprite, changes it's image size to 40x40 and sets it's location to the given
        coordinates used for UI nothing else
        :param x: takes given x coordinate for it to be placed on the screen
        :param y: takes given y coordinate for it to be placed on the screen
        """
        super().__init__()
        self.image = wyglad.wyglady_heart["heart"]
        self.image = transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.heartX = x
        self.heartY = y


class CoinUI(sprite.Sprite):
    """ The second coin of the game inherits from the Sprite class. Used as a visual representation of coins collected."""
    def __init__(self, x, y):
        """
        Initializes the Second coin sprite, second bc of the size of playable and collidable one isnt good and
        changing it inside main would be a pain to fix changes it's image size to 40x40 and sets it's location to the
        given coordinates Used for UI nothing else
        :param x: takes given x coordinate for it to be placed on the
        screen
        :param y: takes given y coordinate for it to be placed on the screen
        """
        super().__init__()
        self.image = wyglad.wyglady_coin["coin"]
        self.image = transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.coinX = x
        self.coinY = y
