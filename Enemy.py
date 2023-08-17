import pygame, random
from bullet import *
from tile import *
class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphics/player/en.png").convert_alpha()
        self.direction= pygame.math.Vector2(0,0)
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 0.5
        self.health = 100
        #shots
        self.shot_sounds = pygame.mixer.Sound("sounds/effects/shot.mp3")




        #shooting
        self.bullets = pygame.sprite.Group()
        self.bullet_delay = random.randint(20, 60)




    def horizontal_movement_collision(self, tiles):
        self.rect.x += self.direction.x * self.speed
        """
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
        """





    def fire(self):
        bullet = Bullet((self.rect.centerx,self.rect.centery),-1)
        self.bullets.add(bullet)
        pygame.mixer.Sound.play(self.shot_sounds)

    def update(self,tiles,x_shift):
        self.rect.x += x_shift
        self.horizontal_movement_collision(tiles)
        self.rect.y += self.direction.y * self.speed
        self.bullets.update(tiles)
        self.direction.y = random.randint(-10, 10)

        self.bullet_delay -= 1
        if self.bullet_delay == 0:
            self.bullet_delay = random.randint(30, 60)
            self.fire()

        #for i in range():
            #self.get_input()

    def draw_bullets(self,surface):
        self.bullets.draw(surface)
