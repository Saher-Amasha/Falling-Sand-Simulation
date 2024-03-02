"""
Square class
"""

import pygame
from position import Position
from shapes.shape import Shape


class Square(Shape):
    """
    Square class
    """

    def __init__(
        self, shape_id, position: Position, color: str, height: int = 4
    ) -> None:
        super().__init__(shape_id, position, color)
        self.width = height
        self.height = height

    def draw(self, window):
        """
        Draws Square
        """
        return pygame.draw.rect(
            window,
            self.color,
            (self.position.x * 8, self.position.y * 8, self.width, self.height),
        )

    def __str__(self) -> str:
        return super().__str__() + f"Height:{self.height}, Width:{self.width}"
