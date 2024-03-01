from dataclasses import dataclass


@dataclass
class Position:
    x:int
    y:int
    def to_grid_pos(self,shape_width):
        return Position(int(self.x/shape_width),int(self.y/shape_width))