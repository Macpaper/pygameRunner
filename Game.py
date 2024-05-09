import pygame
from Player import Player
from spritesheet import Spritesheet
from TileEnum import TileEnum
from grass import Grass
from enemy import Enemy
from timer import Timer
from random import randint
import random
class GameObj:
  G_COLORKEY_1 = (94, 129, 162)
  def __init__(self, screen,clock):
    self.G_SHEET = Spritesheet("spritesheet.png", self.G_COLORKEY_1)
    self.screen = screen
    self.clock = clock
    p = Player(self)
    self.player = pygame.sprite.GroupSingle() 
    self.player.add(p)
    self.tile_group = pygame.sprite.Group()
    self.scroll_speed = 5 
    self.enemy_sprites = pygame.sprite.Group()
    self.enemy_sprites.add(Enemy(self))
    self.playerDead = False
    self.timers = {
      "spawn_enemy": Timer(randint(1500, 2500), autostart=True, repeat=True, callback = self.spawn_enemy)
    }

    for i in range(30):  
      tile1 = Grass(self, i * 50 - 200, screen.get_height() / 2, type = list(TileEnum)[i%6])
      self.tile_group.add(tile1)

  def update(self):
    self.player.update()
    self.tile_group.update()
    self.enemy_sprites.update()
    for timer in self.timers.values():
      timer.update()
    
  def spawn_enemy(self):
    self.enemy_sprites.add(Enemy(self))
  
  def draw(self):
    self.player.draw(self.screen)
    self.tile_group.draw(self.screen)
    self.enemy_sprites.draw(self.screen)
    if self.playerDead:
      font = pygame.font.Font(None, 74)
      text = font.render("Game Over", True, (255, 0, 0))
      text_rect = text.get_rect(center = (self.screen.get_width() / 2, self.screen.get_height() / 4))
      self.screen.blit(text, text_rect)
      self.scroll_speed = 0
      self.timers["spawn_enemy"].stop()
