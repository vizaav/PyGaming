from pygame import image, transform, sprite, time
import mySprites.wyglad as wyglad


class BrajanekSprite(sprite.Sprite):
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
        self.image = wyglad.wyglady[name]
        self.image = transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.centerx, self.rect.centery)

    def animate_running(self, left_leg, right_leg):

        self.change_image(left_leg)
        time.wait(100)
        self.change_image(right_leg)
        time.wait(100)

    def update(self):
        self.rect.center = (self.brajanekX, self.brajanekY)

    def move(self, direction):
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
        brajanekSpriteCopy = BrajanekSprite()
        brajanekSpriteCopy.image = self.image
        brajanekSpriteCopy.rect = self.rect
        brajanekSpriteCopy.speed = self.speed
        brajanekSpriteCopy.brajanekX = self.brajanekX
        brajanekSpriteCopy.brajanekY = self.brajanekY
        return brajanekSpriteCopy


class Bushfence(sprite.Sprite):

    def __init__(self, isHorizontal):
        super().__init__()
        if isHorizontal:
            self.image = image.load("assets/obstacles/bushfence_horizontal.png")
            self.rect = self.image.get_rect()
            # self.rect.center = (1000, 300)
            # self.image = transform.scale(self.image, (40, 40))
        else:
            self.image = image.load("assets/obstacles/bushfence_vertical.png")
            self.rect = self.image.get_rect()
            # self.rect.center = (400, 300)
            # self.image = transform.scale(self.image, (40, 40))



        self.bushfenceX = self.rect.centerx
        self.bushfenceY = self.rect.centery

    def check_collision(self, brajanek):
        if self.rect.colliderect(brajanek.rect):
            return True
        else:
            return False

    def get_direction(self, brajanek):
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
        self.rect.x = x
        self.rect.y = y



