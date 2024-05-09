from TileEnum import TileEnum
from tile import Tile
class Grass(Tile):
  def __init__(self, game, x=0, y=0, type=TileEnum.GRASS):
    super().__init__(game, x, y, type)
    