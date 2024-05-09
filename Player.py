import pygame
# from spritesheet import Spritesheet
from subspritesheet import SubSpritesheet
class Player(pygame.sprite.Sprite):
  def __init__(self, game):
    super().__init__()
    self.game = game
    # Get global sheet from game. Then get subimage of all the player sprites.
    self.sheet = self.game.G_SHEET                          
    self.imageSheet = self.sheet.get_image(442, 3, 246, 21)

    w, h = 17, 21
    ckey = game.G_COLORKEY_1
    walk_Surf = SubSpritesheet(self.imageSheet, w, h, ckey)
    
    # x, y of texture atlas, offsetX, offsetY, actual width and height
    walk1 = walk_Surf.get_image(1, 0, 6, 0, 90, 100)
    walk2 = walk_Surf.get_image(10, 0, 6, 0, 90, 100)
    walk3 = walk_Surf.get_image(9, 0, 6, 0, 90, 100)
    walk4 = walk_Surf.get_image(10, 0, 6, 0, 90, 100)
    self.player_walk = [walk1, walk2, walk3, walk4]
    self.player_index = 1

    self.image = self.player_walk[self.player_index]
    self.rect = self.image.get_rect(center = (450, 300))
    self.dx = 0
    self.dy = 0
    self.ax = 0
    self.ay = 0
    self.gravity = 1
    
  def update(self):
    self.apply_physics()
    self.player_input()
    self.animation_state()
    # check for collision with enemies
    if pygame.sprite.spritecollide(self, self.game.enemy_sprites, False):
      self.rect.center = (450, 300)
      self.dx = 0
      self.dy = 0
      self.game.scroll_speed = 5
      self.game.player.remove(self)
      self.game.playerDead = True
  def player_input(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and self.rect.bottom >= self.game.screen.get_height() / 2:
      self.dy = -20
    
    self.dx = 5
    if keys[pygame.K_d]:
      self.dx = 10
    if keys[pygame.K_a]:
      self.dx = 0
      self.player_index = 0
    self.game.scroll_speed = self.dx 
    
  def animation_state(self):
    self.player_index += 0.3
    if self.player_index >= len(self.player_walk): self.player_index = 0
    self.image = self.player_walk[int(self.player_index)]
  def apply_gravity(self):
    self.dy += self.gravity
    if self.rect.bottom >= self.game.screen.get_height() / 2:
      self.rect.bottom = self.game.screen.get_height() / 2
  def apply_physics(self):
    self.rect.y += self.dy
    self.dy += self.ay
    # self.rect.x += self.dx
    self.dx += self.ax
    self.apply_gravity()