from dataclasses import dataclass


@dataclass
class Position:
    """
    Position class contains x y 
    """
    x:int
    y:int
    def to_grid_pos(self,shape_width):
        "converts posittion from pixel coordinates to frid coordinates"""
        return Position(int(self.x/shape_width),int(self.y/shape_width))
