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
