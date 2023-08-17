import pygame
from stopwatch import StopWatch
from bullet import *


class Player(pygame.sprite.Sprite):


    def __init__(self,pos=(0,0)):
        super().__init__()
        self.image = pygame.image.load("graphics/player/Ship4.1.png")

        self.rect = self.image.get_rect(topleft = pos, size = (96,47))
        self.direction= pygame.math.Vector2(0,0)
        self.speed = 10
        self.stopwatch = StopWatch()
        self.stopwatch.start()
        self.time_passed = self.stopwatch.get_elapsed_time
        self.points =0

        self.health = 100

        #shots
        self.shot_sounds = pygame.mixer.Sound("sounds/effects/shot.mp3")
        #shooting
        self.bullets = pygame.sprite.Group()

        self.firing= False





    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        elif keys[pygame.K_SPACE] and not self.firing:
            self.fire()
            self.firing= True
        elif not keys[pygame.K_SPACE] and self.firing:
            self.firing = False
        else:
            self.direction.y = 0
    def horizontal_movement_collision(self, tiles):
        self.rect.x += self.direction.x * self.speed

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                #print(self.health)
                self.health -= 5
                tile.kill()

        if self.health <= 0:

            print("Game over")
            print(self.points)
            self.stopwatch.stop()
            self.stopwatch.get_elapsed_time()
            exit()
            pygame.display.update()



    def fire(self):
        bullet = Bullet((self.rect.centerx,self.rect.centery),1)
        self.bullets.add(bullet)
        pygame.mixer.Sound.play(self.shot_sounds)

    def update(self,tiles):
        self.get_input()
        self.horizontal_movement_collision(tiles)
        self.rect.y += self.direction.y * self.speed
        self.bullets.update(tiles)

    def draw_bullets(self,surface):
        self.bullets.draw(surface)


