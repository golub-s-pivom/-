from readline import redisplay
from turtle import window_width

import pygame 
import time 

#Камера и мир
window = pygame.display.set_mode(800,600),pygame.FULLSKREEN
clock = time.clock()
world_w = 2000
world_h = 3000
#класы
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed,w,h):
        self.image = pygame.transform.scale(pygame.image.load(sprite_image), (w,h))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class player(GameSprite):
    def update(self):
        keys = keys.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < window_width - 65:
            self.rect.x += self.speed
        if keys[pygame.K_s] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_w] and self.rect.y < window_width - 65:
            self.rect.x += self.speed


#цикл
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    player.reset()
    redisplay.update()
