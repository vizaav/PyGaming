# import pygame
# from pygame import image, transform
# import brajanek.wyglad as wyglad
#
#
# class Brajanek(pygame.Rect):
#
#     def __init__(self, WINDOWWIDTH, WINDOWHEIGHT, givenimage=wyglad.stanie_S):
#         super().__init__(givenimage.get_rect())
#         self.image = givenimage
#         self.image = transform.scale(self.image, (30, 50))
#         self.rect = self.image.get_rect()
#         self.rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
#         self.speed = [2, 2]
#         self.brajanekX = self.rect.centerx
#         self.brajanekY = self.rect.centery
#
#     def change_image(self, name):
#         self.image = wyglad.wyglady[name]
#         self.image = transform.scale(self.image, (30, 50))
#         self.rect = self.image.get_rect()
#         self.rect.center = (self.rect.centerx, self.rect.centery)
#
#     def animate_running(self, left_leg, right_leg):
#         self.change_image(left_leg)
#         pygame.time.wait(100)
#         self.change_image(right_leg)
#         pygame.time.wait(100)
#
