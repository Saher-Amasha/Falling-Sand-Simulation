"""
Manage and store all shapes
"""

from position import Position
from shapes.rectangle import Rectangle
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

    def add_square(
        self, position: Position, color: str, height: int = 8, width: int = 8
    ):
        """
        Add a square to shapes dict
        """
        shape_id = self.shapes_counter
        self.shapes[self.shapes_counter] = Rectangle(
            shape_id, position=position, color=color, height=height, width=width
        )
        self.shapes_counter += 1
        return shape_id
