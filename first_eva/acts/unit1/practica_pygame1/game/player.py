import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
# player part
class player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(player, self).__init__()
        # ubicacion de la imagen usada para el jugador
        self.surf = pygame.image.load("src/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom > self.SCREEN_HEIGHT:
            self.rect.bottom = self.SCREEN_HEIGHT
