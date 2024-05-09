from pygame.time import get_ticks

class Timer:
  def __init__(self, duration, repeat = False, autostart = False, callback = None):
    self.duration = duration
    self.start_time = 0
    self.running = False
    self.repeat = repeat
    self.callback = callback
    # print("Timer created", self.duration, self.repeat, self.callback)
    if autostart:
      self.start() 
  def update(self):
    if self.running:
      if get_ticks() - self.start_time >= self.duration:
        if self.callback: self.callback()
        self.stop()

  def start(self):
    self.start_time = get_ticks()
    self.running = True
  
  def stop(self):
    self.running = False
    self.start_time = 0
    if self.repeat: self.start()

  def reset(self):
    self.start_time = get_ticks()
