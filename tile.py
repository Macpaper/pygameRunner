import pygame
from subspritesheet import SubSpritesheet
from TileEnum import TileEnum
class Tile(pygame.sprite.Sprite):
  TEX_WIDTH = 21
  TEX_HEIGHT = 21
  TEX_OFFSET_X = 2
  TEX_OFFSET_Y = 2
  IMG_WIDTH = 205
  IMG_HEIGHT = 274
  IMG_OFFSET_X = 26
  IMG_OFFSET_Y = 3
  def __init__(self, game, x = 0, y = 0, type=TileEnum.GRASS):
    super().__init__()
    self.type = type
    self.game = game
    self.sheet = self.game.G_SHEET
    self.imageSheet = self.sheet.get_image(self.IMG_OFFSET_X, self.IMG_OFFSET_Y, self.IMG_WIDTH, self.IMG_HEIGHT)
    self.x = x
    self.y = y
    tile_surf = SubSpritesheet(self.imageSheet, self.TEX_WIDTH, self.TEX_HEIGHT, self.sheet.color_key)
    (x, y) = self.get_position()
    tile_img = tile_surf.get_image(x, y, self.TEX_OFFSET_X, self.TEX_OFFSET_Y, 50, 50)
    self.image = tile_img
    self.rect = self.image.get_rect(topleft = (self.x, self.y))
    
  def get_position(self):
    x, y = 0, 0
    if self.type == TileEnum.GRASS:
      x, y = 0, 4
    if self.type == TileEnum.DIRT:
      x, y = 0, 8
    if self.type == TileEnum.SNOW:
      x, y = 0, 2
    if self.type == TileEnum.STONE:
      x, y = 0, 10
    if self.type == TileEnum.VOID:
      x, y = 0, 6
    return (x, y)
  def update(self):
    self.rect.x -= self.game.scroll_speed
    if self.rect.right < 0:
      self.rect.left = self.game.screen.get_width()
     