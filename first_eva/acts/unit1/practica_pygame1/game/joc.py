import pygame
import os.path
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from Cloud import Cloud
from Player import Player
from Enemy import Enemy
from Sound import Sound
from Tamany import *


class Joc:
    def __init__(self):
        pygame.mixer.init()
        self.sound_manager = Sound()
        self.player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.cloud_instance = Cloud(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.clock = pygame.time.Clock()
        pygame.init()

        # utils
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # add sprites
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 250)

        self.ADDCLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDCLOUD, 1200)

        global score
        while True:
            self.reboot = False
            score[0] = 0
            self.joc()
            if self.reboot == True:
                break

        # Salimos del juego
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()


def joc(self):
    global score
    clouds = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif event.type == ADDCLOUD:
                new_cloud = Cloud(SCREEN_WIDTH, SCREEN_HEIGHT)
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

        keys = pygame.key.get_pressed()
        player.update(keys)
        enemies.update()
        clouds.update()

        self.screen.fill(DARK_MODE)

        for cloud in clouds:
            screen.blit(cloud.surf, cloud.rect)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            sound_manager.play_move_down_Sound.stop()
            sound_manager.play_move_up_Sound.stop()
            sound_manager.play_collision_sound()
            # Aplicamos un retraso para escuchar el sonido de colisión
            pygame.time.delay(1500)
            player.kill()
            pygame.display.flip()

        running = False

    Text = "SCORE: [" + str(score[0]) + "]"
    Text = self.font.render(Text, True, DARK_MODE)
    self.screen.blit(Text, (10, 10))
    pygame.display.flip()
    clock.tick(30)
