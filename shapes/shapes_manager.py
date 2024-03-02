"""
Manage and store all shapes
"""

from position import Position
from shapes.rectangle import Square
from shapes.circle import Circle


class ShapesManager:
    """
    Manage and store all shapes
    """

    def __init__(self) -> None:
        self.shapes_counter = 0
        self.shapes = {}

    def add_circle(self, position: Position, color: str, radius: int = 4):
        """
        Add a circle to shapes dict
        """
        shape_id = self.shapes_counter
        self.shapes[self.shapes_counter] = Circle(
            shape_id, position=position, color=color, radius=radius
        )
        self.shapes_counter += 1
        return shape_id

    def add_square(self, position: Position, color: str, height: int = 8):
        """
        Add a square to shapes dict
        """
        shape_id = self.shapes_counter
        self.shapes[self.shapes_counter] = Square(
            shape_id, position=position, color=color, height=height
        )
        self.shapes_counter += 1
        return shape_id
