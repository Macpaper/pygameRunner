import pygame
from subspritesheet import SubSpritesheet
from timer import Timer
class Enemy(pygame.sprite.Sprite):
  def __init__(self, game):
    super().__init__()
    self.game = game
  
    self.sheet = self.game.G_SHEET                          
    self.imageSheet = self.sheet.get_image(305, 292, 62, 8)
    
    w, h = 15, 8
    ox, oy, = 8, 2
    enemy_surf = SubSpritesheet(self.imageSheet, w, h, self.sheet.color_key)
    
    # x, y of texture atlas, offsetX, offsetY, actual width and height
    enemy_walk1 = enemy_surf.get_image(0, 0, ox, oy, 50, 60)
    enemy_walk2 = enemy_surf.get_image(1, 0, ox, oy, 50, 60)
    enemy_walk3 = enemy_surf.get_image(2, 0, ox, oy, 50, 60)

    self.enemy_index = 0
    self.enemy_cycle = [enemy_walk1, enemy_walk2, enemy_walk3]
    self.image = self.enemy_cycle[self.enemy_index]
    self.rect = self.image.get_rect(bottomright = (1250, self.game.screen.get_height() / 2))

    self.timer1 = Timer(500, repeat = False, callback = self.handle_ai)
    self.timer1.start()
    self.dx = -self.game.scroll_speed
    self.dy = 0
    self.ax = 0
    self.ay = 0
    self.gravity = 1 

  def update(self):
    self.apply_physics()
    self.animation_state()
    self.apply_bounds()
    self.timer1.update()

    self.dx = -self.game.scroll_speed
  
  def apply_gravity(self):
    self.dy += self.gravity
    if self.rect.bottom >= self.game.screen.get_height() / 2:
      self.rect.bottom = self.game.screen.get_height() / 2
      if self.timer1.running == False:
        self.timer1.start()
      # if pygame.time.get_ticks() - self.jumpTime > 1000:
      #   self.dy = -20
      #   self.jumpTime = pygame.time.get_ticks()

  def apply_physics(self):
    self.rect.y += self.dy
    self.dy += self.ay
    self.rect.x += self.dx
    self.dx += self.ax
    self.apply_gravity()
    if self.rect.bottom < self.game.screen.get_height() / 2:
      self.rect.x -= 5
  def animation_state(self):
    self.enemy_index += 0.1
    if self.enemy_index >= len(self.enemy_cycle): self.enemy_index = 0
    self.image = self.enemy_cycle[int(self.enemy_index)]
  def apply_bounds(self):
    if self.rect.right < 0:
      self.game.enemy_sprites.remove(self)
  def handle_ai(self):
    # if self.rect.bottom >= self.game.screen.get_height() / 2:
    self.dy = -20 