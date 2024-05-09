import pygame, sys
from Game import GameObj
from spritesheet import Spritesheet

W_WIDTH, W_HEIGHT = 1280, 720

bg_image = pygame.image.load("backgrounds.png")
bg_rect = bg_image.get_rect()
bg_surf = pygame.Surface([bg_rect.width, bg_rect.height/3 * 2])
bg_surf.blit(bg_image, (0, 0), (0, 0, bg_rect.width, bg_rect.height/3))
bg_surf.blit(bg_image, (0, bg_rect.height/3), (0, bg_rect.height/3*2, bg_rect.width, bg_rect.height/3))
bg_surf = pygame.transform.scale(bg_surf, (W_WIDTH, W_HEIGHT))

def main():
  global running, W_WIDTH, W_HEIGHT
  init()
  g = GameObj(screen, clock)
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        sys.exit()

    g.update() 

    screen.fill((150, 250, 200))
    screen.blit(bg_surf, (0, 0))
    g.draw()

    pygame.display.update() 
    clock.tick(60)  

  pygame.quit()

def init():
  global running, screen, clock, W_WIDTH, W_HEIGHT
  pygame.init()
  screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
  pygame.display.set_caption("Pygame Jumper")
  clock = pygame.time.Clock()
  running = True

if __name__ == "__main__":
  main()