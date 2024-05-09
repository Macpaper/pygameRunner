import pygame
class Spritesheet():
  BLACK = (0, 0, 0)
  def __init__(self, image_src, key):
    self.sheet = pygame.image.load(image_src).convert_alpha()
    self.color_key = key
  def get_image(self, x, y, w, h):
    image = pygame.Surface([w, h]).convert_alpha()
    image.blit(self.sheet, (0, 0), (x, y, w, h))
    return image