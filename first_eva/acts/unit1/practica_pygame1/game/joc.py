import pygame
import os.path
import os
import time
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_p,
    K_SPACE,
    KEYDOWN,
    QUIT,
)
from Cloud import Cloud
from Player import Player
from Enemy import Enemy
# from Sound import Sound
from Tamany import *

class Joc:
    def __init__(self):
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load(os.path.join("src", "Apoxode_-_Electric_1.mp3"))
        pygame.mixer.music.play(loops=-1)
        pygame.init()
        # Utils
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.SysFont("monospace", 20)
        self.font2 = pygame.font.SysFont("monospace", 50)
        self.background_color = LIGHT_MODE
        self.last_bg = pygame.time.get_ticks()
        self.is_day = True 
        self.move_up_sound = pygame.mixer.Sound(os.path.join("src", "Rising_putter.ogg"))
        self.move_down_sound = pygame.mixer.Sound(os.path.join("src", "Falling_putter.ogg"))
        self.colission_sound = pygame.mixer.Sound(os.path.join("src", "Collision.ogg"))
        
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 500)  # Inicialmente cada 500 ms

        self.ADDCLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDCLOUD, 1200)

        self.CHANGE_BG_TIMER = pygame.USEREVENT + 4
        pygame.time.set_timer(self.CHANGE_BG_TIMER, 20000)  # Cambiar cada 20 segundos

        self.highest_score = self.test_score()
        self.highest_level = self.test_level()

        global SCORE
        global LEVEL

        while True:
            self.game_over = False
            SCORE[0] = 0
            LEVEL[0] = 1
            self.main_menu()
            self.run_game()
            self.max_highest_score()
            self.max_highest_level()
            self.show_defeat_screen()
            if self.game_over == False:
                break

        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()

    def main_menu(self):
        self.screen.fill(LIGHT_MODE)

        Text = self.font.render("  The f-16 at Ukraine  ", True, RED)
        Text_center = (
            SCREEN_WIDTH / 2 - Text.get_width() // 2,
            SCREEN_HEIGHT / 2 - Text.get_height() // 2
        )

        TextStart = self.font.render("Press SPACE to Start", True, RED)
        TextStart_center = (
            SCREEN_WIDTH / 2 - TextStart.get_width() // 2,
            SCREEN_HEIGHT / 2 + 30
        )

        clouds_Added = pygame.sprite.Group()
        clouds_Added.add(Cloud())
        clouds_Added.add(Cloud())
        clouds_Added.add(Cloud())

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        running = False
                    elif event.key == K_p:
                        running = False

                elif event.type == QUIT:
                    self.game_over = True
                    running = False
                elif event.type == self.ADDCLOUD:
                    new_cloud = Cloud()
                    clouds_Added.add(new_cloud)

            clouds_Added.update()
            self.screen.fill(LIGHT_MODE)

            self.screen.blit(Text, Text_center)
            self.screen.blit(TextStart, TextStart_center)

            for entity in clouds_Added:
                self.screen.blit(entity.surf, entity.rect)

            pygame.display.flip()
            self.clock.tick(30)

    def run_game(self):
        global SCORE
        global LEVEL
        player = Player(self.move_up_sound, self.move_down_sound)  
        clouds = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        bg_timer = 0
        bg_change_interval = 20000
        light_mode = LIGHT_MODE
        new_enemy = None
        
        running = True
        while running:
            dt = self.clock.get_time()
            bg_timer += dt
             
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    self.game_over = True
                    running = False

                elif event.type == self.ADDENEMY:
                    new_enemy = Enemy()
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)
                
                elif event.type == self.ADDCLOUD:
                    new_cloud = Cloud()
                    clouds.add(new_cloud)
                    all_sprites.add(new_cloud)
                    
                if new_enemy is not None:    
                    if LEVEL[0] == 1:
                        pygame.time.set_timer(self.ADDENEMY, 500)
                        new_enemy.speed = random.randint(1, 10)
                    elif LEVEL[0] == 2:
                        pygame.time.set_timer(self.ADDENEMY, 450)
                        new_enemy.speed = random.randint(5, 12)
                    elif LEVEL[0] == 3:
                        pygame.time.set_timer(self.ADDENEMY, 50)
                        new_enemy.speed = random.randint(7, 14)
                    elif LEVEL[0] == 4:
                        pygame.time.set_timer(self.ADDENEMY, 10)
                        new_enemy.speed = random.randint(9, 16)
                    elif LEVEL[0] == 5:
                        pygame.time.set_timer(self.ADDENEMY, 5)
                        new_enemy.speed = random.randint(12, 18)

            if bg_timer >= bg_change_interval:
                # Cambiar entre light_mode y dark_mode
                light_mode = not light_mode
                if light_mode:
                    self.background_color = LIGHT_MODE
                else:
                    self.background_color = DARK_MODE
                bg_timer = 0

            keys = pygame.key.get_pressed()
            player.update(keys)
            enemies.update()
            clouds.update()
            
            
            
            for sprite in all_sprites:
                if type[sprite] != Player:
                    self.screen.blit(sprite.surf, sprite.rect)
                    
            for cloud in clouds:
                self.screen.blit(cloud.surf, cloud.rect)
            self.screen.fill(self.background_color)
            
            if pygame.sprite.spritecollideany(player, enemies):
                self.move_up_sound.stop()
                self.move_down_sound.stop()
                self.colission_sound.play()
                player.kill()
                pygame.time.delay(1500)
                
                running = False
                
            score_text = "SCORE: {}".format(SCORE[0]) + " LEVEL: {}".format(LEVEL[0]) + "            HIGHEST SCORE: {}".format(self.highest_score) + " HIGHEST LEVEL: {}".format(self.highest_level)
            score_render = self.font.render(score_text, True, TEXT_COLOR)
            self.screen.blit(score_render, (10, 10))

                
            if LEVEL[0] == 1 and SCORE[0] >= 500:
                LEVEL[0] += 1
            elif LEVEL[0] == 5 :
                self.gamePassed()

            pygame.display.flip()
            self.clock.tick(30)

    def show_defeat_screen(self):
        defeat_text = self.font.render("The f-16 at Ukraine has been shot down", True, RED)
        defeat_text_center = (
            SCREEN_WIDTH / 2 - defeat_text.get_width() // 2,
            SCREEN_HEIGHT / 2 - defeat_text.get_height() // 2
        )

        retry_text = self.font.render("Press SPACE to Retry", True, RED)
        retry_text_center = (
            SCREEN_WIDTH / 2 - retry_text.get_width() // 2,
            SCREEN_HEIGHT / 2 + 30
        )

        clouds_added = pygame.sprite.Group()
        clouds_added.add(Cloud())
        clouds_added.add(Cloud())
        clouds_added.add(Cloud())

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_SPACE:
                        self.game_over = False
                        running = False
                elif event.type == QUIT:
                    self.game_over = True
                    running = False
                elif event.type == self.ADDCLOUD:
                    new_cloud = Cloud()
                    clouds_added.add(new_cloud)

            clouds_added.update()
            self.screen.fill(self.background_color)

            self.screen.blit(defeat_text, defeat_text_center)
            self.screen.blit(retry_text, retry_text_center)

            for entity in clouds_added:
                self.screen.blit(entity.surf, entity.rect)

            pygame.display.flip()
            self.clock.tick(30)

    def gamePassed(self):
        self.screen.fill(LIGHT_MODE)

        Text = self.font.render("  The f-16 at Ukraine has winned ", True, RED)
        Text_center = (
            SCREEN_WIDTH / 2 - Text.get_width() // 2,
            SCREEN_HEIGHT / 2 - Text.get_height() // 2
        )

        clouds_Added = pygame.sprite.Group()
        clouds_Added.add(Cloud())
        clouds_Added.add(Cloud())
        clouds_Added.add(Cloud())

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        running = False
                    elif event.key == K_p:
                        running = False

                elif event.type == QUIT:
                    self.game_over = True
                    running = False
                elif event.type == self.ADDCLOUD:
                    new_cloud = Cloud()
                    clouds_Added.add(new_cloud)

            clouds_Added.update()
            self.screen.fill(LIGHT_MODE)

            self.screen.blit(Text, Text_center)

            for entity in clouds_Added:
                self.screen.blit(entity.surf, entity.rect)

            pygame.display.flip()
            self.clock.tick(30)
            
    def max_highest_score(self):
        global SCORE
        if SCORE[0] > self.highest_score:
            self.highest_score = SCORE[0]
            database = open(os.path.join("src","punt_max.txt"), 'w+')
            database.write(str(SCORE))
            database.close()
            
    def max_highest_level(self):
        global LEVEL
        if SCORE[0] > self.highest_level:
            self.highest_level = LEVEL[0]
            database = open(os.path.join("src","level_max.txt"), 'w+')
            database.write(str(LEVEL))
            database.close()
              
    def test_score(self):
        try:
            database = open(os.path.join("src","punt_max.txt"), 'r')
        except:
            database = open(os.path.join("src","punt_max.txt"), 'w+')
            database.write(str(0))
                
        try:
            highest_score = int(database.readline())
        except ValueError:
            highest_score = 0
                
        database.close()
        return highest_score   
    
    def test_level(self):
        try:
            database = open(os.path.join("src","level_max.txt"), 'r')
        except:
            database = open(os.path.join("src","level_max.txt"), 'w+')
            database.write(str(0))
                
        try:
            highest_score = int(database.readline())
        except ValueError:
            highest_score = 0
                
        database.close()
        return highest_score         
        
if __name__ == "__main__":
    joc = Joc()

