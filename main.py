import time

import pygame
from classes import *
from pygame.locals import *

widht = 640
height = 480

screen = pygame.display.set_mode((widht, height), 0)
pygame.init()

hero = Hero(widht/2, (height-20))
shots = []

background_image = pygame.image.load('galaxy.jpg')
background_image = pygame.transform.scale(background_image, (widht,height))

hero_sprite = pygame.sprite.Group()
hero_sprite.add(hero)

bullet_sprite = pygame.sprite.Group()

while True:
    time.sleep(0.016)
    #Calculation

    #Screen att
    screen.fill(BLACK)

    screen.blit(background_image, (0,0))

    hero.att_sprite()
    hero_sprite.draw(screen)

    for s in shots:
        bullet_on_screen = s.draw_bullet(screen)
        s.att_sprite()
        bullet_sprite.add(s)
        bullet_sprite.draw(screen)
        if not bullet_on_screen: shots.remove(s)

    pygame.display.flip()

    if pygame.key.get_pressed()[pygame.K_w]:
        if is_within_boundaries(hero.y_pos - hero.vel, 0, screen.get_height()):
            hero.move('up')
    if pygame.key.get_pressed()[pygame.K_s]:
        if is_within_boundaries(hero.y_pos + hero.vel, 0, screen.get_height() - hero.height):
            hero.move('down')
    if pygame.key.get_pressed()[pygame.K_a]:
        if is_within_boundaries(hero.x_pos - hero.vel, 0, screen.get_width()):
            hero.move('left')
    if pygame.key.get_pressed()[pygame.K_d]:
        if is_within_boundaries(hero.x_pos + hero.vel, 0, screen.get_width() - hero.width):
            hero.move('right')



    #Events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            print(len(shots))
            exit()
        if e.type == pygame.KEYDOWN:
            key = str(pygame.key.name(e.key))
            if key == 'up':
                s = Shot(hero.x_pos+hero.width/2, hero.y_pos, 'up')
                shots.append(s)

