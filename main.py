import pygame,sys, time
from settings import *
from level    import *
from Enemy import *
from player import *

game_over = True

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock  = pygame.time.Clock()
level = Level(level_map, screen)

bg = pygame.image.load("graphics/player/yy.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (screen_width, screen_height))

obj = Player()

font = pygame.font.Font("freesansbold.ttf", 30)
start_text = font.render("Press enter to start", True, (255, 255, 255))
""""
def start_screen():
    global game_over
    screen.blit(start_text, (300, 300))
    screen.blit(bg, (0, 0))
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
"""




while True:
    """"
    if game_over:
        game_over == False
        start_screen()
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    obj.__init__
    x = (level.player.sprite.health)
    y = (level.player.sprite.points)
    text = font.render("Score :0" + str(y), True, (255, 255, 255))
    text1 = font.render("Health:" + str(x), True, (255, 255, 255))
    bg = pygame.image.load("graphics/player/yy.jpg")
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    """
    if level.run4() == True:
        game_over = True
        level.player.sprite.kill()
        
    """
    if x <= 0:
        print("")


    else:
        print("")
    screen.blit(bg, (0, 0))
    screen.blit(text, (0, 0))
    screen.blit(text1, (screen_width - 250, 0))

    level.run()
    pygame.display.update()

    clock.tick(fps)
    """
     def main():
        if x <= 0:
            print("Game over")
        #print(self.points)
        #self.stopwatch.stop()
        #self.stopwatch.get_elapsed_time()
            pygame.display.update()
            level.restart()
    """

