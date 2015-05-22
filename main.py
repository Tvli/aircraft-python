import pygame, sys, screenText
from process import process
from process import gameover
from classes import *
from time import sleep

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("audio/background_music.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

SCREENWIDTH, SCREENHEIGHT = 500, 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)


clock = pygame.time.Clock()
FPS = 24


player = Player(SCREENWIDTH / 2.0 - 25, SCREENHEIGHT - 47, "images/player.png")

total_frames = 0


color = 0
delta = 5

while True:
  process(player,FPS, total_frames, SCREENWIDTH)

  if gameover():
    sleep(1.5)
    screen_image = pygame.image.load("images/gameover.jpg")
    screen.blit(screen_image, (0,0))
    pygame.display.flip()
    sleep(3)
    pygame.quit()
    sys.exit()
    pass

  player.motion(SCREENWIDTH, SCREENHEIGHT)
  Flight.update(SCREENHEIGHT)
  Bullet.movement()

  total_frames += 1

  color += delta
  if color == 255:
    delta = -5
  elif color == 0:
    delta = 5
  else:
    pass

  screen.fill((color,color,color))
  BaseClass.all_sprites.draw(screen)
  Bullet.List.draw(screen)

  screenText.screen_text(screen, 'Score : {0}'.format(player.score), 0, 0)


  pygame.display.flip()
  clock.tick(FPS)