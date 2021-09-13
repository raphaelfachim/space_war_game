import pygame
from colors import WHITE, ORC_GREEN, HERO_RED, BLACK, RED
from utils import is_within_boundaries

class Hero(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('space_ship.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = x_pos, y_pos
        self.__name = 'Raphael'
        self.__hp = 10
        self.__attack = 5
        self.__width = self.rect.width
        self.__height = self.rect.height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.vel = 5

    def __str__(self):
        return str(f'{self.__name}\nHP: {self.__hp}\nAttack: {self.__attack}\n')
    
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def att_sprite(self):
        self.rect.topleft = self.x_pos, self.y_pos

    def draw(self, screen):
        rect = pygame.Rect(self.x_pos, self.y_pos, self.__width, self.__height)
        pygame.draw.rect(screen, WHITE, rect)

    def move(self, direction):
        if direction == 'left':
            self.x_pos -= self.vel
        if direction == 'right':
            self.x_pos += self.vel
        if direction == 'up':
            self.y_pos -= self.vel
        if direction == 'down':
            self.y_pos += self.vel

    def shoot(self, screen, direction):
        shot = Shot(self.x_pos, self.y_pos)

class Orc(object):
    def __init__(self, x_pos, y_pos):
        self.__name = 'Orc'
        self.__hp = 20
        self.__attack = 1
        self.__width = 15
        self.__height = 15
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def __str__(self):
        return str(f'{self.__name}\nHP: {self.__hp}\nAttack: {self.__attack}\n')
    
class Tank(object):
    def __init__(self, x_pos, y_pos):
        self.__name = 'Tank'
        self.__hp = 200
        self.__attack = 10
        self.__width = 150
        self.__height = 30
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __str__(self):
        return str(f'{self.__name}\nHP: {self.__hp}\nAttack: {self.__attack}\n')

class Shot(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x_pos-self.rect.width/2), y_pos
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.vel = 4
        self.radius = 3
        self.direction = direction

    def att_sprite(self):
        self.rect.bottomleft = (self.x_pos - self.rect.width / 2), self.y_pos

    def draw_bullet(self, screen):
        if is_within_boundaries(self.y_pos, 0, screen.get_height()):
            self.y_pos -= self.vel
            return True
        else: return False
