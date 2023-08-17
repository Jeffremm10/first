import pygame,time
from settings import *
from tile import Tile
from player import Player
from bullet import *
from Enemy import Enemy

from stopwatch import StopWatch


class Level:

    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.Group()
        self.setup_level(level_data)
        self.time = 0
        pygame.mixer.music.load("sounds/music/astro.mp3")
        pygame.mixer.music.set_volume(100)
        pygame.mixer.music.play(-1)
        self.world_shift = -4

    def run4(self):
        if self.player.sprite.health == 0:
            return True
    def restart(self):
        self.player.sprite.kill()
        "HEHEHE"




    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                elif cell == "p":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                elif cell == "e":
                    enemy_sprite = Enemy((x,y))
                    self.enemy.add(enemy_sprite)


    def run(self):
        self.tiles.draw(self.display_surface)
        self.player.update(self.tiles)
        self.tiles.update(self.world_shift)
        self.player.draw(self.display_surface)
        self.player.sprite.draw_bullets(self.display_surface)
        self.enemy.draw(self.display_surface)
        self.enemy.update(self.tiles,self.world_shift)
        for e in self.enemy:
            e.draw_bullets(self.display_surface)

            if pygame.sprite.spritecollide(self.player.sprite, e.bullets, True):
                self.player.sprite.health -= 25
                print(self.player.sprite.health)
                healthy = self.player.sprite.health
            if pygame.sprite.spritecollide(e, self.player.sprite. bullets, True):
                e.health -= 34
                if e.health <= 0:
                    e.kill()
                    self.player.sprite.points +=100





        self.time+= 1
        if self.time > 300:
            self.time = 1
            self.player.sprite.health += 10
            self.player.sprite.points += 250
            self.world_shift-=1







