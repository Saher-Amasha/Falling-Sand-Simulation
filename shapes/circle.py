import pygame
from position import Position
from shapes.shape import Shape


class Circle(Shape):
    """
    Circle class
    """

    def __init__(self, shape_id, position: Position, color: str, radius: int) -> None:
        super().__init__(shape_id, position, color)
        self.radius = radius

    def draw(self, window):
        return pygame.draw.circle(
            window, self.color, (self.position.x * 8, self.position.y * 8), self.radius
        )

    def __str__(self) -> str:
        return super().__str__() + f"radius{self.radius}"
