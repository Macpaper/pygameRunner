import pygame
class SubSpritesheet:
  def __init__(self, image, w, h, colorKey):
    self.surf = pygame.Surface([w, h]).convert_alpha()
    self.w = w
    self.h = h
    self.image = image
    self.colorKey = colorKey
  def get_image(self, x, y, offsetX, offsetY, realWidth, realHeight):
    image = self.surf.blit(self.image, (0, 0), (x * (self.w + offsetX), y * (self.h + offsetY), self.w, self.h))
    image = pygame.transform.scale(self.surf, (realWidth, realHeight))
    image.set_colorkey(self.colorKey) 
    return image