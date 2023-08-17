import pygame
from settings import *
from tile import *
from player import *
class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,direction):
        super().__init__()
        self.image = pygame.image.load("graphics/player/shot.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction= pygame.math.Vector2(10 * direction ,1)
        """
    def bullet2(self,pos):
        super.__init__()
        self.image = pygame.Surface((50,5))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction= pygame.math.Vector2(-10 ,0)
        """



    def horizontal_movement_collision(self,tiles):
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                tile.kill()
                self.kill()

    def update(self,tiles):
        self.rect.x += self.direction.x
        self.horizontal_movement_collision(tiles)
        if self.rect.x > screen_width:
            self.kill()
