import pygame
from position import Position
from shapes.shape import Shape


class Rectangle(Shape):
    """
    Rectangle class
    """
    def __init__(self, shape_id, position: Position, color: str,height:int,width:int) -> None:
        super().__init__(shape_id, position, color)
        self.width=width
        self.height=height

    def draw(self,window):
        """
        Draws rectangle
        """
        return pygame.draw.rect(window,self.color,
                                (self.position.x*8, self.position.y*8, self.width, self.height))